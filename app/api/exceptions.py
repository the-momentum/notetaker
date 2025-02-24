from typing import TYPE_CHECKING, Any, Sequence

from pydantic import BaseModel
from pydantic.error_wrappers import ErrorList, ErrorWrapper

if TYPE_CHECKING:
    from pydantic.error_wrappers import Loc


class ValidationErrorModel(BaseModel):
    pass


class BaseValidationError(Exception):
    def __init__(self, errors: Sequence[ErrorList]) -> None:
        self._errors = errors
        super().__init__()

    def errors(self) -> Sequence[ErrorList]:
        """Return the list of errors."""
        return self._errors


class ValidationError(BaseValidationError):
    def __init__(self, exc: Exception, loc: "Loc", body: Any = None) -> None:
        self.body = body
        self.exc = exc
        self.loc = loc

        super().__init__([self.to_wrapper()])

    def to_wrapper(self) -> ErrorWrapper:
        return ErrorWrapper(exc=self.exc, loc=self.loc)


class BaseError(Exception):
    pass
