"""
Lightweight CLI to run the real-time eSSVI notebook pipeline from Python.
This wrapper simply executes the notebook (if present) or raises a helpful message.
"""
from pathlib import Path
import sys
import subprocess

def main():
    nb = Path(__file__).resolve().parents[2] / "notebooks" / "real_time_fit.ipynb"
    if not nb.exists():
        print("Notebook not found at:", nb)
        print("Run the pipeline by opening notebooks/real_time_fit.ipynb in Jupyter,")
        print("or move your notebook there.")
        sys.exit(1)
    try:
        # Execute notebook to produce plots and outputs (requires jupyter)
        subprocess.check_call([sys.executable, "-m", "jupyter", "nbconvert",
                               "--to", "notebook", "--execute",
                               "--inplace", str(nb)])
        print("Notebook executed successfully.")
    except Exception as e:
        print("Failed to run notebook via nbconvert:", e)
        sys.exit(2)

if __name__ == "__main__":
    main()
