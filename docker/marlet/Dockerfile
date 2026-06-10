# Marlet-branded Mattermost image.
#
# Keeps the server binary 100% stock (official mattermost-team-edition image,
# zero AGPL diff) and swaps only the Apache-2.0-licensed webapp client with the
# Marlet-rebranded build produced by CI (.github/workflows/marlet-build.yml).
#
# Build context must contain the CI-built webapp at ./dist
# (contents of webapp/channels/dist).

FROM mattermost/mattermost-team-edition:10.5

USER root

# Replace the stock client entirely so no stale Mattermost-branded assets remain.
RUN rm -rf /mattermost/client

# Official image runs as user mattermost (uid:gid 2000:2000).
COPY --chown=2000:2000 dist/ /mattermost/client/

USER mattermost
