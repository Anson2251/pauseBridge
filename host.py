import subprocess

pauseBridgeCallPath = "./pause.sh"
winePrefix = "/home/anson/wine/netease-cloud-music/"
pauseCommand = ["bash", pauseBridgeCallPath, winePrefix]

def pausePlayer():
	subprocess.Popen(pauseCommand)

pausePlayer()

