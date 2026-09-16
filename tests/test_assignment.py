"""Check numerical identities and the coverage of the executed notebook."""
import copy
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
from numpy.testing import assert_allclose, assert_array_equal

ROOT = Path(__file__).resolve().parents[1]
SPEC = json.loads((ROOT / "src/examples.json").read_text())


def run_row(number):
    values = []
    namespace = {"print": lambda *items, **kwargs: values.append(copy.deepcopy(items[0] if len(items) == 1 else items))}
    exec(SPEC["setup"], namespace)
    values.clear()
    exec(SPEC["examples"][number - 1]["code"], namespace)
    return values, namespace


class AssignmentTests(unittest.TestCase):
    def test_all_rows_executed_in_ipython(self):
        notebook = json.loads((ROOT / "notebooks/assignment0.ipynb").read_text())
        cells = [c for c in notebook["cells"] if c["cell_type"] == "code"]
        rows = [c["metadata"]["row"] for c in cells if "row" in c["metadata"]]
        self.assertEqual(rows, list(range(1, 83)))
        for cell in cells:
            self.assertIsInstance(cell["execution_count"], int)
            self.assertFalse(any(o["output_type"] == "error" for o in cell["outputs"]))
        for task in ["3", "4"]:
            cell = next(c for c in cells if c["metadata"].get("task") == task)
            self.assertTrue(any("image/png" in o.get("data", {}) for o in cell["outputs"]))

    def test_arithmetic(self):
        expected = {20: [[11, 11], [24, 14]], 21: [[6, 3], [10, 8]],
                    22: [[1.5, 1/3], [0.4, 2]], 23: [[27, 1], [8, 64]]}
        for row, answer in expected.items():
            assert_allclose(run_row(row)[0][0], answer)

    def test_indexing_and_boundary(self):
        assert_array_equal(run_row(13)[0][0], [[10, 12], [28, 30], [37, 39]])
        assert_array_equal(run_row(14)[0][0].ravel(), np.arange(3, 22, 2))
        for result in run_row(27)[0]:
            assert_allclose(result, [[0.7, 0.5], [0.4, 0.8]])
        self.assertEqual(run_row(28)[0][0][0, 2], 0.5)
        self.assertEqual(run_row(29)[0][0][0, 2], 0.0)

    def test_copies_and_flattening(self):
        for row in (31, 32):
            values, ns = run_row(row)
            assert_array_equal(ns["x"], [[3, 1], [2, 4]])
            self.assertFalse(np.shares_memory(ns["x"], ns["y"]))
        values, _ = run_row(33)
        assert_array_equal(values[0], [3, 1, 2, 4])
        assert_array_equal(values[1], [3, 2, 1, 4])

    def test_inverse_and_pseudoinverse(self):
        assert_allclose(run_row(61)[0][0], [[0.4, -0.1], [-0.2, 0.3]])
        values, ns = run_row(62)
        inverse = values[0]
        assert_allclose(inverse, [[5/6, 1/3, -1/6], [-0.5, 0, 0.5]], atol=1e-14)
        assert_allclose(ns["a"] @ inverse @ ns["a"], ns["a"], atol=1e-14)
        self.assertEqual(run_row(63)[0][-1], 2)

    def test_linear_systems(self):
        values, ns = run_row(64)
        assert_allclose(ns["spd"] @ values[0], [1, 2, 3], atol=1e-13)
        coefficients, residual, rank, singular = values[1]
        assert_allclose(coefficients, [7/6, 0.5])
        assert_allclose(residual, 1/6)
        self.assertEqual(rank, 2)
        values, ns = run_row(65)
        assert_allclose(values[0] @ ns["a"], ns["b"], atol=1e-13)

    def test_factorizations(self):
        values, ns = run_row(66)
        u, s, v = values
        assert_allclose(u[:, :2] @ np.diag(s) @ v.T, ns["a"], atol=1e-13)
        assert_allclose(u.T @ u, np.eye(3), atol=1e-13)
        values, ns = run_row(67)
        assert_allclose(values[0].T @ values[0], ns["a"], atol=1e-13)
        values, ns = run_row(71)
        for q, r in [(values[0], values[1]), (values[2], values[3])]:
            assert_allclose(q @ r, ns["a"], atol=1e-13)
            assert_allclose(q.T @ q, np.eye(q.shape[1]), atol=1e-13)
        values, ns = run_row(72)
        assert_allclose(values[0] @ values[1] @ values[2], ns["a"], atol=1e-13)

    def test_eigenpairs_and_iterative_solver(self):
        values, ns = run_row(68)
        d, v = values
        assert_allclose(ns["a"] @ v, v * d, atol=1e-12)
        values, ns = run_row(69)
        d, v = values
        assert_allclose(ns["a"] @ v, (ns["b"] @ v) * d, atol=1e-12)
        values, ns = run_row(70)
        d, v = values
        assert_allclose(np.sort(d.real), [7, 11, 13], atol=1e-12)
        assert_allclose(ns["a"] @ v, v * d, atol=1e-12)
        values, ns = run_row(73)
        self.assertEqual(values[1], 0)
        assert_allclose(ns["a"] @ values[0], ns["b"], atol=1e-12)

    def test_fourier_transform_and_resampling(self):
        assert_allclose(run_row(74)[0][0], [10, -2+2j, -2, -2-2j])
        assert_allclose(run_row(75)[0][0], [1, 2, 3, 4], atol=1e-14)
        assert_allclose(run_row(80)[0][-1], [0, 1, 0, -1], atol=1e-14)

    def test_plot_data(self):
        import matplotlib
        matplotlib.use("Agg", force=True)
        import matplotlib.pyplot as plt
        with patch.object(plt, "show"):
            plt.close("all")
            exec((ROOT / "src/task3.py").read_text(), {})
            ax = plt.gca()
            assert_array_equal(ax.lines[0].get_xdata(), [1, 2, 3, 4])
            assert_array_equal(ax.lines[0].get_ydata(), [1, 2, 7, 14])
            self.assertEqual(ax.get_xlim(), (0.0, 6.0))
            self.assertEqual(ax.get_ylim(), (0.0, 20.0))
            plt.close("all")
            ns = {}
            exec((ROOT / "src/task4.py").read_text(), ns)
            self.assertTrue(np.all(np.abs(ns["amplitude"]) <= ns["envelope"] + 1e-14))
            self.assertEqual(len(ns["time"]), 801)
            self.assertAlmostEqual(ns["amplitude"][0], 1.0)
            self.assertAlmostEqual(ns["amplitude"][-1], np.exp(-2.8))
            plt.close("all")


if __name__ == "__main__":
    unittest.main()
