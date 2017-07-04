#  This code is licensed under the  GLP 3.0 
#  To view a copy of this license, visit
#  https://www.gnu.org/licenses/gpl-3.0.en.html
#
#  This plugin is NOT free software. It is open source, you are allowed to
#  modify it (if you keep the license) and it may  be commercially 
#  distributed  under the conditions noted above, ever with the sources.
#  
#  by iqas Openplus 2017

from Components.Converter.Converter import Converter
from enigma import iServiceInformation, iPlayableService, eTimer, eServiceReference, eConsoleAppContainer
from Components.Element import cached
import os
from Poll import Poll


class Bitrate2op(Poll, Converter, object):

        def __init__(self, type):
                Converter.__init__(self, type)
                Poll.__init__(self)
                self.poll_interval = 500
                self.poll_enabled = True
                self.container = eConsoleAppContainer()
                self.type = self.retval = type
                self.container.dataAvail.append(self.dataAvail)

        def dataAvail(self, str):
                print str
                video, audio = str.split(' ')
                self.retval = self.type.replace('%A', '%s' % audio[:-1]).replace('%V', '%s' % video)
                print self.retval

        @cached
        def getText(self):

                service = self.source.service
                vpid = apid = dvbnamespace = tsid = onid = -1
                if service:
                        serviceInfo = service.info()
                        vpid = serviceInfo.getInfo(iServiceInformation.sVideoPID)
                        apid = serviceInfo.getInfo(iServiceInformation.sAudioPID)
                        adapter = 0
                        demux = 0
                            
                        try:
                                stream = service.stream()
                                if stream:
                                        streamdata = stream.getStreamingData()
                                        if streamdata:
                                                if 'demux' in streamdata:
                                                        demux = streamdata["demux"]
                                                if 'adapter' in streamdata:
                                                        adapter = streamdata["adapter"]
                        except:
                                pass

                        cmd = "/usr/bin/opbitrate " + str(adapter) + " " + str(demux) + " " + str(vpid) + " " + str(apid)
                        print cmd
                        self.container.execute(cmd)
                return self.retval

        text = property(getText)
