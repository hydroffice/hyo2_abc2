import ctypes
import sys
from ctypes import wintypes


class WinApp:

    @classmethod
    def set_app_user_model_id(cls, app_id: str) -> None:
        # This is needed to display the app icon on the taskbar
        if sys.platform != "win32":
            return

        shell32 = ctypes.WinDLL("shell32", use_last_error=True)

        set_app_id = shell32.SetCurrentProcessExplicitAppUserModelID
        set_app_id.argtypes = [wintypes.LPCWSTR]
        set_app_id.restype = ctypes.c_long  # HRESULT

        result = set_app_id(app_id)
        if result != 0:
            raise ctypes.WinError(ctypes.get_last_error())
