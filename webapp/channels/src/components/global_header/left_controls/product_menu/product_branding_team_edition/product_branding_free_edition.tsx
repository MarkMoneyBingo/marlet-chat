// Copyright (c) 2015-present Mattermost, Inc. All Rights Reserved.
// See LICENSE.txt for license information.

import React from 'react';
import styled from 'styled-components';

import Logo from 'components/common/svg_images_components/logo_dark_blue_svg';

const ProductBrandingFreeEditionContainer = styled.span`
    display: flex;
    align-items: center;

    > * + * {
        margin-left: 8px;
    }
`;

const StyledLogo = styled(Logo)`
    path {
        fill: rgba(var(--sidebar-text-rgb), 0.75);
    }
`;

// Marlet: no edition badge — licensing SKUs are not part of the product surface.
const ProductBrandingFreeEdition = (): JSX.Element => {
    return (
        <ProductBrandingFreeEditionContainer tabIndex={-1}>
            <StyledLogo
                width={116}
                height={20}
            />
        </ProductBrandingFreeEditionContainer>
    );
};

export default ProductBrandingFreeEdition;
