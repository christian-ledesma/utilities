from typing import final
from requests.exceptions import ReadTimeout
from Config.constants import CONSTANTS

from Utilities.EmailHandler import Gmail
from Utilities.JsonHandler import JsonHandler
from Utilities.PathHandler import PathHandler
from Utilities.Scrapper import Scrapper

def get_data():
    data_file = PathHandler.get_current_path() + CONSTANTS.DATA_PATH
    return JsonHandler.read(data_file)


def start():
    try:
        data = get_data()
        output = Scrapper.start(data["SearchUrl"], data["Tag"], data["Class"])
    except ReadTimeout:
        output = Scrapper.start(data["SearchUrl"], data["Tag"], data["Class"], data["AgentString"])
    except Exception as e:
        print(e)
    finally:
        if output is not None:
            sender_login = data["Email"]["Login"]
            receiver = "christian_ledesma_a@hotmail.com" # Dejarlo en blanco
            message = "Algo"
            Gmail.send(sender_login, receiver, message)


if __name__ == "__main__":
    start()
