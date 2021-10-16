import os
import sys
import subprocess
blender_path = "E:/Program Files/Blender Builds/stable/blender-2.93.4-windows-x64/blender.exe"
script_loc = "C:/Users/yiann/Desktop/blender.py"
# blender = subprocess.Popen([blender_path, '',
#      '--python', "subprocess.blend", ''])

#exit(subprocess.call([blender_path, '--background','--python', "subprocess.blend", '--'] + sys.argv))
subprocess.Popen([blender_path,'--python',script_loc])



