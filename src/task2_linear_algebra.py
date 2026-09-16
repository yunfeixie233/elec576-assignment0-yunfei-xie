"""Run every row of the NumPy linear algebra equivalents table."""
import numpy as np
import scipy
import scipy.linalg
from scipy import linalg, signal
from scipy.sparse.linalg import cg, eigs
from numpy.random import default_rng
np.set_printoptions(precision=6, suppress=True, linewidth=76, threshold=10000)
small = np.array([[3., 1.], [2., 4.]])
other = np.array([[2., 3.], [5., 2.]])
scan = np.arange(1., 46.).reshape(5, 9)
threshold = np.array([[0.2, 0.7, 0.5], [0.9, 0.4, 0.8]])
complex_matrix = np.array([[1+2j, 3-1j], [2j, 4+0j]])
spd = np.array([[6., 2., 1.], [2., 5., 2.], [1., 2., 4.]])
rect = np.array([[1., 0.], [1., 1.], [1., 2.]])
for name in ['small', 'other', 'scan', 'threshold', 'complex_matrix', 'spd', 'rect']:
    print(name + ' =')
    print(globals()[name])


# 2.1 Dimensions
print('2.1 Dimensions')
a = small.copy()
print(np.ndim(a))
print(a.ndim)


# 2.2 Number of elements
print('2.2 Number of elements')
a = small.copy()
print(np.size(a))
print(a.size)


# 2.3 Array shape
print('2.3 Array shape')
a = small.copy()
print(np.shape(a))
print(a.shape)


# 2.4 Length of one axis
print('2.4 Length of one axis')
a = scan.copy()
n = 2
print(a.shape[n-1])


# 2.5 Create an array
print('2.5 Create an array')
a = np.array([[1., 2., 3.], [4., 5., 6.]])
print(a)


# 2.6 Assemble blocks
print('2.6 Assemble blocks')
a, b = small.copy(), other.copy()
c, d = np.eye(2), np.zeros((2, 2))
print(np.block([[a, b], [c, d]]))


# 2.7 Last vector entry
print('2.7 Last vector entry')
a = np.array([4., 9., 16.])
print(a[-1])


# 2.8 One matrix entry
print('2.8 One matrix entry')
a = scan.copy()
print(a[1, 4])


# 2.9 One row
print('2.9 One row')
a = scan.copy()
print(a[1])
print(a[1, :])


# 2.10 First five rows
print('2.10 First five rows')
a = scan.copy()
print(a[0:5])
print(a[:5])
print(a[0:5, :])


# 2.11 Last five rows
print('2.11 Last five rows')
a = np.arange(1., 15.).reshape(7, 2)
print(a)
print(a[-5:])


# 2.12 A rectangular slice
print('2.12 A rectangular slice')
a = scan.copy()
print(a[0:3, 4:9])


# 2.13 Selected rows and columns
print('2.13 Selected rows and columns')
a = scan.copy()
print(a[np.ix_([1, 3, 4], [0, 2])])


# 2.14 Rows 3 through 21 with a stride of two
print('2.14 Rows 3 through 21 with a stride of two')
a = np.arange(1., 22.).reshape(21, 1)
print(a[2:21:2, :])


# 2.15 Every other row
print('2.15 Every other row')
a = scan.copy()
print(a[::2, :])


# 2.16 Reverse the rows
print('2.16 Reverse the rows')
a = small.copy()
print(a[::-1, :])


# 2.17 Append the first row
print('2.17 Append the first row')
a = small.copy()
print(a[np.r_[:len(a), 0]])


# 2.18 Transpose
print('2.18 Transpose')
a = small.copy()
print(a.transpose())
print(a.T)


# 2.19 Conjugate transpose
print('2.19 Conjugate transpose')
a = complex_matrix.copy()
print(a.conj().transpose())
print(a.conj().T)


# 2.20 Matrix multiplication
print('2.20 Matrix multiplication')
a, b = small.copy(), other.copy()
print(a @ b)


# 2.21 Elementwise multiplication
print('2.21 Elementwise multiplication')
a, b = small.copy(), other.copy()
print(a * b)


# 2.22 Elementwise division
print('2.22 Elementwise division')
a, b = small.copy(), other.copy()
print(a / b)


# 2.23 Elementwise powers
print('2.23 Elementwise powers')
a = small.copy()
print(a**3)


# 2.24 A Boolean comparison
print('2.24 A Boolean comparison')
a = threshold.copy()
print(a > 0.5)


# 2.25 Indices satisfying a condition
print('2.25 Indices satisfying a condition')
a = threshold.copy()
print(np.nonzero(a > 0.5))


# 2.26 Select columns using index positions
print('2.26 Select columns using index positions')
a = threshold.copy()
v = np.array([0.3, 0.9, 0.7])
print(a[:, np.nonzero(v > 0.5)[0]])


