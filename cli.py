"""Command-line interface for the simple shout tool."""

import sys

from tool import shout


if len(sys.argv) > 1:
    user_input = " ".join(sys.argv[1:])
else:
    user_input = "hello"

print(shout(user_input))