"""This file:
- spawns a backend runner process
- orchestrates the connection of frontend to backend
- exposes the ASGI app as a public object
"""

from frontend.main import app  # expose ASGI app
