import inspect
import logging
import os
from shutil import copytree, rmtree

logger = logging.getLogger(__name__)


class Testing:

    def __init__(self, root_folder: str | None = None):

        if root_folder is None:  # Identify repository root folder of caller by finding parent folder with setup.py
            parent_frame = inspect.currentframe().f_back  # Get caller functions frame
            parent_filepath = os.path.abspath(inspect.getframeinfo(parent_frame).filename)  # Get filename of caller
            parent_dir = os.path.dirname(parent_filepath)

            while True:
                if os.path.exists(os.path.join(parent_dir, "setup.py")):
                    root_folder = parent_dir
                    break
                next_parent = os.path.abspath(os.path.join(parent_dir, os.path.pardir))
                if next_parent == parent_dir:  # We've hit file system root
                    raise RuntimeError("Cannot identify repository root. "
                                       f"Not setup.py found in any parents of {parent_dir}")
                parent_dir = next_parent

        if not os.path.exists(root_folder):
            raise RuntimeError("passed invalid root folder: %s" % root_folder)
        self.root_folder = root_folder

    # --- FOLDERS ---

    def root_data_folder(self) -> str:
        data_folder = os.path.abspath(os.path.join(self.root_folder, 'data'))
        if not os.path.exists(data_folder):
            raise RuntimeError("the root test data folder does not exist: %s" % data_folder)
        return data_folder

    def input_data_folder(self) -> str:
        folder = os.path.abspath(os.path.join(self.root_data_folder(), 'input'))
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    def input_data_sub_folders(self, prefix: str | None = None) -> list[str]:
        """Return a list of sub-folders under the input folder"""
        folder_list = list()
        list_dir = os.listdir(self.input_data_folder())
        for element in list_dir:
            element_path = os.path.join(self.input_data_folder(), element)
            if os.path.isdir(element_path):
                if prefix is None or element.startswith(prefix):
                    folder_list.append(element_path)
        return folder_list

    def download_data_folder(self) -> str:
        folder = os.path.abspath(os.path.join(self.root_data_folder(), 'download'))
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    def temp_data_folder(self) -> str:
        folder = os.path.abspath(os.path.join(self.root_data_folder(), 'temp'))
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    def temp_data_sub_folders(self, prefix: str | None = None) -> list[str]:
        """Return a list of sub-folders under the input folder"""
        folder_list = list()
        list_dir = os.listdir(self.temp_data_folder())
        for element in list_dir:
            element_path = os.path.join(self.temp_data_folder(), element)
            if os.path.isdir(element_path):
                if prefix is None or element.startswith(prefix):
                    folder_list.append(element_path)
        return folder_list

    def reset_temp_folder(self) -> None:

        def ignore_existing_files(src: str, names: list[str]) -> list[str]:
            ignore_list = []

            for name in names:

                src_item = os.path.join(src, name)
                dst_item = os.path.join(self.temp_data_folder(), os.path.relpath(src_item, src))

                if os.path.exists(dst_item):
                    ignore_list.append(name)

            return ignore_list

        copytree(self.input_data_folder(), self.temp_data_folder(), dirs_exist_ok=True, ignore=ignore_existing_files)

    def delete_temp_folder(self) -> None:
        rmtree(self.temp_data_folder(), ignore_errors=True)

    def output_data_folder(self) -> str:
        folder = os.path.abspath(os.path.join(self.root_data_folder(), 'output'))
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder

    # -- FILES ---

    @classmethod
    def files(cls, folder: str, ext: str, subfolder: str | None = None) -> list[str]:
        file_list = list()
        for root, _, files in os.walk(folder):

            # logger.info("root: %s, folder: %s" % (root, subfolder))
            if subfolder is not None:
                if subfolder not in root:
                    continue

            for f in files:
                if f.endswith(ext) or (ext == ".*"):
                    file_list.append(os.path.join(root, f))
        return file_list

    def input_test_files(self, ext: str, subfolder: str | None = None) -> list[str]:
        return self.files(folder=self.input_data_folder(), ext=ext, subfolder=subfolder)

    def download_test_files(self, ext: str, subfolder: str | None = None) -> list[str]:
        return self.files(folder=self.download_data_folder(), ext=ext, subfolder=subfolder)

    def temp_test_files(self, ext: str, subfolder: str | None = None) -> list[str]:
        return self.files(folder=self.temp_data_folder(), ext=ext, subfolder=subfolder)

    def output_test_files(self, ext: str, subfolder: str | None = None) -> list[str]:
        return self.files(folder=self.output_data_folder(), ext=ext, subfolder=subfolder)
