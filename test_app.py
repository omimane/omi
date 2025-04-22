# tests/test_app.py

import pytest
from app import some_function_to_test  # Assuming you have functions like this

def test_some_function():
    """Test that a function in app.py works correctly."""
    result = some_function_to_test(10, 20)
    assert result == 30, f"Expected 30, but got {result}"

# Example to test if the app runs (simulating Streamlit app launch):
import subprocess

def test_streamlit_app_runs():
    """Test that Streamlit app starts without errors"""
    result = subprocess.run(
        ['streamlit', 'run', 'app.py', '--server.headless', 'true'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    assert result.returncode == 0, f"Streamlit app failed to start: {result.stderr.decode()}"
