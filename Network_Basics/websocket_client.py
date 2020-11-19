

#http://127.0.0.1:8000/
# WS client example

import asyncio
import websockets

async def hello():
    uri = "ws://127.0.0.1:8000/ws/kps/"
    async with websockets.connect(uri) as websocket:
        flag = True
        while True:
            if flag:
                in_msg = 'Pi Online'

                await websocket.send(in_msg)
                print(f"> {in_msg}")
                flag = False

            resp = await websocket.recv()
            print('From the server : ',resp)

asyncio.get_event_loop().run_until_complete(hello())


