import asyncio
import websockets
import pickle
import json
import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65431        # The port used by the server

async def hello(websocket, path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            line = await websocket.recv()
            print(f"< {line}")
            if line is None:
                return
        
            s.sendall(b'get-data')
            data = s.recv(1024).decode('utf-8')
            print('Received from socket server : ', data)
            await websocket.send(data)

start_server = websockets.serve(hello, "192.168.11.66", 8866)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


