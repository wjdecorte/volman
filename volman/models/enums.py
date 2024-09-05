from dataclasses import dataclass


@dataclass(frozen=True)
class Protocol:
    SFTP: str = "sftp"
    S3: str = "s3"


@dataclass(frozen=True)
class FileType:
    FULL_FILE: str = "full-file"
    INCREMENTAL: str = "incremental"


@dataclass(frozen=True)
class ColumnMappingPolicy:
    POSITIONAL_BASED: str = "positional-based"
    NAME_BASED: str = "name-based"


@dataclass(frozen=True)
class IntervalUnit:
    MINUTES: str = "minutes"
    HOURS: str = "hours"
    DAYS: str = "days"


@dataclass(frozen=True)
class TransportType:
    INBOUND: str = "inbound"
    OUTBOUND: str = "outbound"


@dataclass(frozen=True)
class CredentialType:
    SSHKEY: str = "sshkey"
    PASSWORD: str = "password"
