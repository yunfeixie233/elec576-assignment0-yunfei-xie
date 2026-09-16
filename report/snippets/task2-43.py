from numpy.random import default_rng
rng = default_rng(42)
print(rng.random((3, 4)))
from numpy import random
random.seed(42)
try:
    random.rand((3, 4))
except TypeError as error:
    print(type(error).__name__ + ": " + str(error))
print(random.rand(3, 4))

