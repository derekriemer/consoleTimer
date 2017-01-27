# consoleKurk: An Add-on for nvda that does <Insert thing here>

#Copyright (C) 2016 derek riemer

#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""consoleKurk:
A global plugin to make consoles read correctly.
"""

import time
import globalPluginHandler
import ui
import editableText
import controlTypes
from NVDAObjects import behaviors

class TerminalChange(editableText.EditableText):
	timeout = 0.05 #wait longer for terminals by default.

	def _hasCaretMoved(self, bookmark, retryInterval=0.01, timeout=0.03):
		return super(TerminalChange, self)._hasCaretMoved(bookmark, retryInterval, TerminalChange.timeout)

	def script_incrTimeout(self, gesture):
		TerminalChange.timeout+=.01
		ui.message("I'm being {} patient, more than before.".format(TerminalChange.timeout))

	def script_decrTimeout(self, gesture):
		if TerminalChange.timeout >= .01:
			TerminalChange.timeout-=.01
			ui.message("I'm being {} patient, less than before.".format(TerminalChange.timeout))
		else:
			ui.message("Error")


	__gestures = {
		"kb:nvda+shift+pageUp" : "incrTimeout",
		"kb:nvda+shift+pageDown" : "decrTimeout",
	}


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def chooseNVDAObjectOverlayClasses(self,obj,clsList):
		if behaviors.Terminal in clsList or obj.windowClassName in (u"ConsoleWindowClass"):
			clsList.insert(0, TerminalChange)

