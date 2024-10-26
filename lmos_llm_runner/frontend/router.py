from fastapi import APIRouter

router = APIRouter(prefix="/v1", tags=["openAI"])


@router.post("/completions")
def generate_completion():
    """Function to generate a completion"""
    # TODO: dispatch to ZMQ bridge
    ...


@router.post("/chat/completions")
def generate_chat_completion():
    """function to generate a chat completion"""
    # TODO: dispatch to ZMQ bridge
    ...
