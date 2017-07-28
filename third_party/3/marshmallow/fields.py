"""Stub for field classes for various types of data."""

from typing import Any, Optional, Callable, Dict as _Dict


class Field:
    def __init__(self,
                 default: Any = None,
                 attribute: Optional[str] = None,
                 load_from: Optional[str] = None,
                 dump_to: Optional[str] = None,
                 validate: Optional[Callable] = None,
                 required: bool = False,
                 allow_none: Optional[bool] = None,
                 load_only: bool = False,
                 dump_only: bool = False,
                 missing: Any = None,
                 error_messages: Optional[_Dict[str, str]]=None) -> None:
        ...

    def _deserialize(self, value: Any, attr: Any, data: Any) -> Any:
        ...


class Raw(Field):
    ...


class Nested(Field):
    ...


class List(Field):
    def __init__(self, cls_or_instance: Any) -> None:
        ...


class String(Field):
    ...


class UUID(String):
    ...


class Number(Field):
    ...


class Integer(Number):
    ...


class Decimal(Number):
    def __init__(self, places: Optional[int] = None) -> None:
        ...


class Boolean(Field):
    ...


class FormattedString(Field):
    ...


class Float(Number):
    ...


class DateTime(Field):
    ...


class LocalDateTime(DateTime):
    ...


class Time(Field):
    ...

class Date(Field):
    ...


class Dict(Field):
    ...


class ValidatedField(Field):
    ...


Str = String
