# import os
# import concurrent
# import concurrent.futures
# import queue

import multiprocessing
import os
import time

# Your root directory path
rootdir = "."
keyword = "test"

#Your batch size
batch_size = 1

# executor = concurrent.futures.ProcessPoolExecutor(10)

# q = []

def try_multiple_operations(file_path):
    # for item in items:
    #     try:
    #         api.my_operation(item)
    #     except:
    #         print('error with item')
    # print(file_path)
    # for file_path in file_name_batch:
        # Do some processing on the batch now
        # print (file_path)
    try:
        # print(file_path)
        with open(file_path, "rb") as f:  # open the file for reading
            # read the file line by line
            # global keyword
            # print(file_path)
            for line in f:  # use: for i, line in enumerate(f) if you need line numbers
                try:
                    line = line.decode("utf-8")  # try to decode the contents to utf-8
                    # print(line)
                except ValueError:  # decoding failed, skip the line
                    continue
                if keyword in line:  # if the keyword exists on the current line...
                    print(file_path)  # print the file path
                    # break  # no need to iterate over the rest of the file
    except (IOError, OSError):  # ignore read and permission errors
        pass

def walk_dirs(directory, batch_size):
    walk_dirs_generator = os.walk(directory)
    for dirname, subdirectories, filenames in walk_dirs_generator:
        for i in range(0, len(filenames), batch_size):
            # slice the filenames list 0-31, 32-64 and so on
            # yield [os.path.join(dirname, filename) for filename in filenames[i:i+batch_size]]
            the_queue.put(os.path.join(dirname, filenames[i]))



# Finally iterate over the walk_dirs function which itself returns a generator
# for file_name_batch in walk_dirs(rootdir, batch_size):
# walk_dirs(rootdir, batch_size)
# while(q):
#     # futures = executor.submit(try_multiple_operations, q.pop())
#     # concurrent.futures.wait(futures)
#     result = executor.map(try_multiple_operations, q.pop())

# q1.push(result())




the_queue = multiprocessing.Queue()

walk_dirs(rootdir, batch_size)

def worker_main(queue):
    # print(os.getpid(),"working")
    while True:
        item = queue.get(True)
        # print(os.getpid(), "got", item)
        try_multiple_operations(item)
        # time.sleep(1) # simulate a "long" operation

the_pool = multiprocessing.Pool(3, worker_main,(the_queue,))

# for i in range(5):
#     the_queue.put("hello")
#     the_queue.put("world")


# time.sleep(10)
