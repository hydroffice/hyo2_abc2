import os
import shutil


def remove_pycache(folder: str):

    print("folder path: %s" % folder)

    for dir_path, dir_names, files in os.walk(folder):

        for d in dir_names:

            if d == "__pycache__":

                full_path = os.path.join(dir_path, d)
                print(full_path)
                shutil.rmtree(full_path)


folder_path = r"C:\code\hyo2\abc\hyo2_huddl"

remove_pycache(folder=folder_path)
