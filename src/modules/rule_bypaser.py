from src import *

def get_rules(guildid):
    session = get.ss()
    tokens = get.tokens()
    found = False
    for token in tokens:
        if not found:
            try:
                r = session.get(
                    f"https://discord.com/api/v9/guilds/{guildid}/member-verification?with_guild=false",
                    headers=headers(token)
                )
                if get.debug():
                    input(f"RULE FETCHER: {r.status_code}") 
                    input(f"RULE FETCHER: {r.text}") 
                if r.status_code == 200:
                    rules_list = r.json()["form_fields"][0]["values"]
                    rules = '\n'.join(rules_list)
                    found == True
                    return rules
                else:
                    pass
            except Exception as e:
                if get.debug():
                    input(f"RULE FETCHER: {e}") 


def bypass_rules(token, guildid, jonson=False):
    session = get.ss()
    try:
        r = session.put(
            f"https://discord.com/api/v9/guilds/{guildid}/requests/@me",
            headers=headers(token)
        )
        if get.debug():
            input(f"RULE BYPASS: {r.status_code}")
            input(f"RULE BYPASS: {r.text}")

        if jonson: return r.status_code, r.json()
        else: return r.status_code, r.text
        
    except Exception as e:
        if get.debug():
            input(f"RULE BYPASS: {e}")
        return 69, "failed lol imagine"