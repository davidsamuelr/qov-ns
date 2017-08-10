import commands
#import re

def onlyTimes(ping):
	pingTimes = (commands.getoutput("echo \""+ping+"\" | grep time= | awk -F 'time=' {'print $2'} | awk -F ' ms' {'print $1'}").split("\n"))
	return pingTimes
	#return re.findall("time=(\d+)", ping)
	#return re.findall("time=([0-9\.]+)", ping)


def onlyPackets(ping):
	pingPackets = commands.getoutput("echo \""+ping+"\" | grep received | awk -F ' ' {'print $1 \" \" $4'}").split(" ")
	return pingPackets
	#return list (re.findall("(\d+) packets transmitted, (\d+) received", ping)[0])