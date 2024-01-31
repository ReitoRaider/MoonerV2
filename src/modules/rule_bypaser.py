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


def bypass_rules(token, guildid):
    session = get.ss()
    try:
        r = session.put(
            f"https://discord.com/api/v9/guilds/{guildid}/requests/@me",
            headers=headers(token)
        )
        if get.debug():
            input(f"RULE BYPASS: {r.status_code}")
            input(f"RULE BYPASS: {r.text}")
        if r.status_code == 201:
            return "succes" 
        elif r.status_code == 403:
            return "locked"
        elif r.status_code == 429:                          
            return "ratelimit", r.json().get('retry_after')
        elif r.status_code == 401:
            return "invalid"  
        else:
            return "failed"
    except Exception as e:
        if get.debug():
            input(f"RULE BYPASS: {e}")