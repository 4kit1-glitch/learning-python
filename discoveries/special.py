import os
import platform
import sys


print(__file__) # stores the script current location
print(sys.executable) # name of interpreter
print(sys.version_info.minor)
print(sys.version_info)
print(os.name) # name will be nt for windows
print(sys.platform)

print(platform.system())
print(platform.node())