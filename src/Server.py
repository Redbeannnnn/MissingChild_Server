import websockets
import asyncio


class Server:
    def __init__(self,socket_port:int = 8765):
        self.clients:list = []
        self.socket_port = socket_port
        pass

    # 启动服务器
    async def start(self):
        async with websockets.serve(self.receive_message, "localhost", self.socket_port) as websocket:
            print(f"Server is running on ws://localhost:{self.socket_port}")
            await asyncio.Future()

    # 接收消息
    async def receive_message(self, websocket):
        while True:
            try:
                message = await websocket.recv()
                self.clients.append(websocket)
                self.get_command(message["player"],message["message"])
            except websockets.exceptions.ConnectionClosed:
                self.clients.remove(websocket)
                print("Connection closed")
                break

    # 发送消息给所有客户端
    async def send_message_to_all(self, message):
        for client in self.clients:
            try:
                await client.send(message)
            except websockets.exceptions.ConnectionClosed:
                self.clients.remove(client)
                print("Connection closed")

    # 发送消息给指定客户端
    async def send_message_to_client(self, websocket, message):
        try:
            await websocket.send(message)
        except websockets.exceptions.ConnectionClosed:
            self.clients.remove(websocket)
            print("Connection closed")

    def get_command(self,player:str,message:str):
        pass

    def get_client_number(self):
        msg={"command":"heart_beat"}
        self.send_message_to_all(msg)
        return len(self.clients)
    

    


