// Copyright (c) 2015-present Mattermost, Inc. All Rights Reserved.
// See LICENSE.txt for license information.

import React from 'react';
import styled from 'styled-components';

type Props = {
    width?: number;
    height?: number;
    className?: string;
}

const Svg = styled.svg.attrs({
    version: '1.1',
    xmlns: 'http://www.w3.org/2000/svg',
    xmlnsXlink: 'http://www.w3.org/1999/xlink',
})``;

// Marlet placeholder wordmark (martlet mark + name) — final mark TBD
export default (props: Props) => (
    <Svg
        className={props.className}
        width={props.width ? props.width.toString() : '182'}
        height={props.height ? props.height.toString() : '30'}
        viewBox='0 0 240 64'
        fill='none'
        xmlns='http://www.w3.org/2000/svg'
    >
        <path
            fillRule='evenodd'
            clipRule='evenodd'
            fill='currentColor'
            d='M8 44 C14 28 26 18 40 16 C36 20 34 24 34 28 C42 22 52 20 58 21 C52 24 48 28 46 32 C50 31 54 31 56 32 C44 36 36 44 32 52 C28 46 22 44 16 45 C12 45.5 9 45 8 44 Z'
        />
        <text
            x='72'
            y='44'
            fontFamily='Metropolis, Segoe UI, Helvetica, Arial, sans-serif'
            fontSize='32'
            fontWeight='700'
            fill='currentColor'
        >
            {'marlet'}
        </text>
    </Svg>
);
