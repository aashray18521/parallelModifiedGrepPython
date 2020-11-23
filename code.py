import multiprocessing
import os
import time

rootdir = "."
keyword = "blah"

batch_size = 1

def try_multiple_operations(file_path):
    try:
        with open(file_path, "rb") as f:  # open the file for reading
            for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                try:
                    line = line.decode("utf-8")  # try to decode the contents to utf-8
                except ValueError:  # decoding failed, skip the line
                    continue
                if keyword in line:  # if the keyword exists on the current line...
                    print(file_path)  # print the file path
    except (IOError, OSError):  # ignore read and permission errors
        pass

def walk_dirs(directory, batch_size):
    walk_dirs_generator = os.walk(directory)
    for dirname, subdirectories, filenames in walk_dirs_generator:
        for i in range(0, len(filenames), batch_size):
            the_queue.put(os.path.join(dirname, filenames[i]))

the_queue = multiprocessing.Queue()

walk_dirs(rootdir, batch_size)

def worker_main(queue):
    while True:
        item = queue.get(True)
        try_multiple_operations(item)

the_pool = multiprocessing.Pool(3, worker_main,(the_queue,))