from PySide6 import QtCore, QtWidgets
import traceback
import logging

from hyo2.abc2.lib.progress.abstract_progress import AbstractProgress

logger = logging.getLogger(__name__)


class QtProgress(AbstractProgress):
    """Qt-based implementation of a progress bar. It does NOT run backwards"""

    def __init__(self, parent: QtWidgets.QWidget | None) -> None:
        super().__init__()
        self._parent = parent
        self._qt_app = QtWidgets.QApplication
        self._progress: QtWidgets.QProgressDialog | None = None

    @property
    def canceled(self) -> bool:
        """Currently, always false"""
        if self._progress is not None:
            self._is_canceled = self._progress.wasCanceled()
        return self._is_canceled

    def start(self, title: str = "Progress", text: str = "Processing", min_value: float = 0.0, max_value: float = 100.0,
              init_value: float = 0.0, has_abortion: bool = False, is_disabled: bool = False) -> None:

        self._is_disabled = is_disabled
        if is_disabled:
            return

        if title is not None:
            self._title = title
        if text is not None:
            self._text = text

        # set initial values
        if min_value >= max_value:
            raise RuntimeError("invalid min and max values: min %d, max %d" % (min_value, max_value))
        self._min = min_value
        self._max = max_value
        self._range = self._max - self._min
        if init_value < min_value:
            raise RuntimeError("invalid init value: init %d, min %d" % (init_value, min_value))
        self._value = init_value

        self._is_canceled = False
        if self._progress is None:
            self._progress = QtWidgets.QProgressDialog(self._parent)
        self._progress.setWindowTitle(title)
        self._progress.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        if not has_abortion:
            # noinspection PyTypeChecker
            self._progress.setCancelButton(None)
        self._progress.setMinimumDuration(1000)

        self._display()
        self._progress.setVisible(True)

    def update(self, value: float = None, text: str | None = None, restart: bool = False) -> None:
        if self._is_disabled:
            return

        if value is not None:
            if (value < self._value) and not restart:
                logger.warning('attempt to update current progress value (%d) with a smaller value (%d)'
                               % (self._value, value))
            if value < self._min:
                logger.warning('attempt to update current progress value (%d) < valid range(%s %s)'
                               % (value, self._min, self._max))
                value = self._min
            if value > self._max:
                logger.warning('attempt to update current progress value (%d) > valid range(%s %s)'
                               % (value, self._min, self._max))
                value = self._max
            self._value = value

        if text is not None:
            self._text = text

        self._display()

    def add(self, quantum: float, text: str | None = None) -> None:
        if self._is_disabled:
            return

        tmp_value = self._value + quantum

        if tmp_value < self._value:
            logger.warning('attempt to update current progress value (%d) with a smaller value (%d)'
                           % (self._value, tmp_value))
        if tmp_value < self._min:
            logger.warning('attempt to update current progress value (%d) < valid range(%s %s)'
                           % (tmp_value, self._min, self._max))
            tmp_value = self._min
        if tmp_value > self._max:
            logger.warning('attempt to update current progress value (%d) > valid range(%s %s)'
                           % (tmp_value, self._min, self._max))
            tmp_value = self._max

        self._value = tmp_value
        if text is not None:
            self._text = text

        # logger.info('added %.4f: %.4f' % (quantum, self._value))

        self._display()

    def auto(self, text: str | None = None) -> None:
        if self._is_disabled:
            return
        self._auto_value()
        if text is not None:
            self._text = text
        self._display()

    def end(self) -> None:
        self._value = self._max
        self._text = 'Done!'
        self._display()
        self._progress.setHidden(True)

    def _display(self) -> None:

        if self._progress is None:
            logger.info("The progress bar was not started")
            for line in traceback.format_stack():
                logger.debug("- %s" % line.strip())
            return

        self._progress.setLabelText(self._text)
        self._progress.forceShow()
        self._progress.setValue(int(((self._value - self._min) / self._range) * 100))

        # noinspection PyArgumentList
        self._qt_app.processEvents()
