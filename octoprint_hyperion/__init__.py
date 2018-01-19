#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# coding=utf-8

from __future__ import absolute_import
import re
import os
import string
import octoprint.plugin

class OctoprintHyperionPlugin(octoprint.plugin.AssetPlugin,
							octoprint.plugin.SettingsPlugin,
							octoprint.plugin.ShutdownPlugin,
							octoprint.plugin.StartupPlugin,
							octoprint.plugin.TemplatePlugin):

	def __init__(self):
		self._logger.debug(u"OctoprintHyperion init")

	def on_after_startup(self):
		self._logger.debug(u"OctoprintHyperion Startup")

	def on_shutdown(self):
		self._logger.debug(u"OctoprintHyperion Shutdown")

	def HandleM150(self, comm_instance, phase, cmd, cmd_type, gcode, *args, **kwargs):
		if gcode and cmd.startswith("M150"):
			self._logger.debug(u"M150 Detected: %s" % (cmd,))
			# Emulating Marlin 1.1.0's syntax
			# https://github.com/MarlinFirmware/Marlin/blob/RC/Marlin/Marlin_main.cpp#L6133
			command = "hyperion-remote " + cmd
			command = string.replace(command, 'M150 ', ' ')
			command = command.lower()
			returned_value = os.system(command)  # returns the exit code in unix
			self._logger.debug(u"returned value: %s" % (command,))
            
	##~~ SettingsPlugin mixin

	def get_settings_version(self):
		return 1

	def get_template_configs(self):
		return [
			dict(type="settings", name="Octoprint Hyperion Configuration", custom_bindings=False)
		]

	def get_settings_defaults(self):
		return dict(r=0, g=0, b=0, pigpiod=False)

	def on_settings_initialized(self):
		self._logger.debug(u"OctoprintHyperion on_settings_load()")

	def on_settings_save(self, data):
		self._logger.debug(u"OctoprintHyperion on_settings_save()")
		octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
	
	##~~ Softwareupdate hook

	def get_update_information(self):
		return dict(
			ledstripcontrol=dict(
				displayName="Octoprint Hyperion Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="google",
				repo="OctoPrint-hyperion",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/systemik/OctoPrint-hyperion/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "Octoprint Hyperion"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = OctoprintHyperionPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information,
		"octoprint.comm.protocol.gcode.queuing": __plugin_implementation__.HandleM150
	}

