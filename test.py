class A:
    def __init__(self, num):
        self.num = num

class Singleton:
    def __init__(self, obj):
        self.obj = obj

sing = Singleton(A(5))