# 2.27 Select columns using a Boolean mask
print('2.27 Select columns using a Boolean mask')
a = threshold.copy()
v = np.array([0.3, 0.9, 0.7])
print(a[:, v.T > 0.5])
v = v.reshape(-1, 1)
print(a[:, v.ravel() > 0.5])


# 2.28 Replace entries below a threshold
print('2.28 Replace entries below a threshold')
a = threshold.copy()
a[a < 0.5] = 0
print(a)


# 2.29 Multiply by a strict Boolean mask
print('2.29 Multiply by a strict Boolean mask')
a = threshold.copy()
print(a * (a > 0.5))


# 2.30 Fill an array
print('2.30 Fill an array')
a = small.copy()
a[:] = 3
print(a)


# 2.31 Copy an array
print('2.31 Copy an array')
x = small.copy()
y = x.copy()
y[0, 0] = 99
print(y)
print(x)


# 2.32 Copy a row
print('2.32 Copy a row')
x = small.copy()
y = x[1, :].copy()
y[0] = 99
print(y)
print(x)


# 2.33 Flatten an array
print('2.33 Flatten an array')
x = small.copy()
y = x.flatten()
print(y)
print(x.flatten("F"))


# 2.34 The values 1 through 10
print('2.34 The values 1 through 10')
print(np.arange(1., 11.))
print(np.r_[1.:11.])
print(np.r_[1:10:10j])


# 2.35 The values 0 through 9
print('2.35 The values 0 through 9')
print(np.arange(10.))
print(np.r_[:10.])
print(np.r_[:9:10j])


# 2.36 A column vector
print('2.36 A column vector')
print(np.arange(1., 11.)[:, np.newaxis])


# 2.37 A zero matrix
print('2.37 A zero matrix')
print(np.zeros((3, 4)))


# 2.38 A three-dimensional zero array
print('2.38 A three-dimensional zero array')
print(np.zeros((3, 4, 5)))


# 2.39 An array of ones
print('2.39 An array of ones')
print(np.ones((3, 4)))


# 2.40 An identity matrix
print('2.40 An identity matrix')
print(np.eye(3))


# 2.41 Read a diagonal
print('2.41 Read a diagonal')
a = small.copy()
print(np.diag(a))


# 2.42 Construct a diagonal matrix
print('2.42 Construct a diagonal matrix')
v = np.array([2., 5., 8.])
print(np.diag(v, 0))


# 2.43 Random values with a fixed seed
print('2.43 Random values with a fixed seed')
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


# 2.44 Evenly spaced values
print('2.44 Evenly spaced values')
print(np.linspace(1, 3, 4))


# 2.45 Dense coordinate grids
print('2.45 Dense coordinate grids')
print(np.mgrid[0:9., 0:6.])
print(np.meshgrid(np.r_[0:9.], np.r_[0:6.]))


# 2.46 Open coordinate grids
print('2.46 Open coordinate grids')
print(np.ogrid[0:9., 0:6.])
print(np.ix_(np.r_[0:9.], np.r_[0:6.]))


# 2.47 An irregular dense grid
print('2.47 An irregular dense grid')
print(np.meshgrid([1, 2, 4], [2, 4, 5]))


# 2.48 An irregular open grid
print('2.48 An irregular open grid')
print(np.ix_([1, 2, 4], [2, 4, 5]))


# 2.49 Repeat a matrix
print('2.49 Repeat a matrix')
a = small.copy()
m, n = 2, 3
print(np.tile(a, (m, n)))


# 2.50 Join columns
print('2.50 Join columns')
a, b = small.copy(), other.copy()
print(np.concatenate((a, b), 1))
print(np.hstack((a, b)))
print(np.column_stack((a, b)))
print(np.c_[a, b])


# 2.51 Join rows
print('2.51 Join rows')
a, b = small.copy(), other.copy()
print(np.concatenate((a, b)))
print(np.vstack((a, b)))
print(np.r_[a, b])


# 2.52 Maximum over all entries
print('2.52 Maximum over all entries')
a = small.copy()
print(a.max())
print(np.nanmax(a))
a[0, 0] = np.nan
print(a.max())
print(np.nanmax(a))


# 2.53 Maximum in each column
print('2.53 Maximum in each column')
a = small.copy()
print(a.max(0))


# 2.54 Maximum in each row
print('2.54 Maximum in each row')
a = small.copy()
print(a.max(1))


# 2.55 Elementwise maximum
print('2.55 Elementwise maximum')
a, b = small.copy(), other.copy()
print(np.maximum(a, b))


# 2.56 Euclidean norm
print('2.56 Euclidean norm')
v = np.array([3., 4.])
print(np.sqrt(v @ v))
print(np.linalg.norm(v))


# 2.57 Logical AND
print('2.57 Logical AND')
a = np.array([0, 2, 3, 0])
b = np.array([1, 1, 0, 0])
print(np.logical_and(a, b))


# 2.58 Logical OR
print('2.58 Logical OR')
a = np.array([0, 2, 3, 0])
b = np.array([1, 1, 0, 0])
print(np.logical_or(a, b))


