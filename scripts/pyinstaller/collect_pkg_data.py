from PyInstaller.building.build_main import TOC


def collect_pkg_data(package, include_py_files=False, subdir=None):
    import os
    from PyInstaller.utils.hooks import get_package_paths, remove_prefix, PY_IGNORE_EXTENSIONS

    # Accept only strings as packages.
    if type(package) is not str:
        raise ValueError

    pkg_base, pkg_dir = get_package_paths(package)
    if subdir:
        pkg_dir = os.path.join(pkg_dir, subdir)
    # Walk through all file in the given package, looking for data files.
    data_toc = TOC()
    for dir_path, dir_names, files in os.walk(pkg_dir):

        copy_root_token = os.path.split(dir_path)[-1]
        copy_root = copy_root_token in ["support", "configdata"]
        # if copy_root:
        #     print("- %s" % dir_path)

        for f in files:
            extension = os.path.splitext(f)[1]
            if include_py_files or (extension not in PY_IGNORE_EXTENSIONS):
                source_file = os.path.join(dir_path, f)
                dest_folder = remove_prefix(dir_path, os.path.dirname(pkg_base) + os.sep)
                dest_file = os.path.join(dest_folder, f)
                data_toc.append((dest_file, source_file, 'DATA'))

                if copy_root:
                    source_file = os.path.join(dir_path, f)
                    root_path = os.path.join(os.path.dirname(pkg_base), "hyo2", "grids") + os.sep
                    dest_folder = remove_prefix(dir_path, root_path)
                    dest_file = os.path.join(dest_folder, f)
                    # print("%s -> %s" % (dest_file, source_file))
                    data_toc.append((dest_file, source_file, 'DATA'))

    return data_toc


grids_data = collect_pkg_data('hyo2.grids')

print("%s" % (grids_data,))
