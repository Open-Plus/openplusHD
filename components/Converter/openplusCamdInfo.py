# 2boom 2011-13
# Modified by ErAzOr
#  CamdInfo3 - Converter
# <widget source="session.CurrentService" render="Label" position="189,397" zPosition="4" size="350,20" noWrap="1" valign="center" halign="center" font="Regular;14" foregroundColor="clText" transparent="1"  backgroundColor="#20002450">
#	<convert type="CamdInfo">Camd</convert>
# </widget>			

from enigma import iServiceInformation
from Components.Converter.Converter import Converter
from Components.ConfigList import ConfigListScreen
from Components.config import config, getConfigListEntry, ConfigText, ConfigPassword, ConfigClock, ConfigSelection, ConfigSubsection, ConfigYesNo, configfile, NoSave
from Components.Element import cached
from Tools.Directories import fileExists
from Poll import Poll
from os import popen
import os

class openplusCamdInfo(Poll, Converter, object):
	def __init__(self, type):
		Converter.__init__(self, type)
		Poll.__init__(self)
		self.poll_interval = 2000
		self.poll_enabled = True
		
	@cached
	def getText(self):
		service = self.source.service
		info = service and service.info()
		if not service:
			return None
		camd = ""
		serlist = None
		camdlist = None
		nameemu = []
		nameser = []
		if not info:
			return ""
		
			# LbPanel 
		if fileExists("/usr/lib/enigma2/python/Plugins/SystemPlugins/LBpanel/plugin.pyo"): 
			if config.plugins.lbpanel.activeemu.value != "none":
				valor = config.plugins.lbpanel.activeemu.value.replace('camemu.', '')
				return valor
			else:			 
				return None
		# TS-Panel
		elif fileExists("/etc/startcam.sh"):
			try:
				for line in open("/etc/startcam.sh"):
					if line.find("script") > -1:
						return "%s" % line.split("/")[-1].split()[0][:-3]
			except:
				camdlist = None
		# domica 8120
		elif fileExists("/etc/init.d/cam"):
			if config.plugins.emuman.cam.value: 
				return config.plugins.emuman.cam.value
		#PKT
		elif fileExists("//usr/lib/enigma2/python/Plugins/Extensions/PKT/plugin.pyo"):
			if config.plugins.emuman.cam.value: 
				return config.plugins.emuman.cam.value
		#HDMU
		elif fileExists("/etc/.emustart") and fileExists("/etc/image-version"):
			try:
				for line in open("/etc/.emustart"):
					return line.split()[0].split('/')[-1]
			except:
				return None
	
		# AAF & ATV & VTI 
		elif fileExists("/etc/image-version") and not fileExists("/etc/.emustart"):
			emu = ""
			server = ""
			for line in open("/etc/image-version"):
				if line.find("=AAF") > -1 or line.find("=OpenPlus") > -1 or line.find("=openATV") > -1:
					if config.softcam.actCam.value: 
						emu = config.softcam.actCam.value
						if "Oscam" in config.softcam.actCam.value:
							if fileExists("/tmp/.oscam/oscam.version"):
								try:
									for line in open("/tmp/.oscam/oscam.version"):
										if line.find("Version") > -1:
											item = line.split(":",1)
											emu = item[1].strip()
								except:
									pass
			        if config.softcam.actCam2.value: 
						server = config.softcam.actCam2.value
						if config.softcam.actCam2.value == "no CAM 2 active" or config.softcam.actCam2.value == "Keine CAM 2 aktiv":
							server = ""
				elif line.find("=vuplus") > -1:
					if fileExists("/tmp/.emu.info"):
						for line in open("/tmp/.emu.info"):
							emu = line.strip('\n')
			return "%s - %s" % (emu, server)
		# BlackHole	
		elif fileExists("/etc/CurrentBhCamName"):
			try:
				camdlist = open("/etc/CurrentBhCamName", "r")
			except:
				return None
		# Domica	
		elif fileExists("/etc/active_emu.list"):
			try:
				camdlist = open("/etc/active_emu.list", "r")
			except:
				return None
		# Egami	
		elif fileExists("/tmp/egami.inf","r"):
			for line in open("/tmp/egami.inf"):
				item = line.split(":",1)
				if item[0] == "Current emulator":
					return item[1].strip()
		#Pli
		elif fileExists("/etc/init.d/softcam") or fileExists("/etc/init.d/cardserver"):
			try:
				for line in open("/etc/init.d/softcam"):
					if line.find("echo") > -1:
						nameemu.append(line)
				camdlist = "%s" % nameemu[1].split('"')[1]
			except:
				pass
			try:
				for line in open("/etc/init.d/cardserver"):
					if line.find("echo") > -1:
						nameser.append(line)
				serlist = "%s" % nameser[1].split('"')[1]
			except:
				pass
			if serlist is None:
				serlist = ""
			elif camdlist is None:
				camdlist = ""
			elif serlist is None and camdlist is None:
				serlist = ""
				camdlist = ""
			return ("%s %s" % (serlist, camdlist))
		# OoZooN
		elif fileExists("/tmp/cam.info"):
			try:
				camdlist = open("/tmp/cam.info", "r")
			except:
				return None
		# Merlin2	
		elif fileExists("/etc/clist.list"):
			try:
				camdlist = open("/etc/clist.list", "r")
			except:
				return None
		# GP3
		elif fileExists("/usr/lib/enigma2/python/Plugins/Bp/geminimain/lib/libgeminimain.so"):
			try:
				from Plugins.Bp.geminimain.plugin import GETCAMDLIST
				from Plugins.Bp.geminimain.lib import libgeminimain
				camdl = libgeminimain.getPyList(GETCAMDLIST)
				cam = None
				for x in camdl:
					if x[1] == 1:
						cam = x[2] 
				return cam
		   	except:
				return None
		else:
			return None
			
		if serlist is not None:
			try:
				cardserver = ""
				for current in serlist.readlines():
					cardserver = current
				serlist.close()
			except:
				pass
		else:
			cardserver = " "

		if camdlist is not None:
			try:
				emu = ""
				for current in camdlist.readlines():
					emu = current
				camdlist.close()
			except:
				pass
		else:
			emu = " "
			
		return "%s %s" % (cardserver.split('\n')[0], emu.split('\n')[0])
		
	text = property(getText)

	def changed(self, what):
		Converter.changed(self, what)
