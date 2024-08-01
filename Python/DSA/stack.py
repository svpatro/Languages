class Stack:
    def __init__(self):
        self.topOfStack = 0
        self.__index = []

    def __len__(self):
        return len(self.__index)

    def push(self, val):
        self.__index.insert(0, val)
        self.topOfStack = self.topOfStack + 1

    def peak(self):
        if len(self) == 0:
            print("No items in array! Cannot peak.")
        else:
            return self.__index[0]

    def pop(self):
        if len(self) == 0:
            print("No items in array! Cannot pop.")
        else:
            val = self.__index.pop()
            self.topOfStack = self.topOfStack - 1
            return val
            

