"""
Common functions for update scripts.
"""

import os


def update(publication_name: str, output_path: str, scraper_parser: str) -> None:
    """Use a Docker container scraper+parser to refresh content.

    `scraper_parser` is expected to be a path/name reference to
    a Docker container on hub.docker.com. Its interface is
    expected to output JSON when it's `run`.

    `publication_name` will be used to create a git commit message.

    `output_path` is a relative path in this `data` repo.
    """

    run(
        # Download, parse, and save the output
        f"docker run {scraper_parser} > {output_path}",

        # Commit to git and push to the upstream repo
        "git pull --prune",
        f"git add {output_path}",
        f"git commit -m 'Daily {publication_name} update'",
        "git push origin master",
    )


def run(*commands: str) -> None:
    """Execute a list of commands, breaking on error"""
    for cmd in commands:
        run_single(cmd)


def run_single(command: str) -> None:
    """Execute one command, raising Exception if it has an error"""
    print(f"\nRunning command: {command}")
    if os.system(command) != 0:
        raise Exception("Error running " + command)
