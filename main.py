import asyncio
import websockets

# INX-MQTT WebSocket settings
WS_HOST = 'inx-mqtt'
WS_PORT = 1888

# INX-MQTT topics
TOPIC_CONFIRMED = '$IOTA/tangle/confirmed'
TOPIC_UNCONFIRMED = '$IOTA/tangle/unconfirmed'

async def subscribe(websocket):
    # subscribe to topics
    await websocket.send(TOPIC_CONFIRMED)
    await websocket.send(TOPIC_UNCONFIRMED)

async def on_message(websocket, path):
    async for message in websocket:
        print('Received message on topic %s: %s' % (path, message))

# create WebSocket client
start_server = websockets.serve(on_message, WS_HOST, WS_PORT, ping_interval=None, ping_timeout=None)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_until_complete(subscribe(start_server.ws_server.connection_made_future()))
asyncio.get_event_loop().run_forever()
