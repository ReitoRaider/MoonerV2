from src import *

def leave(token, guildid, jonson=False):
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

        if jonson: return r.status_code, r.json()
        else: return r.status_code, r.text
    
    except Exception as e:
        if get.debug():
            input(f"LEAVER ERROR: {e}")
        else:
            return 69, "failed lol imagine"