import os
import sys
from PyInstaller.building.build_main import TOC
from PyInstaller.utils.hooks import remove_prefix, PY_IGNORE_EXTENSIONS


def collect_folder_data(folder: str, visit_sub_folders=True, include_py_files=False,):

    interpreter_path = os.path.dirname(sys.executable)
    folder_path = os.path.join(interpreter_path, folder)
    print("folder path: %s" % folder_path)
    # Walk through all file in the given package, looking for data files.
    data_toc = TOC()
    for dir_path, dir_names, files in os.walk(folder_path):

        for f in files:
            extension = os.path.splitext(f)[1]
            # print(f)
            if not include_py_files and (extension in PY_IGNORE_EXTENSIONS):
                continue

            source_file = os.path.join(dir_path, f)
            dest_folder = remove_prefix(dir_path, interpreter_path + os.sep)
            dest_file = os.path.join(dest_folder, f)
            data_toc.append((dest_file, source_file, 'DATA'))

        if not visit_sub_folders:
            break

    return data_toc


grids_data = collect_folder_data(folder=os.path.join("Library", "share"),
                                 visit_sub_folders=False, include_py_files=False)

print("%s" % (grids_data,))
