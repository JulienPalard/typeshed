from typing import NamedTuple, Any, Dict, Callable, Optional


MarshalResult = NamedTuple(
    'MarshalResult',
    [('data', Dict[str, Any]),
     ('errors', Dict[str, Any])])

UnmarshalResult = NamedTuple(
    'UnmarshalResult',
    [('data', Dict[str, Any]),
     ('errors', Dict[str, Any])])


class Schema:
    def __init__(self,
                 only: tuple = (),
                 exclude: tuple = (),
                 prefix: str = '',
                 strict: Optional[bool] = None,
                 many: bool = False,
                 load_only: tuple = (),
                 dump_only: tuple = (),
                 partial: bool = False) -> None:
        ...

    def load(self,
             data: Dict[str, Any],
             many: Optional[bool] = None,
             partial: Optional[bool] = None) -> UnmarshalResult:
        ...

    def dump(self,
             obj: Dict[str, Any],
             many: Optional[bool] = None,
             update_fields: bool = True) -> UnmarshalResult:
        ...

def post_load(fn: Callable,
              pass_many: bool = False,
              pass_original: bool = False) -> Callable:
    ...
