# Python Script to install packages from json index table

# Import Libraries
import json
import subprocess


# Load package json index
installerVars = json.load(open('hypervisor.json'))

# Add "dependencies" package list(s) to (un)install command
for dependency in installerVars["dependencies"]:
	installString = 'sudo apt-get -y install ' +  dependency
	uninstallString = 'sudo apt-get -y remove ' +  dependency
	
# Print dependencies / install command to stdout & Execute (un)install command
	print dependency
	print installString
	subprocess.Popen( installString,  shell=True,  stdin=subprocess.PIPE ).communicate()
	

## Discarded
#print installerVars["dependencies"][dependency]
#subprocess.call("(sudo apt-get install rolldice)", shell=True)
#subprocess.Popen( 'sudo apt-get -y install rolldice',  shell=True,  stdin=subprocess.PIPE ).communicate()
#subprocess.Popen( uninstallString,  shell=True,  stdin=subprocess.PIPE ).communicate()
