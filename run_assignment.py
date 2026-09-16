"""Execute the assignment in an IPython kernel and save its results."""
from pathlib import Path
import base64
import json
import os
import sys
import tempfile

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parent


def execute():
    examples = json.loads((ROOT / "src/examples.json").read_text())
    cells = []

    def markdown(text):
        cells.append(nbformat.v4.new_markdown_cell(text))

    def code(text, **metadata):
        cells.append(nbformat.v4.new_code_cell(text, metadata=metadata))

    markdown("# ELEC 576 Assignment 0\n\nYunfei Xie (yx106)\n\n"
             "Python, NumPy, SciPy, and Matplotlib exercises.")
    markdown("## Task 1: Anaconda environment")
    code("import subprocess\n"
         "result = subprocess.run(['conda', 'info'], capture_output=True, text=True, check=True)\n"
         "print(result.stdout, end='')", task="1")
    markdown("## Task 2: Linear algebra equivalents\n\n"
             "The numbered examples follow all 82 rows of the "
             "[NumPy table](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html#linear-algebra-equivalents). "
             "The matrices and supporting examples are defined below.")
    code(examples["setup"], task="2", role="setup")
    for item in examples["examples"]:
        heading = f"### 2.{item['row']} {item['title']}"
        if item["note"]:
            heading += "\n\n" + item["note"]
        markdown(heading)
        code(item["code"], task="2", row=item["row"])
    markdown("## Optional NumPy practice\n\n"
             "These examples use broadcasting, reductions, Boolean indexing, and slicing from the "
             "[Stanford tutorial](https://cs231n.github.io/python-numpy-tutorial/).")
    code((ROOT / "src/optional_numpy.py").read_text(), task="optional")
    code("%matplotlib inline\n"
         "from matplotlib_inline.backend_inline import set_matplotlib_formats\n"
         "set_matplotlib_formats('png')\n"
         "import matplotlib.pyplot as plt\n"
         "plt.rcParams['figure.dpi'] = 140", role="plot_setup")
    markdown("## Task 3: Assigned plot")
    code((ROOT / "src/task3.py").read_text(), task="3")
    markdown("## Task 4: Damped oscillation\n\n"
             "The signal is exp(-0.7t) cos(2 pi 1.5t). The dashed curves show its positive and negative envelopes.")
    code((ROOT / "src/task4.py").read_text(), task="4")
    markdown("## Task 5: Version control account\n\n"
             "GitHub account: [yunfeixie233](https://github.com/yunfeixie233).")
    markdown("## Task 6: IDE project\n\n"
             "The project is configured for Visual Studio Code.\n\n"
             "Repository: https://github.com/yunfeixie233/elec576-assignment0-yunfei-xie")
    notebook = nbformat.v4.new_notebook(cells=cells)
    notebook.metadata["kernelspec"] = {"name": "assignment-python", "display_name": "Python (ELEC 576)", "language": "python"}
    notebook.metadata["language_info"] = {"name": "python", "version": sys.version.split()[0]}
    with tempfile.TemporaryDirectory(prefix="elec576-kernel-") as temp:
        kernel = Path(temp) / "kernels" / "assignment-python"
        kernel.mkdir(parents=True)
        (kernel / "kernel.json").write_text(json.dumps({
            "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            "display_name": "Python (ELEC 576)", "language": "python"}))
        old = os.environ.get("JUPYTER_PATH")
        os.environ["JUPYTER_PATH"] = temp + (os.pathsep + old if old else "")
        try:
            NotebookClient(notebook, timeout=120, kernel_name="assignment-python",
                           resources={"metadata": {"path": str(ROOT)}},
                           allow_errors=False).execute()
        finally:
            if old is None:
                os.environ.pop("JUPYTER_PATH", None)
            else:
                os.environ["JUPYTER_PATH"] = old
    (ROOT / "notebooks").mkdir(exist_ok=True)
    (ROOT / "results").mkdir(exist_ok=True)
    (ROOT / "figures").mkdir(exist_ok=True)
    notebook.metadata["kernelspec"] = {
        "name": "python3", "display_name": "Python 3 (ipykernel)", "language": "python"
    }
    nbformat.write(notebook, ROOT / "notebooks/assignment0.ipynb")
    records = []
    for cell in notebook.cells:
        if cell.cell_type != "code":
            continue
        output = ""
        for entry in cell.get("outputs", []):
            if entry.output_type == "stream":
                output += entry.text
            elif entry.output_type in {"execute_result", "display_data"}:
                data = entry.get("data", {})
                output += data.get("text/plain", "") + ("\n" if "text/plain" in data else "")
                if "image/png" in data and cell.metadata.get("task") in {"3", "4"}:
                    (ROOT / "figures" / f"task{cell.metadata.task}.png").write_bytes(base64.b64decode(data["image/png"]))
            elif entry.output_type == "error":
                raise RuntimeError(entry.evalue)
        records.append({"execution_count": cell.execution_count,
                        "metadata": dict(cell.metadata), "code": cell.source, "output": output})
    (ROOT / "results/execution.json").write_text(json.dumps(records, indent=2) + "\n")
    conda = next(r["output"] for r in records if r["metadata"].get("task") == "1")
    (ROOT / "results/conda-info.txt").write_text(conda)
    transcript = []
    for r in records:
        transcript += [f"In [{r['execution_count']}]:", r["code"], r["output"]]
    (ROOT / "results/ipython-transcript.txt").write_text("\n".join(transcript))
    print(f"Executed {len(records)} code cells; all 82 table rows completed.")
    print("Saved notebooks/assignment0.ipynb, results/, and figures/.")


if __name__ == "__main__":
    execute()
