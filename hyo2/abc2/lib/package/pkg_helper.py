import ctypes
import importlib
import logging
import os
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone

import psutil
from appdirs import user_data_dir

from hyo2.abc2.lib.package.pkg_info import PkgInfo

logger = logging.getLogger(__name__)


class PkgHelper:
    """ A collection class with many helper functions, in alphabetic order """

    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)

    def __init__(self, pkg_info: PkgInfo):
        self._pi = pkg_info

    @classmethod
    def clean_folder(cls, folder: str, filter_files: tuple[str] | None, filter_folders: tuple[str] | None) -> None:

        if not os.path.exists(folder):
            raise RuntimeError("Unable to locate the folder to clean: %s" % folder)

        logger.info("cleaning folder: %s ..." % folder)
        if not filter_files:
            filter_files = ()
        logger.debug("file filters: %s" % (filter_files,))
        if not filter_folders:
            filter_folders = ()
        logger.debug("folder filters: %s" % (filter_folders,))

        for dir_path, dir_names, files in os.walk(folder):

            for d in dir_names:

                if d in filter_folders:
                    full_path = os.path.join(dir_path, d)
                    shutil.rmtree(full_path)
                    logger.debug("deleted folder: %s" % full_path)

            for f in files:

                if f in filter_files:
                    full_path = os.path.join(dir_path, f)
                    os.remove(full_path)
                    logger.debug("deleted file: %s" % full_path)

        logger.info("cleaning folder: %s ... DONE" % folder)

    @classmethod
    def explore_folder(cls, path: str) -> bool:
        """Open the passed path using OS-native commands"""

        if cls.is_url(path):
            import webbrowser
            webbrowser.open(path)
            return True

        if not os.path.exists(path):
            logger.warning('invalid path to folder: %s' % path)
            return False

        path = os.path.normpath(path)

        if cls.is_darwin():
            subprocess.call(['open', '--', path])
            return True

        elif cls.is_linux():
            subprocess.call(['xdg-open', path])
            return True

        elif cls.is_windows():
            subprocess.call(['explorer', path])
            return True

        logger.warning("Unknown/unsupported OS")
        return False

    @classmethod
    def first_match(cls, dct, val):
        if not isinstance(dct, dict):
            raise RuntimeError("invalid first input: it is %s instead of a dict" % type(dct))

        # print(dct, val)
        values = [key for key, value in dct.items() if value == val]
        if len(values) != 0:
            return values[0]

        else:
            raise RuntimeError("unknown value %s in dict: %s" % (val, dct))

    @classmethod
    def hstb_atlases_folder(cls) -> str:
        if not cls.is_pydro():
            raise RuntimeError("this method should be called only within a Pydro environment")

        folder = os.path.join(cls.hstb_folder(), os.pardir, os.pardir, os.pardir, os.pardir, "supplementals")
        if not os.path.exists(folder):
            os.mkdir(folder)
        return folder

    @classmethod
    def hstb_folder(cls) -> str:
        if not cls.is_pydro():
            raise RuntimeError("this method should be called only within a Pydro environment")

        # noinspection PyUnresolvedReferences
        from HSTB.explorer import __file__ as hstb_explorer_file

        return os.path.abspath(os.path.join(os.path.dirname(hstb_explorer_file)))

    @classmethod
    def hstb_woa09_folder(cls) -> str:
        if not cls.is_pydro():
            raise RuntimeError("this method should be called only within a Pydro environment")

        try:
            # noinspection PyUnresolvedReferences
            import WOA09
            folder = WOA09.__path__[0]
        except ImportError:
            folder = os.path.join(cls.hstb_atlases_folder(), "woa09")
            if not os.path.exists(folder):
                os.mkdir(folder)
        return folder

    @classmethod
    def hstb_woa13_folder(cls) -> str:
        if not cls.is_pydro():
            raise RuntimeError("this method should be called only within a Pydro environment")

        try:
            # noinspection PyUnresolvedReferences
            import WOA13
            folder = WOA13.__path__[0]
        except ImportError:
            folder = os.path.join(cls.hstb_atlases_folder(), "woa13")
            if not os.path.exists(folder):
                os.mkdir(folder)
        return folder

    @classmethod
    def hstb_woa18_folder(cls) -> str:
        if not cls.is_pydro():
            raise RuntimeError("this method should be called only within a Pydro environment")

        try:
            # noinspection PyUnresolvedReferences
            import WOA18
            folder = WOA18.__path__[0]
        except ImportError:
            folder = os.path.join(cls.hstb_atlases_folder(), "woa18")
            if not os.path.exists(folder):
                os.mkdir(folder)
        return folder

    @classmethod
    def hstb_woa23_folder(cls) -> str:
        if not cls.is_pydro():
            raise RuntimeError("this method should be called only within a Pydro environment")

        try:
            # noinspection PyUnresolvedReferences
            import WOA23
            folder = WOA23.__path__[0]
        except ImportError:
            folder = os.path.join(cls.hstb_atlases_folder(), "woa23")
            if not os.path.exists(folder):
                os.mkdir(folder)
        return folder

    @classmethod
    def is_64bit_os(cls) -> bool:
        """ Check if the current OS is at 64 bits """
        return platform.machine().endswith('64')

    @classmethod
    def is_64bit_python(cls) -> bool:
        """ Check if the current Python is at 64 bits """
        return platform.architecture()[0] == "64bit"

    @classmethod
    def is_darwin(cls) -> bool:
        """ Check if the current OS is Mac OS """
        return sys.platform == 'darwin'

    @classmethod
    def is_linux(cls) -> bool:
        """ Check if the current OS is Linux """
        return sys.platform in ['linux', 'linux2']

    @classmethod
    def is_pydro(cls) -> bool:
        try:
            # noinspection PyUnresolvedReferences
            from HSTB import explorer
            return True

        except ImportError:
            return False

    @classmethod
    def is_script_already_running(cls, python_only: bool = False) -> bool:

        script_name = os.path.basename(sys.argv[0])
        # logger.info("script name: %s" % script_name)

        process_counter = 0

        # get a list with the running processes
        for pid in psutil.pids():

            try:
                # get the process from id
                proc = psutil.Process(pid)

                if python_only:
                    # check if it is an instance of Python
                    if proc.name() != "python.exe":
                        continue

                # check if the name of the script is being called
                try:
                    command_line = proc.cmdline()
                except Exception:
                    continue

                # for Windows 10
                if isinstance(command_line, list):
                    for command_parameter in command_line:
                        if script_name in command_parameter:
                            process_counter += 1
                            if process_counter > 1:
                                logger.info("%s already in execution" % script_name)

                # for other Windows versions
                elif script_name in proc.cmdline():
                    process_counter += 1
                    if process_counter > 1:
                        logger.info("%s already in execution" % script_name)

            # a process of the list can end itself during the survey
            except psutil.NoSuchProcess:
                logger.debug('Skipping process %s' % pid)

        # if the script is already running there will be two instances
        return process_counter > 1

    @classmethod
    def is_url(cls, value) -> bool:
        if len(value) > 7:

            https = "http"
            if value[:len(https)] == https:
                return True

        return False

    @classmethod
    def is_user_admin(cls):
        if cls.is_windows():

            if ctypes.windll.shell32.IsUserAnAdmin():
                logger.debug("user is admin")
                return True
            else:
                logger.debug("user is not admin")
                return False

        else:
            raise RuntimeError("Windows only")

    @classmethod
    def is_windows(cls) -> bool:
        """ Check if the current OS is Windows """
        return (sys.platform == 'win32') or (os.name == "nt")

    @classmethod
    def python_path(cls):
        """ Return the python site-specific directory prefix (the temporary folder for PyInstaller) """

        # required by PyInstaller
        if hasattr(sys, '_MEIPASS'):
            if cls.is_windows():
                import win32api
                # noinspection PyProtectedMember
                return win32api.GetLongPathName(sys._MEIPASS)
            else:
                # noinspection PyProtectedMember
                return sys._MEIPASS

        # check if in a virtual environment
        if hasattr(sys, 'real_prefix'):

            if cls.is_windows():
                import win32api
                # noinspection PyProtectedMember
                return win32api.GetLongPathName(sys.real_prefix)
            else:
                return sys.real_prefix

        return sys.prefix

    @classmethod
    def timestamp(cls) -> str:
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @classmethod
    def truncate_too_long(cls, path: str, max_path_length: int = 260, left_truncation: bool = False) -> str:

        max_len = max_path_length

        path_len = len(path)
        if path_len < 260:
            return path

        logger.debug("path truncation required since path would be longer than %d [left: %s]"
                     % (max_len, left_truncation))

        folder_path, filename = os.path.split(path)
        file_base, file_ext = os.path.splitext(filename)

        if left_truncation:
            new_len = max_len - len(folder_path) - len(file_ext) - 2
            if new_len < 1:
                raise RuntimeError("the passed path is too long: %d" % path_len)
            path = os.path.join(folder_path, file_base[(len(file_base) - new_len):] + file_ext)

        else:
            new_len = max_len - len(folder_path) - len(file_ext) - 2
            if new_len < 1:
                raise RuntimeError("the passed path is too long: %d" % path_len)
            path = os.path.join(folder_path, file_base[:new_len] + file_ext)

        return path

    def explore_pkg_folder(self) -> None:
        self.explore_folder(self.pkg_folder())

    def hydroffice_folder(self) -> str:
        return os.path.abspath(os.path.join(self.pkg_folder(), os.pardir))

    def pkg_folder(self):
        _dir = user_data_dir(self._pi.name, "HydrOffice")
        if not os.path.exists(_dir):  # create it if it does not exist
            os.makedirs(_dir)

        return _dir

    def pkg_info(self, qt_html: bool = False, with_ocs_email: bool = False) -> str:

        def style_row(raw_row: str, is_h1: bool = False, is_h2: bool = False) -> str:
            if qt_html:
                if is_h1:
                    return "<h1>%s</h1>" % raw_row
                elif is_h2:
                    return "<h2>%s</h2>" % raw_row
                else:
                    return "<p>%s</p>" % raw_row
            else:
                if is_h1:
                    return "%s:\n" % raw_row
                elif is_h2:
                    return "[%s]\n" % raw_row
                else:
                    return "  - %s\n" % raw_row

        def style_url(text: str, url: str) -> str:
            if qt_html:
                return "<a href=\"%s\">%s</a>" % (url, text,)
            else:
                return "%s(%s)" % (text, url)

        def style_mailto(text: str, url: str) -> str:
            if qt_html:
                return "<a href=\"mailto:%s?Subject=%s%%20v.%s\" target=\"_top\">%s</a>" \
                    % (url, self._pi.name, self._pi.version, text,)
            else:
                return "%s(%s)" % (text, url)

        def package_version(package: str) -> str:
            try:
                return importlib.import_module("%s" % package).__version__
            except (ImportError, AttributeError):
                try:
                    return importlib.import_module("%s" % package).VERSION
                except (ImportError, AttributeError):

                    def import_class(cl):
                        d = cl.rfind(".")
                        classname = cl[d + 1:len(cl)]
                        m = __import__(cl[0:d], globals(), locals(), [classname])
                        return getattr(m, classname)

                    try:
                        return import_class("%s" % package).version()
                    except (ImportError, AttributeError):
                        return "N/A"

        msg = str()

        msg += style_row("General Info", is_h2=True)
        msg += style_row("version: %s" % self._pi.version)
        msg += style_row("author: %s" % style_mailto(self._pi.author, self._pi.author_email))
        msg += style_row("general support: %s" % style_mailto(self._pi.support_email, self._pi.support_email))
        if with_ocs_email:
            msg += style_row(
                "NOAA support: %s" % style_mailto("ocs.qctools@noaa.gov", "ocs.qctools@noaa.gov"))
        msg += style_row("website: %s" % style_url(self._pi.url, self._pi.url))
        msg += style_row("license: %s" % style_url(self._pi.lic, self._pi.lic_url))

        msg += style_row("Hosting Environment", is_h2=True)
        msg += style_row("os: %s %s-bit" % (os.name, "64" if self.is_64bit_os() else "32"))
        msg += style_row("python: %s %s-bit" % (platform.python_version(), "64" if self.is_64bit_python() else "32"))
        msg += style_row("pydro: %s" % self.is_pydro())

        msg += style_row("Dependencies", is_h2=True)
        for key in self._pi.deps_dict.keys():
            msg += style_row("%s: %s" % (key, package_version(self._pi.deps_dict[key]),))

        return msg

    def web_url(self, suffix: str | None = None) -> str:

        url = '%s%s' % (self._pi.url, self._pi.version.replace('.', '_'),)
        if self.is_pydro():
            url += "_pydro"

        if suffix and isinstance(suffix, str):
            url += "_" + suffix

        return url
