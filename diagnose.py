#!/usr/bin/python
# Copyright (c) 2015 Matheus SIlva
# System diagnose tool run it before sending a bug report

import platform as sysinfo
import base64 as encoder

nl = '\n'
EI = sysinfo.platform() + nl + sysinfo.machine() + nl + sysinfo.processor() + nl + sysinfo.system() + ' ' + sysinfo.version()


file = open("system.info", "w+")
file.write(EI)
file.close()

print (encoder.b85encode(bytes(EI, "utf-8")))
