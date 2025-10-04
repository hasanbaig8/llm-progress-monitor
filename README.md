- create a venv and install requirements
- progress_bar.ipynb has the relevant demos

Notes
-----

On Debian/Ubuntu systems the package `python3-apt` is provided by the
system package manager (apt) and should be installed via:

	sudo apt update && sudo apt install python3-apt

Do not pin distribution-specific builds of `python-apt` in `requirements.txt`.
Those are not available on PyPI and will cause `pip install -r requirements.txt`
to fail. This repository leaves `python-apt` out of the pip requirements and
documents the apt install step above.