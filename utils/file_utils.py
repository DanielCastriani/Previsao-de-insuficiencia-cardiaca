import os


def create_path_if_not_exists(path: str, *args, file_name: str = None):
    path = os.path.join(path, *args)

    if not os.path.exists(path):
        os.makedirs(path)

    if file_name:
        path = os.path.join(path, file_name)

    return path
