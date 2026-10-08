# Create a custom context manager using @contextmanager from the contextlib
# module that opens a file, yields the file object,
# and ensures the file is closed even if an exception occurs

from contextlib import contextmanager
@contextmanager
def a(file,mode):

    f = open(file, mode)

    try:

        yield f
    finally:
        f.close()

with a("test3.txt","w+") as fp :

    fp.write("Hi my name is deepak")
    fp.seek(0)

    print(fp.read())