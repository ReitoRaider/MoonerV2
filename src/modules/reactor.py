from src import *

def get_reactions(channel_id, message_id):
    found_message = False
    found_emojis = False
    session = get.ss()
    tokens = get.tokens()
    found = False
    emojis = []
    for token in tokens:
        if not found:
            try:
                r = session.get(
                    f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=50",
                    headers=headers(token),
                )
                if get.debug():
                    input(f"REACTION FETCHER: {r.status_code}") 
                    input(f"REACTION FETCHER: {r.text}") 
                if r.status_code == 200:
                    found == True
                    for entry in r.json():
                        if entry["id"] == message_id and entry["channel_id"] == channel_id:
                            found_message = True
                        for message in r.json():
                            for reaction in message.get("reactions", []):
                                emoji_name = reaction["emoji"]["name"]
                                count = reaction["count"]
                                emojis.append(f"{emoji_name}:{count}")
                            return emojis, True, found_message
                    else:
                        return [], False, False
                else:
                    return [], False, False
            except Exception as e:
                if get.debug():
                    input(f"RACTION FETCHER: {e}") 

def react(token, channel_id, message_id, emoji, jonson=False):
    session = get.ss()
    try:
        r = session.put(
            f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/%40me?location=Message&type=0",
            headers=headers(token)
        )
        if get.debug():
            input(f"REACTONER: {r.status_code}")
            input(f"REACTONER: {r.text}")

        if jonson: return r.status_code, r.json()
        else: return r.status_code, r.text
    
    except Exception as e:
        if get.debug():
            input(f"REACTON ERROR {e}")
        return 69, "failed lol imagine"