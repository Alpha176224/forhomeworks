import math

class Vector:
    def __init__(self, *components):
        self.components = list(components)
    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector(*[x + y for x, y in zip(self.components, other.components)])
    
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        return Vector(*[x - y for x, y in zip(self.components, other.components)])
    
    def __mul__(self, scalar):
        return Vector(*[x * scalar for x in self.components])
    
    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        return sum(x * y for x, y in zip(self.components, other.components))
    
    def magnitude(self):
        return math.sqrt(sum(x ** 2 for x in self.components))
    
    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"
    
    def __eq__(self, other):
        return self.components == other.components
