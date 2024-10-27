"""This file provides a function to lazy load the main backend,
used by subprocess to spawn a new process"""


def entrypoint():
    import backend.main