# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ApplicationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Object representing the application type of the Confidential Ledger. Defaults to
    ConfidentialLedger.
    """

    CONFIDENTIAL_LEDGER = "ConfidentialLedger"
    CODE_TRANSPARENCY = "CodeTransparency"


class CheckNameAvailabilityReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reason why the given name is not available."""

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class EnclavePlatform(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Object representing the enclave platform for the Confidential Ledger application. Defaults to
    IntelSgx.
    """

    INTEL_SGX = "IntelSgx"
    AMD_SEV_SNP = "AmdSevSnp"


class LanguageRuntime(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Object representing LanguageRuntime for Manged CCF."""

    CPP = "CPP"
    JS = "JS"


class LedgerRoleName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LedgerRole associated with the Security Principal of Ledger."""

    READER = "Reader"
    CONTRIBUTOR = "Contributor"
    ADMINISTRATOR = "Administrator"


class LedgerSku(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SKU associated with the ledger resource."""

    STANDARD = "Standard"
    BASIC = "Basic"
    UNKNOWN = "Unknown"


class LedgerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the ledger. Private means transaction data is encrypted."""

    UNKNOWN = "Unknown"
    PUBLIC = "Public"
    PRIVATE = "Private"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Object representing ProvisioningState for Confidential Ledger."""

    UNKNOWN = "Unknown"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    CREATING = "Creating"
    DELETING = "Deleting"
    UPDATING = "Updating"


class RunningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Object representing RunningState for Confidential Ledger."""

    ACTIVE = "Active"
    PAUSED = "Paused"
    UNKNOWN = "Unknown"
    PAUSING = "Pausing"
    RESUMING = "Resuming"
