"""
Common functions for update scripts.
"""

import os


def run(*commands: str) -> None:
    """Execute a list of commands, breaking on error"""
    for cmd in commands:
        run_single(cmd)


def run_single(command: str) -> None:
    """Execute one command, raising Exception if it has an error"""
    if os.system(command) != 0:
        raise Exception("Error running " + command)
