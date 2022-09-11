
from selenium import webdriver
import time

from input import get_input
from chessdotcom import actions
from chessdotcom.label_game import label_game
from darknetconvert import create_training_data_file_structure
from chessdotcom.changeboardstyle import change_board_style
from chessdotcom.actions import get_game_ids
from flags import flags
from chessdotcom.xpaths import xpaths
from flags import flags

get_input()

driver_location = "/snap/bin/chromium.chromedriver"
binary_location = "/usr/bin/chromium-browser"

options = webdriver.ChromeOptions()
options.binary_location = binary_location
options.add_argument("--user-data-dir=./user_data")

driver = webdriver.Chrome(executable_path=driver_location, options=options)
driver.maximize_window()

create_training_data_file_structure()

if flags['game_id'] == '':
    game_ids, game_ids_with_username = get_game_ids(driver, flags['username'])
else:
    game_ids = [flags['game_id']]
    game_ids_with_username = [f"{flags['game_id']}?username={flags['username']}"]

change_board_style(driver, flags['board_style'])

for index in range(0, len(game_ids)):   
    flags['game_id'] = game_ids[index]
    flags['game_id_with_username'] = game_ids_with_username[index]

    print(f"https://www.chess.com/game/live/{flags['game_id_with_username']}")
    driver.get(f"https://www.chess.com/game/live/{flags['game_id_with_username']}")
    time.sleep(2)
    actions.click_element(driver, xpaths['end_game_pop_up'])
    actions.click_element(driver, xpaths['game_start'])
    label_game(driver, str(flags['board_style']))
    


