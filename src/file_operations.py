import logging
import os
import os.path
import errno

logger = logging.getLogger('fidelity_parser')

EXAMPLES_DIRECTORY = 'examples'


# Really not a fan of this, but it works
# Reference https://stackoverflow.com/questions/23793987/write-a-file-to-a-directory-that-doesnt-exist
def ensure_directory_exists(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def write_content_to_file(file_content, file_dir, file_path):
    ensure_directory_exists(file_dir)
    f = open(file_path, "wb")
    f.write(file_content)
    f.close()


def update_file_create_time(file_path, date):
    os.utime(file_path, (date.timestamp(), date.timestamp()))


def read_from_file(file_path):
    f = open(file_path)
    contents = f.read()
    f.close()
    return contents
