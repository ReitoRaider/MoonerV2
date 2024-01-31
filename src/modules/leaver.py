from src import *

def leave(token, guildid):
    session = get.ss()
    try:
        payload = {
            "lurking": False,
        }

        r = session.delete(
            f"https://discord.com/api/v9/users/@me/guilds/{guildid}",
            json=payload,
            headers=headers(token)
        )

        if get.debug():
            input(f"LEAVER: {r.status_code}") 
            input(f"LEAVER: {r.text}") 

        if r.status_code == 204:
            return "succes"
        else:
            return "failed"
    except Exception as e:
        if get.debug():
            input(f"LEAVER ERROR: {e}")
        else:
            return "failed"