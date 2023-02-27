"""
This file works as the central point for running the visualization package.
"""
from visualization import app


def main():
    """
    Author(s): Michael Plunkett
    """
    print("We are gonna do some visualization")
    if __name__ == "__main__":
        app.run_server(host="localhost", port=8005)
