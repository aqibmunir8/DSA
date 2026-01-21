import ctypes

class Meralist:
    def __init__(self):
        self.size = 1
        self.n =0
        # Create a C type array with size = self.size
        self.A = self.__make_array(self.size)
    
    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def append(self, item):
        if self.n == self.size:
            #resize
            pass
        # Append
        self.A[self.n] = item
        self.n += 1

    def __str__(self):
        result = ''
        for i in range(self.n):
            result += str(self.A[i]) + ", "
        return f"[{result}]"
    
L = Meralist()
L.append("Hello World")
L.append("Hello World")
print(L)