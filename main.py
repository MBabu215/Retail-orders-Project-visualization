# import constants from the'constants.py'
print('constants from constants.py')
import constants
print(constants.MAX_PLAYERS)
print(constants.ESCORT_CARS)
print(constants.SPEED_LIMIT)

from constants import MAX_PLAYERS,ESCORT_CARS,SPEED_LIMIT
print(MAX_PLAYERS)

#importing from .env
print("constants from dotenv")
import os 
from dotenv import load_dotenv
load_dotenv()
MAX_PLAYERS = os.getenv('MAX_PLAYERS')
ESCORT_CARS = os.getenv('ESCORT_CARS')
print(MAX_PLAYERS)
print(ESCORT_CARS)
