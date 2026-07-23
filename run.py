import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

# Change working directory to src so relative paths (e.g. file uploads) work
os.chdir(os.path.join(os.path.dirname(__file__), "src"))

from main import app  # noqa: E402
