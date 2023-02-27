"""
This file works as the central point for running the visualization package.
"""
from visualization import app


def main():
    """
    Author(s): Michael Plunkett
    """
    app.run_server(host="localhost", port=8005)
