from fastapi import APIRouter
from zmq_server import zmq_producer

router = APIRouter(prefix="/v1", tags=["openAI"])


@router.post("/completions")
async def generate_completion():
    """Function to generate a completion"""
    # TODO: dispatch to ZMQ bridge
    ...


@router.post("/chat/completions")
async def generate_chat_completion():
    """function to generate a chat completion"""
    # TODO: dispatch to ZMQ bridge
    ...
