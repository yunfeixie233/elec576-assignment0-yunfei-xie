# ELEC 576 / COMP 576 Assignment 0

Yunfei Xie (yx106), Fall 2026.

The notebook contains the results for all 82 rows of NumPy's linear algebra equivalents table, the assigned Matplotlib plot, an original damped-oscillation plot, and optional NumPy practice.

## Files

- `notebooks/assignment0.ipynb`: executed notebook, including both figures.
- `src/task2_linear_algebra.py`: runnable Python examples for all table rows.
- `src/task3.py` and `src/task4.py`: plotting scripts.
- `src/optional_numpy.py`: broadcasting, indexing, and copy examples.
- `src/examples.json`: inputs and explanations used to build the notebook.
- `results/`: captured IPython output and Anaconda environment information.
- `figures/`: figures extracted from the executed notebook.
- `tests/test_assignment.py`: numerical checks and notebook coverage checks.

## Run

The recorded results use Anaconda Distribution 2026.07-1, Python 3.14.6, NumPy 2.4.6, SciPy 1.18.0, and Matplotlib 3.11.0.

To use the Anaconda installation on this Mac, run:

```sh
source ~/anaconda3/bin/activate
python run_assignment.py
python -m unittest discover -s tests -v
```

To create a separate environment on another machine, run:

```sh
conda env create -f environment.yml
conda activate elec576-assignment0
python run_assignment.py
python -m unittest discover -s tests -v
```

Open this folder in Visual Studio Code and select the Python interpreter from the activated environment. The `.vscode/settings.json` file points to the local Anaconda base interpreter by default. The executed notebook can also be opened in JupyterLab.

`run_assignment.py` starts an IPython kernel, executes the notebook, and saves its outputs. It replaces the generated notebook, transcript, and figures when run again. The `conda info` result will describe the environment used for that run.

To run only the linear algebra examples in IPython, use:

```sh
ipython src/task2_linear_algebra.py
```

The two displayed `TypeError` messages are intentional demonstrations of outdated calls in the table. Each is followed by a working version. Other differences involving column masks, sorting axes, QR dimensions, and resampling are explained beside the corresponding examples.

## Sources

- Course handout: ELEC 576 / COMP 576, Fall 2026, Assignment 0.
- [NumPy for MATLAB users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html#linear-algebra-equivalents): required command list.
- [SciPy reference](https://docs.scipy.org/doc/scipy/reference/): factorization, solver, and resampling behavior.
- [Matplotlib pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html): plotting API.
- [Stanford NumPy tutorial](https://cs231n.github.io/python-numpy-tutorial/): optional practice topics.
- [Chen Zeng's Assignment 0](https://github.com/ZengChen94/Introduction-to-Deep-Learning/tree/master/Assignment%200): used to check task coverage and outputs. The examples and custom figure in this project were written independently.
