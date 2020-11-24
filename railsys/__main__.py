"""
The main module
"""

from __future__ import (absolute_import, print_function, with_statement)
import animations.intro as intro  # pylint: disable=import-error,unused-import
import core.prompts as prmpt  # pylint: disable=import-error,no-name-in-module
import core.fmgmt as dbase    # pylint: disable=import-error,no-name-in-module

# o = prmpt.prompt()
# o.intro_prompt()


class Ask:
    """This will be the main class interacting with the user"""
    def __init__(self):
        self.ask = prmpt.prompt()

    def __str__(self):
        print("This is the Ask class. railsys/__main__.")

    def intro_ask(self):
        """Asks the questions when the program is first launched"""
        self.ask.intro_prompt()
        inp = input("Enter your choice : ")
        return inp

    def train_ask(self):
        """ To be written """
        self.ask.train_book_prompt()
        inp = input("Enter your choice : ")
        return inp

    def class_ask(self):
        """ To be written """
        self.ask.train_opts_prompt()
        inp = input("Enter your choice : ")
        return inp

    def date_ask(self):
        """To be written"""


class Admin:
    "This class contains methods that allows\
    adding new Train schedules to the database"

    def __init__(self):
        self.db = dbase.MakeDb("TrainInfo")  # pylint: disable=invalid-name

    def add_info(self, trainid, train_name, journey, timing):
        """To be written"""
        self.db.store_values(trainid, train_name, journey, timing)

    def del_info(self, trainid, train_name, journey, timing):
        """To be written"""
        self.db.delete_data(trainid, train_name, journey, timing)
