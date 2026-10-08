# Create a custom context manager using a class
# that opens a file in write mode in the __enter__ method,
# writes a line to the file, closes the file in the __exit__ method,
# and properly prints or logs any exception information received in __exit__.

class a:

    def __init__(self,fn,mode):
        self.fn = fn
        self.mode = mode

    def __enter__(self):

        self.fp = open(self.fn,self.mode)
        self.fp.write("Hi")
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.fp.close()
        print(exc_type)
        print(exc_val)
        print(exc_tb)

with a("Test3.txt","w") as fp:

    pass

