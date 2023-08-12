a = 0
b = 1
print(f'a = {a}, b = {b}.')
a_array = [1, 2, 3, 4]
print(f'a-size = {len(a_array)}')

class MCL:
    def __init__(self, x=0.0):
        self.a_array = []
        self.a = 0
        self.b = 1

    def print(self):
        print(f'a = {self.a}, b = {self.b}.')
        print(f'a-size = {len(self.a_array)}')

x = 0.0
mcl = MCL(x)
mcl.print()
