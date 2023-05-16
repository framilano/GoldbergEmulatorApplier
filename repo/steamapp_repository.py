import requests
import dotenv
from os import getcwd
    
def get_dlcs(app_id):
    response = requests.get(f"https://store.steampowered.com/api/appdetails/?appids={app_id}")
    response_json = response.json()

    dlcs_ids = []
    if ("dlc" in response_json[app_id]['data']):
        dlcs_ids = response_json[app_id]['data']['dlc']

    dlcs = {}
    for id in dlcs_ids:
        response_dlc = requests.get(f"https://store.steampowered.com/api/appdetails/?appids={id}")
        response_dlc_json = response_dlc.json()
        dlcs[id] = response_dlc_json[str(id)]['data']['name']

    return dlcs

def get_game_data(app_id):
    api_key = dotenv.get_key(dotenv_path=getcwd()+"/.env", key_to_get='api_key')
    
    #Retrieving Game Name and Achievements
    response = requests.get(f"http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2?appid={app_id}&key={api_key}")
    response_json = response.json()
    
    if (len(response_json) == 0): return None

    #Game has been removed from Steam, response is valid but data are not
    try:
        game_data = {
            "name": response_json['game']['gameName'],
            "achievements": response_json['game']['availableGameStats']['achievements'],
            "dlcs": get_dlcs(str(app_id)),
        }
        return game_data
    except(KeyError):
        return "invalid_game_data"

