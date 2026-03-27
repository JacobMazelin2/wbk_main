"""Ensure Webots controller Python bindings are on sys.path before `import controller`."""

from __future__ import annotations

import os
import sys


def prepend_webots_controller_python_path() -> None:
    """Prepend $WEBOTS_HOME/lib/controller/pythonXY for the current interpreter."""
    home = os.environ.get("WEBOTS_HOME", "/usr/local/webots")
    major, minor = sys.version_info[:2]
    py_dir = f"python{major}{minor}"
    lib_controller = os.path.join(home, "lib", "controller")
    path = os.path.join(lib_controller, py_dir)
    if os.path.isdir(path) and path not in sys.path:
        sys.path.insert(0, path)


def format_webots_controller_help() -> str:
    home = os.environ.get("WEBOTS_HOME", "/usr/local/webots")
    lib_controller = os.path.join(home, "lib", "controller")
    avail: list[str] = []
    if os.path.isdir(lib_controller):
        avail = sorted(
            x
            for x in os.listdir(lib_controller)
            if x.startswith("python") and os.path.isdir(os.path.join(lib_controller, x))
        )
    return (
        f"WEBOTS_HOME={home!r}, controller dirs={avail}, "
        f"need bindings for Python {sys.version_info.major}.{sys.version_info.minor}. "
        "Install a Webots release whose lib/controller includes that folder, or align Python with an available folder."
    )
