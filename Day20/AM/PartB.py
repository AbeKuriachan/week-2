class Vector:
    def __init__(self, values):
        if not isinstance(values, tuple):
            raise TypeError("Input must be a tuple")

        for v in values:
            if not isinstance(v, (int, float)):
                raise TypeError("All elements must be numbers")

        self.values = values


    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector with Vector")

        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be of same length")

        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])

        return Vector(tuple(result))


    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract Vector with Vector")

        if len(self.values) != len(other.values):
            raise ValueError("Vectors must be of same length")

        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] - other.values[i])

        return Vector(tuple(result))

    # Scalar Multiplication
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply by a scalar (int/float)")

        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] * scalar)

        return Vector(tuple(result))


    def __rmul__(self, scalar):
        return self.__mul__(scalar)


    def __repr__(self):
        return f"Vector{self.values}"


v1 = Vector((1, 2, 3))
v2 = Vector((4, 5, 6))


print(v1 + v2)


print(v1 - v2)


print(v1 * 3)


print(2 * v2)