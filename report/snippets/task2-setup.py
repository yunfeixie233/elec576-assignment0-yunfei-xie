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

