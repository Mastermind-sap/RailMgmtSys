"""
This module contains all the prompts for the System
"""
from __future__ import (print_function, absolute_import, with_statement)
from tabulate import tabulate   # pylint: disable=import-error

class prompt_str:
    "This class contains the strings for the prompt"
    intro_str = [
                 ["1", "Book a Train"],
                 ["2", "Cancel a reservation"],
                 ["3", "Call an Ambulance"],
                 ["4", "Check Train Status"],
                 ["5", "Order a meal"],
                 ["6", "Exit"],
                 ["7", "Admin"]
                ]

    train_book = [
                 ["1", "Rajdhani Express"],
                 ["2", "Durantor Express"],
                 ["3", "Maharaja Express"],
                 ["4", "Gareebrath Express"],
                 ["5", "Nova Express"]
                 ]

    train_opts = [
                ["1", "First Tier"],
                ["2", "Second Tier"],
                ["3", "Third Tier"]
                 ]


class prompt:
    "This will create the prompt for intro"
    def __init__(self):
        self.prompts = prompt_str()

    def intro_prompt(self):
        headers = ["Options" , "Prompt"]    # pylint disable 
        print(tabulate(self.prompts.intro_str, headers, tablefmt="fancy_grid"))   # pylint disable 

    def train_book_prompt(self):
        headers = ["Options" , "Prompt"]    # pylint disable 
        print(tabulate(self.prompts.train_book, headers , tablefmt="fancy_grid"))   # pylint disable 

    def train_opts_prompt(self):
        print(self.prompts.train_opts)

prompt().train_book_prompt()
