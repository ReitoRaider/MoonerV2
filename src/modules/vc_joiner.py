from src import *
import websocket

def join_vc(token, guild, channel, mute, deaf):
    try:
        for _ in range(1):
            ws = websocket.WebSocket()

            ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")

            ws.send(json.dumps({
                "op": 2,
                "d": {
                    "token": token,
                    "properties": {
                        "$os": "windows",
                        "$browser": "Discord",
                        "$device": "desktop"
                    }
                }
            }))

            ws.send(json.dumps({
                "op": 4,
                "d": {
                    "guild_id": guild,
                    "channel_id": channel,
                    "self_mute": False,
                    "self_deaf": False
                }
            }))
            return "succes"
    except:
        return "failed"