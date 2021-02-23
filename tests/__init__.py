import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
REPO_DIR = SCRIPT_DIR.parent

sys.path.append(str(REPO_DIR))
