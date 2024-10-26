"""This file runs a bundled instance of uvicorn"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")