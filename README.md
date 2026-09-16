# ELEC 576 / COMP 576 Assignment 0

Yunfei Xie (yx106), Fall 2026.

## Submission

- [Report PDF](report/ELEC576_Assignment_0_Yunfei_Xie.pdf)
- [Editable LaTeX source](report/ELEC576_Assignment_0_Yunfei_Xie.tex)
- [Assignment questions](questions/ELEC576_Assignment_0-1.pdf)
- [Executed notebook](notebooks/assignment0.ipynb)

The report covers all six tasks, including code and output for all 82 table rows, plus optional NumPy practice. Submit the report PDF on Canvas.

## Run the code

The recorded results use Anaconda Distribution 2026.07-1 and Python 3.14.6. On the original Mac:

~~~sh
source ~/anaconda3/bin/activate
python run_assignment.py
python -m unittest discover -s tests -v
~~~

On another machine, first create and activate the supplied environment:

~~~sh
conda env create -f environment.yml
conda activate elec576-assignment0
~~~

Open this folder in Visual Studio Code or JupyterLab and select that environment. The runner replaces the generated notebook, results, and figures. The two captured TypeError messages come from invalid calls in the NumPy table; working calls follow them.

Python examples are in src/, captured outputs in results/, and plots in figures/. The report keeps its own copies of the submitted code snippets and figures.

## Build the report

With LaTeX installed:

~~~sh
cd report
latexmk -pdf -interaction=nonstopmode -halt-on-error ELEC576_Assignment_0_Yunfei_Xie.tex
~~~

## Sources

- [NumPy table](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html#linear-algebra-equivalents)
- [SciPy documentation](https://docs.scipy.org/doc/scipy/reference/)
- [Matplotlib tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [Stanford NumPy tutorial](https://cs231n.github.io/python-numpy-tutorial/)
- [Reference assignment](https://github.com/ZengChen94/Introduction-to-Deep-Learning/tree/master/Assignment%200), used to compare task coverage and outputs.
