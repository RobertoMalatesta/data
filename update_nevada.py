#!/bin/env python3.7

"""
A script, meant to be run from cron, which parses
the current Nevada laws and commits the result to
the data repository.
"""

import os
from typing import List


def run_all(commands: List[str]) -> None:
    """Execute a list of commands, breaking on error"""
    for cmd in commands:
        run(cmd)


def run(command: str) -> None:
    """Execute a command, raising Exception if it has an error"""
    if os.system(command) != 0:
        raise Exception("Error running " + command)


run_all([
    "docker run publiclaw/nevada-nrs > usa/nevada/nrs.json",
    "git add usa/nevada/nrs.json",
    "git commit -m 'Daily Nevada update'",
    "git push origin master"
])
