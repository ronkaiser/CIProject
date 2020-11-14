import platform
from datetime import date
import os
import json

my_system = platform.uname()
today = str(date.today())
path = os.getcwd()

system_info = {"system": my_system.system, "nodeName": my_system.node, "Release": my_system.release, "Version": my_system.version, "Machine": my_system.machine, "Processor": my_system.processor, "Date": today, "Path": path}


json_object = json.dumps(system_info, indent = 4)


print(json_object) 
