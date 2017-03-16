# consoleTimer #

consoleTimer was written by derek riemer, and is GPL V2, as required by being an NVDA addon.

* [Source available on Github:](https://github.com/derekriemer/consoleTimer)

## Background

When using command lines over ssh, usually, there's network lag. This lag is expected, however, the way NVDA handles cursor movement is not friendly with lag in terminals, because this operation is a synchrinous opperation. This causes NVDA to wrongly report the wrong letter when moving to another letter with the arrow keys. For example, if the user is on the p of grep, and they press right arrow, they may hear "t" instead of space. This is due to NVDA not waiting long enough to actually properly handle this cursor movement.
This addon was written because I do lots of server administration, and I wanted cursor navigation to work.

## TLDR usage instructions

When in a console, if NVDA is missing or repeating letters as you move around, simply press nvda+shift+pageup to teach it to be more patient, or if it is too laggy, press nvda+shift+page down to teach it to be less patient. This addon will have no affect outside terminals, and the patience changes by .01 for every keypress.

## How to make this work with custom terminals
If you are a developer who wants NVDA to recognize a section or portion of your app as a terminal, and it isn't already, you should implement an appModule for this purpose, to gain the relevant behavior, I.E. announcement of new text written to stdout, etc. Please raise a ticket against [NVDA](https://github.com/nvaccess/nvda/issues/new), and we can help you get your terminal appModule into the screen reader. Support for Putty, Cygwin (Mintty), and secureCRT is already implemtned. Apps such as R may be implemented in the future.
If your app is properly recognized as a terminal by NVDA, (The termminal behavior is properly injected at runtime), this addon should just work. If it doesn't, please let me know via an issue. How to write an app module is out of scope for this document, but is well documented in the [NVDA Developer Guide](https://www.nvaccess.org/files/nvda/documentation/developerGuide.html). This example illustrates [an appModule to teach NVDA that the terminal window on PuTTY is a terminal](https://github.com/nvaccess/nvda/blob/master/source/appModules/putty.py). Also, [Here's an example implementation for MinTTY](https://github.com/nvaccess/nvda/blob/master/source/appModules/mintty.py). The most important thing to make sure happens is that NVDAObjects.behaviors.Terminal is injected to the class list.