from typing import Any, Callable, Union, Tuple, Sequence, Optional
from .. import Tensor
from .grad_mode import no_grad as no_grad, enable_grad as enable_grad, \
    set_grad_enabled as set_grad_enabled

# TODO make Variable and Function more precise
class Variable:
    ...

class Function:
    @staticmethod
    def forward(ctx: Any, *args: Any, **kwargs: Any) -> Any: ...
    @staticmethod
    def backward(ctx: Any, *grad_outputs: Any) -> Any: ...

# 'func' accepts a vararg of tensors, which isn't expressable in the type system at the moment.
# If https://mypy.readthedocs.io/en/latest/additional_features.html?highlight=callable#extended-callable-types is accepted,
# the '...' first argument of Callabe can be replaced with VarArg(Tensor).
# For now, we permit any input.
def gradcheck(func: Callable[..., Union[Tensor, Tuple[Tensor, ...]]], inputs: Union[Tensor, Tuple[Tensor, ...]], eps: float=..., atol: float=..., rtol: float=..., raise_exception: bool=..., check_sparse_nnz: bool=...) -> bool: ...
def gradgradcheck(func: Callable[..., Union[Tensor, Tuple[Tensor, ...]]], inputs: Union[Tensor, Tuple[Tensor, ...]], eps: float=..., atol: float=..., rtol: float=..., gen_non_contig_grad_outputs: bool=..., raise_exception: bool=...) -> bool: ...

class detect_anomaly:
    def __enter__(self) -> None: ...
    def __exit__(self, *args: Any) -> bool: ...

class set_detect_anomaly:
    def __init__(self, mode: bool) -> None: ...
    def __enter__(self) -> None:...
    def __exit__(self, *args: Any) -> bool: ...

_TensorOrTensors = Union[Tensor, Sequence[Tensor]]
def backward(tensors: _TensorOrTensors, grad_tensors: Optional[_TensorOrTensors]=..., retain_graph: Optional[bool]=..., create_graph: bool=...) -> None: ...
def grad(outputs: _TensorOrTensors, inputs: _TensorOrTensors, grad_outputs: Optional[_TensorOrTensors]=..., retain_graph: Optional[bool]=..., create_graph: bool=..., only_inputs: bool=..., allow_unused: bool=...) -> Tuple[Tensor, ...]: ...
