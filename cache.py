import os
from file import write_file
from loader import load_page


cache_folder = "cache"


def get_from_cache_or_load(file_path, url):
    cache_file_path = os.path.join(cache_folder, file_path)

    if os.path.exists(cache_file_path):
        with open(cache_file_path, 'rb') as file:
            page_content = file.read()
    else:
        # Ensure the directory exists before writing the file
        dirs = os.path.dirname(cache_file_path)
        if not os.path.exists(dirs):
            os.makedirs(dirs)

        page_content = load_page(url)
        write_file(cache_file_path, page_content)

    return page_content