import zmq
import pickle

class ZMQBridgeProducer():
    def __init__(self):
        self.context = zmq.Context()
        self.router_socket = self.context.socket(zmq.ROUTER)
        self.router_socket.bind("tcp://127.0.0.1:5555")

    async def completion(self, request):
        self.router_socket.send_multipart([b"completion", pickle.dumps(request)])
        return pickle.loads(self.router_socket.recv())
        

    async def close(self):
        self.router_socket.close()
        self.context.term()

zmq_producer = ZMQBridgeProducer()