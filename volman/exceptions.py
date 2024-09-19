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
class InvalidValueError(AppBaseError):
    http_code: int = 400


@dataclass(frozen=True)
class InvalidActionError(AppBaseError):
    message: str = "Invalid action provided"
    http_code: int = 400


@dataclass(frozen=True)
class ExecutionError(AppBaseError):
    http_code: int = 500


@dataclass(frozen=True)
class UniqueColumnNotFoundError(AppBaseError):
    http_code: int = 500
