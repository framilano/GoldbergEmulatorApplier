from repo.steamapp_repository import get_game_data
from repo.goldberg_repository import get_latest_goldberg
import service.goldberg_service as goldberg_service
import shutil
import terminal_colored_print as tp
from os import getcwd, remove

def main():
    tp.colored_print("Welcome to GoldbergApplier!", format="Bold;Blinking")

    tp.colored_print("Retrieving latest Goldberg Emulator release...", fg_color=3)
    get_latest_goldberg()
    tp.colored_print("Latest Goldberg Emulator release downloaded!", fg_color=2)
    game_data = None
    app_id = ""
    tp.colored_print("Find your game Steam APP ID here: https://steamdb.info/", format="Bold")
    while (game_data is None):
        app_id = input(tp.colored_sprint("Insert game Steam APP ID: ", format="Bold"))
        game_data = get_game_data(app_id=app_id)
        if (game_data is None): tp.colored_print("This APP ID doesn't exist, try again", fg_color=1)
    
    tp.colored_print(f"Name: {game_data['name']}\nDLCs: {len(game_data['dlcs'])}\nAchievements: {len(game_data['achievements'])}", format="Underline")

    goldberg_service.replace_dll()

    goldberg_service.generate_steam_appid_txt(app_id)

    goldberg_service.unlock_dlcs(game_data['dlcs'])

    goldberg_service.achievements(game_data['achievements'])
    
    goldberg_service.offline_mode()

    goldberg_service.disable_networking()

    #Cleaning
    shutil.rmtree(getcwd()+"/goldberg_folder", ignore_errors=True)
    remove(getcwd()+"/latest.zip")

    tp.colored_print("Goldberg Emulator installed successfully!", fg_color=2)
    input("Press Enter to close this prompt")

if (__name__ == "__main__"): main()