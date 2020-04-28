from .abstract_optimizer import AbstractOptimizer

from .ada_delta import AdaDelta
from .ada_grad import AdaGrad
from .ada_max import AdaMax
from .ams_grad import AmsGrad
from .momentum import Momentum
from .rms_prop import RmsProp
from .sgd import Sgd

from .stochastic_reconfiguration import SR

try:
    import torch as _torch
    from .torch import Torch
except:
    pass


try:
    import jax
    from .jax import Jax
except:
    pass
