#!/bin/env python3.7

"""
A cron script which parses the current Nevada laws and commits the result to
the data repository.
"""

from util import update

update(
    name="Nevada NRS",
    output_path="usa/nevada/nrs.json",
    scraper_parser="publiclaw/nevada-nrs"
)
