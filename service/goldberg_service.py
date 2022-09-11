import os
import sys
import json
import terminal_colored_print as tp
from os import getcwd, mkdir
from shutil import copy
dll_path = ""

def replace_dll():
    global dll_path
    
    found = False
    while (found == False):
        dll_path = input(tp.colored_sprint("Drop game steam_api.dll/steam_api64.dll on the command prompt:\n", format="Bold"))
        
        #Removing file name from path
        dll_path = dll_path.split('\\')
        dll_path.pop()
        for i in range(0, len(dll_path)-1):
            dll_path[i] += '\\'
        dll_path = ''.join(dll_path).replace("\"", '')
        
        #Checking if folder contains steam_api.dll
        for file in os.listdir(dll_path):
            if (file == "steam_api64.dll" or file == "steam_api.dll"): 
                found = True
                break
        if (found): break
        print("This folder doesn't have any steam_api.dll file, try again")

    copy(getcwd()+"/goldberg_folder/steam_api.dll", dll_path)
    copy(getcwd()+"/goldberg_folder/steam_api64.dll", dll_path)
    try:
        mkdir(dll_path + "/steam_settings")
    except (FileExistsError):
        print("There's already a steam_settings folder present")
        input("Press Enter to close this prompt")
        sys.exit(0)
def generate_steam_appid_txt(appid):
    open(dll_path+"/steam_appid.txt", "wb").write(str.encode(appid))

def unlock_dlcs(dlcs_dict):
    choice = input("Unlock all DLCs? (Y/N)  ")
    if (choice == "Y" or choice == "y"):
        
        dlcs_str = ""
        for key in dlcs_dict:
            dlcs_str += f"{key}={dlcs_dict[key]}\n"
        
        dlcs_str = dlcs_str.strip()
        open(dll_path + "/steam_settings/DLC.txt", "wb").write(str.encode(dlcs_str))

def offline_mode():
    choice = input("Emulate Steam offline mode? (Y/N)  ")
    if (choice == "Y" or choice == "y"):
        open(dll_path + "/steam_settings/offline.txt", "wb")

def disable_networking():
    choice = input("Disable all networking capabilities? (Y/N)  ")
    if (choice == "Y" or choice == "y"):
        open(dll_path + "/steam_settings/disable_networking.txt", "wb")

def achievements(achievements_list):
    achievements_json = []
    for achievement in achievements_list:
        description = ""
        if ('description' in achievement): description = achievement['description']
        else: description = None
        achievements_json.append({
            "description": description,
            "displayName":  achievement['displayName'],
            "hidden": achievement['hidden'],
            "icon": achievement['icon'],
            "icongray": achievement['icongray'],
            "name": achievement['name']
        })
        
    
    open(dll_path + "/steam_settings/achievements.json", "wb").write(str.encode(json.dumps(achievements_json, indent='\t')))

