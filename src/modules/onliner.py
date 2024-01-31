from src import *
import websocket

def online(token):
    try:
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
        ws.send(
            json.dumps(
                {
                    "op": 2,
                    "d": {
                        "token": token,
                        "properties": {
                            "$os": "Windows",
                        },
                    },
                }
            )
        )
    except:
        pass