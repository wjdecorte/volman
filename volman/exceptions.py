from dataclasses import dataclass
from typing import Dict, Type

ALL_EXCEPTIONS: Dict[str, Type] = {}


@dataclass(frozen=True)
class AppBaseError(Exception):
    """App Base Exception"""

    message: str = "Base exception"
    http_code: int = 500

    @property
    def code(self):
        return f"connectors.error.{self.error_number}"

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.error_number = f"{len(ALL_EXCEPTIONS):03}"
        ALL_EXCEPTIONS[cls.__name__] = cls


@dataclass(frozen=True)
class TestError(AppBaseError):
    message: str = "Test exception"


@dataclass(frozen=True)
class HTTPTestError(AppBaseError):
    http_code: int = 403


@dataclass(frozen=True)
class ConnectorNotFoundError(AppBaseError):
    http_code: int = 404


@dataclass(frozen=True)
class ConnectorAlreadyExistsError(AppBaseError):
    http_code: int = 409


@dataclass(frozen=True)
class InvalidValueError(AppBaseError):
    http_code: int = 400


@dataclass(frozen=True)
class InvalidActionError(AppBaseError):
    message: str = "Invalid action provided"
    http_code: int = 400


@dataclass(frozen=True)
class FileWriteError(AppBaseError):
    message: str = "Failed to write the file"
    http_code: int = 500


@dataclass(frozen=True)
class MissingPluginError(AppBaseError):
    http_code: int = 500


@dataclass(frozen=True)
class ExecutionError(AppBaseError):
    http_code: int = 500


@dataclass(frozen=True)
class AuthenticationError(AppBaseError):
    message: str = "Error occurred while fetching access token"
    http_code: int = 500


@dataclass(frozen=True)
class DatasetFetchError(AppBaseError):
    message: str = "Error occurred while fetching dataset : %message%"
    http_code: int = 500


@dataclass(frozen=True)
class InvalidTokenError(AppBaseError):
    message: str = "Invalid Token : %message%"
    http_code: int = 401


@dataclass(frozen=True)
class InvalidSchemaError(AppBaseError):
    message: str = "Invalid Schema : %message%"
    http_code: int = 500


@dataclass(frozen=True)
class SchemaFetchError(AppBaseError):
    message: str = "Schema fetch error : %message%"
    http_code: int = 500


@dataclass(frozen=True)
class APIKeyNotFoundError(AppBaseError):
    http_code: int = 404


@dataclass(frozen=True)
class APIKeyDeletedError(AppBaseError):
    message: str = "API key is in deleted status"
    http_code: int = 500


@dataclass(frozen=True)
class APIKeyClientIdMismatchError(AppBaseError):
    message: str = "Client Id Mismatch"
    http_code: int = 500


@dataclass(frozen=True)
class UniqueColumnNotFoundError(AppBaseError):
    http_code: int = 500
