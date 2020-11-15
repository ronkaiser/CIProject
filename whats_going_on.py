import platform
from datetime import date
import shutil
import os
import json

my_system = platform.uname()
today = str(date.today())
tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
disk = shutil.disk_usage("/")
key = 'BUILD_NUMBER'
build = os.getenv(key)
path = os.getcwd()


system_info = {"system": my_system.system, "nodeName": my_system.node, "Release": my_system.release,
"Version": my_system.version, "Machine": my_system.machine, "Processor": my_system.processor, "Date": today,
"FreeMem": free_m, "FreeDisk": disk.free, "Build": build, "Path": path}


json_object = json.dumps(system_info, indent = 4)


print(json_object)
