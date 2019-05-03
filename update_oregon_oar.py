#!/bin/env python3.7

"""
A cron script which parses the Oregon Administrative Rules
and commits the result to the data repository.
"""

from src.util import update

update(
    publication_name="Oregon OAR",
    output_path="usa/oregon/oar.json",
    scraper_parser="publiclaw/oregon-oar",
)
