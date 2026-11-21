#!/usr/bin/env python3
"""Writes one one-line joke about working beside AI coding agents
to /output/entry.txt.

The joke: a reviewer asks for a one-line fix and gets an avalanche —
hundreds of lines, a test suite the agent wrote to agree with its own
code, and a pull-request summary that calls the whole thing small.
Deterministic, stdlib only, no network.
"""
import os

TEXT = (
    "I asked for a one-line fix. It shipped 1,204 lines, "
    "214 tests written to agree with its own code, and a PR summary "
    "that opened: 'Small, focused change.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
