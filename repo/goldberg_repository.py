import requests
from zipfile import ZipFile
from os import getcwd

def get_latest_goldberg():
    res = requests.get("https://gitlab.com/Mr_Goldberg/goldberg_emulator/-/jobs/2987292049/artifacts/download", stream=True)
    open(getcwd()+'/latest.zip', 'wb').write(res.content)
    ZipFile(getcwd()+'/latest.zip', 'r').extractall(getcwd()+"/goldberg_folder")
