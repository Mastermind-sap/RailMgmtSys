"""
This contains some attractive strings for the terminal created using cfonts.
"""
from __future__ import (print_function, absolute_import, with_statement)
from cfonts import render, say  # pylint: disable=import-error,unused-import
import time
import os

def animate():
    word="RAILWAY MGMT SYS"
    for i in range(1,len(word)+1):
        print(render(word[0:i], colors=['red', 'yellow'], align='center'))
        time.sleep(0.2)
        os.system('cls')
