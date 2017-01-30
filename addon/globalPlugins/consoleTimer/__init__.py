# consoleTimer: An Add-on for nvda that does <Insert thing here>

#Copyright (C) 2016-2017 derek riemer

#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""consoleTimer:
A global plugin to make consoles read correctly.
"""

import globalPluginHandler
import ui
import editableText
from NVDAObjects import behaviors
import addonHandler
addonHandler.initTranslation()

class TerminalChange(editableText.EditableText):
	timeout = 0.05 #wait longer for terminals by default.

	def _hasCaretMoved(self, bookmark, retryInterval=0.01, timeout=0.03):
		return super(TerminalChange, self)._hasCaretMoved(bookmark, retryInterval, TerminalChange.timeout)

	def script_incrTimeout(self, gesture):
		TerminalChange.timeout+=.01
		#Translators: Just tells the user that NVDA will be more patient.
		ui.message(_("I'm being {} patient, more than before.").format(TerminalChange.timeout))
	#Translators: Message for console Timer to increase the amount of time NVDA will wait.
	script_incrTimeout.__doc__ = _("Increases the time NVDA waits before giving up on consoles to change.")
	#Translators: Category for Console timer.
	script_incrTimeout.category = _("Console Timer")

	def script_decrTimeout(self, gesture):
		if TerminalChange.timeout >= .01:
			TerminalChange.timeout-=.01
			#Translators: Just tells the user that NVDA will be less patient.
			ui.message("I'm being {} patient, less than before.".format(TerminalChange.timeout))
		else:
			#Translators: Just the word for error.
			ui.message(_("Error"))
	#Translators: Message for console Timer to Decrease the amount of time NVDA will wait.
	script_decrTimeout.__doc__ = _("Increases the time NVDA waits before giving up on consoles to change.")
	#Translators: Category for Console timer.
	script_decrTimeout.category = _("Console Timer")




	__gestures = {
		"kb:nvda+shift+pageUp" : "incrTimeout",
		"kb:nvda+shift+pageDown" : "decrTimeout",
	}


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def chooseNVDAObjectOverlayClasses(self,obj,clsList):
		if behaviors.Terminal in clsList or obj.windowClassName in (u"ConsoleWindowClass"):
			clsList.insert(0, TerminalChange)

