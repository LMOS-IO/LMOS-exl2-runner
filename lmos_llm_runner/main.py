"""This file:
- spawns a backend runner process
- orchestrates the connection of frontend to backend
- exposes the ASGI app as a public object
"""

import multiprocessing

from backend.entrypoint import entrypoint as backend
from frontend.main import app  # expose ASGI app

if __name__ == "__main__":
    mp_context = multiprocessing.get_context('spawn')
    backend = mp_context.Process(target=backend)
    backend.start()

    import uvicorn
    uvicorn.run(app)