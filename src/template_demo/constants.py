"""Static configuration of template-demo."""

from pathlib import Path

# Configuration required by oe-python-template
API_VERSIONS: dict[str, str] = {
    "v1": "1.0.0",
    "v2": "2.0.0",
}
MODULES_TO_INSTRUMENT: list[str] = ["template_demo.hello"]
NOTEBOOK_FOLDER = Path(__file__).parent.parent.parent / "examples"
NOTEBOOK_APP = Path(__file__).parent.parent.parent / "examples" / "notebook.py"

# Project specific configuration
