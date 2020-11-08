"""
The main module

"""
from __future__ import absolute_import
import animations.intro as intro  # pylint: disable=import-error
import core.prompts as prompt  # pylint: disable=import-error

intro.animate()
prompt.intro_prompt


