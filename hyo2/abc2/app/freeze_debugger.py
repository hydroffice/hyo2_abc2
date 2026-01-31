import faulthandler
import os
import threading
import time
from datetime import datetime

from PySide6.QtCore import QObject, QTimer


class FreezeDebugger(QObject):

    @classmethod
    def ts(cls) -> str:
        # Local wall-clock time for human reading + monotonic for intervals
        return f"{datetime.now().isoformat(timespec='seconds')} | mono={time.monotonic():.3f}"

    def __init__(self, parent: QObject, log_path: str, heartbeat_ms: int = 300, write_every: float = 5,
                 stall_s: float = 4.5):
        super().__init__(parent)

        self.stall_s: float = stall_s
        self.last_beat: float = time.monotonic()
        self.dumped_for_this_stall: bool = False

        # Log file (line-buffered)
        self.log = open(log_path, "w", buffering=1, encoding="utf-8")
        self.log.write(f"\n{self.ts()} --- debugger start pid={os.getpid()} ---\n")
        faulthandler.enable(file=self.log, all_threads=True)

        # Heartbeat timer (must live in GUI thread + have a parent)
        self.gui_timer = QTimer(self)
        self.gui_timer.timeout.connect(self._beat)
        self.gui_timer.start(heartbeat_ms)

        # Python watchdog thread (independent of Qt event loop)
        self._stop = threading.Event()
        self.thread = threading.Thread(target=self._loop, args=(write_every,), daemon=True)
        self.thread.start()
        print("FREEZE DEBUGGER STARTED")

    def _beat(self) -> None:
        self.last_beat = time.monotonic()
        self.dumped_for_this_stall = False  # reset once GUI is alive again

    def _loop(self, write_every):
        counter = 0
        while not self._stop.is_set():
            time.sleep(1)
            if self._stop.is_set():  # if the stop is set during the sleeping
                break

            counter += 1
            if counter != write_every:
                continue

            counter = 0
            stalled_for = time.monotonic() - self.last_beat
            self.log.write(f"{self.ts()} [debugger] alive stalled_for={stalled_for:.3f}s\n")

            if stalled_for > self.stall_s and not self.dumped_for_this_stall:
                self.dumped_for_this_stall = True
                self.log.write(f"{self.ts()} [debugger] GUI stalled for {stalled_for:.3f}s — dumping stacks\n")
                faulthandler.dump_traceback(file=self.log, all_threads=True)

    def stop(self):
        self.log.write(f"{self.ts()} [debugger] stop\n")
        self.log.close()
        self._stop.set()
