from matrix import Matrix
from matrix import square_matrix_multiply


elements = [1, 2, 3, 4, 5, 6]
ma = Matrix(elements,3,2)
print(ma.elements)
elements = [1, 0, 1, 0]
ma = Matrix(elements, 2, 2)
print(ma)
print(ma[0])
# print(ma[1, 1])
# print(ma[4])
# print(ma[2, 1])

m1 = Matrix([1, 0, 1, 0], 2, 2)
m2 = Matrix([0, 1, 0, 1], 2, 2)
m3 = m1 + m2
print(m3)
m4 = m3 + 1
print(m4)
m5 = Matrix([1, 1, 1, 1], 1, 4)
print(m4 + m5)

