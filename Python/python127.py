class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"(x={self.x}, y={self.y})"
a=point(1,2)
print(a)