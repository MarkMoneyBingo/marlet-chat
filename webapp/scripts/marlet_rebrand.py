#!/usr/bin/env python3
"""Marlet rebrand for webapp i18n strings.

Replaces user-facing "Mattermost" with "Marlet" in
webapp/channels/src/i18n/en.json, EXCEPT in strings that reference
licensing, trademarks, copyright, the about-box attribution, or
Mattermost-owned URLs/domains/emails.

Deterministic and idempotent so it can be re-run after upstream merges:

    python webapp/scripts/marlet_rebrand.py            # apply changes
    python webapp/scripts/marlet_rebrand.py --dry-run  # report only

Prints a report of every skipped string and the rule that skipped it.
"""

import argparse
import json
import re
import sys
from pathlib import Path

EN_JSON = Path(__file__).resolve().parents[1] / "channels" / "src" / "i18n" / "en.json"

# ---------------------------------------------------------------------------
# Exclusion rules. A string is left untouched if ANY rule matches.
# Each rule: (name, predicate(key, value) -> bool)
# ---------------------------------------------------------------------------

# Key prefixes that are excluded wholesale (about box = upstream attribution).
EXCLUDED_KEY_PREFIXES = (
    "about.",
)

# Specific keys excluded regardless of content (extend after upstream merges
# if new attribution/legal strings appear that the regex rules miss).
EXCLUDED_KEYS: set[str] = set()

# Mattermost-owned domains / URL fragments / emails must never be rewritten.
URL_RE = re.compile(
    r"(?i)("
    r"[\w.-]*mattermost[\w-]*\.(com|org|io)"  # mattermost.com, docs.mattermost.com, ...
    r"|your-mattermost-url"                   # placeholder URL chunks in setup docs
    r"|github\.com/mattermost"
    r")"
)

# Legal / licensing language: these strings describe Mattermost Inc.'s own
# commercial licenses, agreements, trademarks or copyright and must keep the
# original name.
LEGAL_RE = re.compile(
    r"(?i)(licen[cs]e|trademark|copyright|©|legal@|Mattermost,? Inc"
    r"|agree to the terms|agreement)"
)

RULES = [
    ("about-box", lambda k, v: k.startswith(EXCLUDED_KEY_PREFIXES)),
    ("excluded-key", lambda k, v: k in EXCLUDED_KEYS),
    ("url/domain/email", lambda k, v: bool(URL_RE.search(v))),
    ("licensing/trademark/copyright", lambda k, v: bool(LEGAL_RE.search(v))),
]

BRAND_RE = re.compile(r"[Mm]attermost")


def rebrand(value: str) -> str:
    return BRAND_RE.sub(lambda m: "Marlet" if m.group(0)[0] == "M" else "marlet", value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="report without writing")
    args = parser.parse_args()

    raw = EN_JSON.read_text(encoding="utf-8")
    data = json.loads(raw)

    replaced = 0
    replaced_occurrences = 0
    skipped: list[tuple[str, str, str]] = []  # (key, rule, value)

    for key, value in data.items():
        if not BRAND_RE.search(value):
            continue
        matched_rule = next((name for name, pred in RULES if pred(key, value)), None)
        if matched_rule:
            skipped.append((key, matched_rule, value))
            continue
        replaced_occurrences += len(BRAND_RE.findall(value))
        data[key] = rebrand(value)
        replaced += 1

    print(f"Strings rebranded:   {replaced} ({replaced_occurrences} occurrences)")
    print(f"Strings skipped:     {len(skipped)}")
    print()
    print("=== Skipped strings (kept as Mattermost) ===")
    for key, rule, value in skipped:
        one_line = value.replace("\n", "\\n")
        if len(one_line) > 120:
            one_line = one_line[:117] + "..."
        print(f"[{rule}] {key}: {one_line}")

    if args.dry_run:
        print("\n--dry-run: no files written")
        return 0

    out = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    EN_JSON.write_text(out, encoding="utf-8", newline="\n")
    print(f"\nWrote {EN_JSON}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
