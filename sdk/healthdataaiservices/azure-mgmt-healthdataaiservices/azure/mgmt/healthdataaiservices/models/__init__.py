# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import DeidPropertiesUpdate
from ._models import DeidService
from ._models import DeidServiceProperties
from ._models import DeidUpdate
from ._models import ErrorAdditionalInfo
from ._models import ErrorDetail
from ._models import ErrorResponse
from ._models import ManagedServiceIdentity
from ._models import ManagedServiceIdentityUpdate
from ._models import Operation
from ._models import OperationDisplay
from ._models import PrivateEndpoint
from ._models import PrivateEndpointConnection
from ._models import PrivateEndpointConnectionProperties
from ._models import PrivateEndpointConnectionResource
from ._models import PrivateLinkResource
from ._models import PrivateLinkResourceProperties
from ._models import PrivateLinkServiceConnectionState
from ._models import ProxyResource
from ._models import Resource
from ._models import SystemData
from ._models import TrackedResource
from ._models import UserAssignedIdentity

from ._enums import ActionType
from ._enums import CreatedByType
from ._enums import ManagedServiceIdentityType
from ._enums import Origin
from ._enums import PrivateEndpointConnectionProvisioningState
from ._enums import PrivateEndpointServiceConnectionStatus
from ._enums import ProvisioningState
from ._enums import PublicNetworkAccess
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "DeidPropertiesUpdate",
    "DeidService",
    "DeidServiceProperties",
    "DeidUpdate",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ManagedServiceIdentity",
    "ManagedServiceIdentityUpdate",
    "Operation",
    "OperationDisplay",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionProperties",
    "PrivateEndpointConnectionResource",
    "PrivateLinkResource",
    "PrivateLinkResourceProperties",
    "PrivateLinkServiceConnectionState",
    "ProxyResource",
    "Resource",
    "SystemData",
    "TrackedResource",
    "UserAssignedIdentity",
    "ActionType",
    "CreatedByType",
    "ManagedServiceIdentityType",
    "Origin",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ProvisioningState",
    "PublicNetworkAccess",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
