// Copyright (c) 2015-present Mattermost, Inc. All Rights Reserved.
// See LICENSE.txt for license information.

import React from 'react';
import type {CSSProperties} from 'react';
import {useIntl} from 'react-intl';

// Marlet placeholder mark (martlet) — final mark TBD
export default function MattermostLogo(props: React.HTMLAttributes<HTMLSpanElement>) {
    const {formatMessage} = useIntl();
    return (
        <span {...props}>
            <svg
                version='1.1'
                x='0px'
                y='0px'
                viewBox='0 0 64 64'
                role='img'
                aria-label={formatMessage({id: 'generic_icons.mattermost', defaultMessage: 'Marlet Logo'})}
            >
                <path
                    style={style}
                    d='M8 44 C14 28 26 18 40 16 C36 20 34 24 34 28 C42 22 52 20 58 21 C52 24 48 28 46 32 C50 31 54 31 56 32 C44 36 36 44 32 52 C28 46 22 44 16 45 C12 45.5 9 45 8 44 Z'
                />
            </svg>
        </span>
    );
}

const style: CSSProperties = {
    fillRule: 'evenodd',
    clipRule: 'evenodd',
};
