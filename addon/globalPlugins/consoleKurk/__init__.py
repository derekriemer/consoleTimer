# consoleKurk: An Add-on for nvda that does <Insert thing here>

#Copyright (C) 2016 derek riemer

#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""consoleKurk:
A global plugin 
"""

import globalPluginHandler
import ui
import editableText
import controlTypes
import brailleInput

class TerminalChange(editableText.EditableText):
	timeout = 0.03
	def _hasCaretMoved(self, bookmark, retryInterval=0.01, timeout=0.03):
		return super(TerminalChange, self)._hasCaretMoved(bookmark, 0.01, TerminalChange.timeout)

	def script_incrTimeout(self, gesture):
		TerminalChange.timeout+=.01
		ui.message("I'm being {} patient, more than before.".format(TerminalChange.timeout))

	def script_decrTimeout(self, gesture):
		if TerminalChange.timeout >= .01:
			TerminalChange.timeout-=.01
			ui.message("I'm being {} patient, less than before.".format(TerminalChange.timeout))
		else:
			ui.message("No, I can't do that, you don't want me to be less patient.")

	def script_guessCharSpeed(self, gesture):
		minSpeed = 0
		maxSpeed=1000
		TerminalChange.timeout = maxSpeed
		guess = .03
		#Until speed is within the allowed delta, we keep sending d and backspace, and seeing how long it takes for us to respond.
		self.runningTest = True
		while maxSpeed-minSpeed > DELTA:
			#Send d
			brailleInput.handler.sendChars("d")

	__gestures = {
		"kb:nvda+shift+pageUp" : "incrTimeout",
		"kb:nvda+shift+pageDown" : "decrTimeout",
	}

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def chooseNVDAObjectOverlayClasses(self,obj,clsList):
		if obj.role == controlTypes.ROLE_TERMINAL or obj.windowClassName in (u'ConsoleWindowClass', u'mintty'):
			clsList.insert(0, TerminalChange)

