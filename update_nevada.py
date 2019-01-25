#!/bin/env python3.7

"""
A cron script which parses the current Nevada laws and commits the result to
the data repository.
"""

from util import run


OUTPUT_PATH: str = "usa/nevada/nrs.json"


run(
    # Download, parse, and save the NRS
    f"docker run publiclaw/nevada-nrs > {OUTPUT_PATH}",

    # Commit to git, and push to the upstream repo
    "git pull --prune"
    f"git add {OUTPUT_PATH}",
    "git commit -m 'Daily Nevada update'",
    "git push origin master"
)
