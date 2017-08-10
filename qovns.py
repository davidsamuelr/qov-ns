import math

quant = 10

def getDelay(pingTimes):
	totalTime = 0
	for i in range(0, len(pingTimes)):
		totalTime += float (pingTimes[i])
	delay = float (totalTime/len(pingTimes))
	return delay

def getJitter(pingTimes):
	jitterP = 0
	for j in range(1, len(pingTimes)):
		jitterP += math.fabs(float(float(pingTimes[j])-float(pingTimes[j-1])))
	jitter = jitterP/(int(10)-1)
	return jitter

def getPacketsLoss(pingPackets):
	loss = int (pingPackets[0]) - int (pingPackets[1])
	return loss