# 2.59 Bitwise AND
print('2.59 Bitwise AND')
a = np.array([0, 2, 3, 0])
b = np.array([1, 1, 0, 0])
print(a & b)


# 2.60 Bitwise OR
print('2.60 Bitwise OR')
a = np.array([0, 2, 3, 0])
b = np.array([1, 1, 0, 0])
print(a | b)


# 2.61 Matrix inverse
print('2.61 Matrix inverse')
a = small.copy()
print(linalg.inv(a))


# 2.62 Pseudoinverse
print('2.62 Pseudoinverse')
a = rect.copy()
print(linalg.pinv(a))


# 2.63 Matrix rank
print('2.63 Matrix rank')
a = np.array([[1., 2., 3.], [2., 4., 6.], [1., 1., 1.]])
print(a)
print(np.linalg.matrix_rank(a))


# 2.64 Square and rectangular linear systems
print('2.64 Square and rectangular linear systems')
a = spd.copy()
b = np.array([1., 2., 3.])
print(linalg.solve(a, b))
a = rect.copy()
b = np.array([1., 2., 2.])
print(linalg.lstsq(a, b))


# 2.65 A system with the unknown on the left
print('2.65 A system with the unknown on the left')
a = small.copy()
b = np.array([[1., 2.], [4., 3.]])
x = linalg.solve(a.T, b.T).T
print(x)
print(x @ a)


# 2.66 Singular value decomposition
print('2.66 Singular value decomposition')
a = rect.copy()
U, S, Vh = linalg.svd(a)
V = Vh.T
print(U)
print(S)
print(V)


# 2.67 Cholesky factorization
print('2.67 Cholesky factorization')
a = spd.copy()
print(linalg.cholesky(a))


# 2.68 Eigenvalues and eigenvectors
print('2.68 Eigenvalues and eigenvectors')
a = spd.copy()
D, V = linalg.eig(a)
print(D)
print(V)


# 2.69 Generalized eigenvalues
print('2.69 Generalized eigenvalues')
a = spd.copy()
b = np.diag([1., 2., 3.])
D, V = linalg.eig(a, b)
print(D)
print(V)


# 2.70 Three eigenpairs of a larger matrix
print('2.70 Three eigenpairs of a larger matrix')
a = np.diag([2., 3., 5., 7., 11., 13.])
D, V = eigs(a, k=3, v0=np.ones(6))
print(D)
print(V)


# 2.71 QR factorization
print('2.71 QR factorization')
a = rect.copy()
Q, R = linalg.qr(a)
print(Q)
print(R)
Q, R = linalg.qr(a, mode="economic")
print(Q)
print(R)


# 2.72 LU factorization
print('2.72 LU factorization')
a = small.copy()
P, L, U = linalg.lu(a)
print(P)
print(L)
print(U)
print(P @ L @ U)


# 2.73 Conjugate gradients
print('2.73 Conjugate gradients')
a = spd.copy()
b = np.array([1., 2., 3.])
x, info = cg(a, b, rtol=1e-12, atol=0.0)
print(x)
print(info)


# 2.74 Discrete Fourier transform
print('2.74 Discrete Fourier transform')
a = np.array([1., 2., 3., 4.])
print(np.fft.fft(a))


# 2.75 Inverse Fourier transform
print('2.75 Inverse Fourier transform')
a = np.fft.fft(np.array([1., 2., 3., 4.]))
print(np.fft.ifft(a))


# 2.76 Default sorting and column sorting
print('2.76 Default sorting and column sorting')
a = small.copy()
print(np.sort(a))
a.sort(axis=0)
print(a)


# 2.77 Sort each row
print('2.77 Sort each row')
a = small.copy()
print(np.sort(a, axis=1))
a.sort(axis=1)
print(a)


# 2.78 Sort rows by their first entry
print('2.78 Sort rows by their first entry')
a = np.array([[3., 1.], [1., 4.], [2., 0.]])
I = np.argsort(a[:, 0])
b = a[I, :]
print(I)
print(b)


# 2.79 Linear regression
print('2.79 Linear regression')
Z = rect.copy()
y = np.array([1., 2., 2.])
x = linalg.lstsq(Z, y)
print(x)
print(Z @ x[0])


# 2.80 Fourier resampling
print('2.80 Fourier resampling')
t = np.arange(12.) / 12
x = np.sin(2 * np.pi * t)
q = 3
try:
    signal.resample(x, np.ceil(len(x)/q))
except TypeError as error:
    print(type(error).__name__ + ": " + str(error))
print(signal.resample(x, int(np.ceil(len(x)/q))))


# 2.81 Unique values
print('2.81 Unique values')
a = np.array([4, 1, 4, 2, 1, 3])
print(np.unique(a))


# 2.82 Remove axes of length one
print('2.82 Remove axes of length one')
a = np.array([[[2., 4., 6.]]])
print(a.shape)
print(a.squeeze())
print(a.squeeze().shape)
