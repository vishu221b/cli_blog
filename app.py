from models.blog import Blog
from database import Database
import pprint
from menu import Menu


Database.initialize()
menu = Menu()
flow = menu.run_menu()