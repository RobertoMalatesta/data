#!/bin/env python3.7

# A script, meant to be run from cron, which parses
# the current Nevada laws and commits the result to
# the data repository.

import os


def run(command):
    if os.system(command) != 0:
        raise Exception("Error running " + command)


run("docker run publiclaw/nevada-nrs > usa/nevada/nrs.json")
run("git add usa/nevada/nrs.json")
run("git commit -m 'Daily Nevada update'")
run("git push origin master")
