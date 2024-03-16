import subprocess

pauseBridgeCallPath = "./pause.sh"
winePrefix = "" # should be modified to your wine prefix
pauseCommand = ["bash", pauseBridgeCallPath, winePrefix]

def pausePlayer():
	subprocess.Popen(pauseCommand)

pausePlayer()

