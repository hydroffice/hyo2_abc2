import logging
from abc import ABCMeta, abstractmethod

logger = logging.getLogger(__name__)


class AbstractProgress(metaclass=ABCMeta):
    """Abstract class for a progress bar"""

    def __init__(self) -> None:
        self._title: str = str()
        self._text: str = str()

        self._min: float = 0.0
        self._max: float = 100.0
        self._range: float = self._max - self._min
        self._value: float = 0.0

        self._is_disabled: bool = False
        self._is_canceled: bool = False

    @property
    def value(self) -> float:
        return self._value

    @property
    def text(self) -> str:
        return self._text

    @property
    def title(self) -> str:
        return self._title

    @property
    def min(self) -> float:
        return self._min

    @property
    def max(self) -> float:
        return self._max

    @property
    def range(self) -> float:
        self._range = self._max - self._min
        return self._range

    @property
    @abstractmethod
    def canceled(self) -> bool:
        pass

    @abstractmethod
    def start(self, title: str = "Progress", text: str = "Processing", min_value: float = 0.0, max_value: float = 100.0,
              init_value: float = 0.0, has_abortion: bool = False, is_disabled: bool = False) -> None:
        pass

    @abstractmethod
    def update(self, value: float = None, text: str = None, restart: bool = False) -> None:
        pass

    @abstractmethod
    def add(self, quantum: float, text: str = None) -> None:
        pass

    def _auto_value(self, min_step: float = 1e-10, max_step: float = 1.0) -> None:
        # progress in [0, 1]
        p = max(0.0, min(1.0, self._value / self._max))

        # quadratic falloff toward max
        self._value += min_step + (max_step - min_step) * (1.0 - p) ** 2

    @abstractmethod
    def auto(self) -> None:
        pass

    @abstractmethod
    def end(self) -> None:
        pass
