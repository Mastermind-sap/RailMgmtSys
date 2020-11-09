"""
The main module
"""

from __future__ import (absolute_import, print_function, with_statement)
import animations.intro as intro  # pylint: disable=import-error,unused-import
import core.prompts as prmpt  # pylint: disable=import-error,no-name-in-module
import core.fmgmt             # pylint: disable=import-error,no-name-in-module

o = prmpt.prompt()
o.intro_prompt()
