from src import *

def fetch_guild(invite):
    try:
        r = requests.get(
            f"https://discord.com/api/v9/invites/{invite}?inputValue={invite}&with_counts=true&with_expiration=true",
            )
        
        data = r.json()
        guild = data['guild']
        inviter = data['inviter']
        info = [
            "Invite: " + data["code"],
            "Inviter ID: " + inviter["id"],
            "Inviter name: " + inviter["username"],
            "Guild ID: " + data["guild_id"],
            "Guild name: " + guild["name"],
            "Channel ID: " + data["channel"]["id"],
            "Channel name: " + data["channel"]["name"],
            "Member count: " + str(data["approximate_member_count"]),
            "Online member count: " + str(data["approximate_presence_count"]),
        ]

    
        return '\n'.join(info)
    except Exception as e:
        if get.debug:
            input(f"GUILD INFO FETCHER: {e}")
        else:
            return "Unknown"