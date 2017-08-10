def calcNQM(delay, jitter, loss):
	return ((jitter*0.3)+(delay*0.3)+(loss*0.2))

def avgNQM(NQM):
	nSum = 0
	i = 5
	while i > 0:
		nSum = nSum + NQM
		i = i - 1
	return nSum/5

def calcHandoff(mNqmWlan0, mNqmWlan1):
	if(mNqmWlan0 > mNqmWlan1 and mNqmWlan1 > 3):
		return 'WLAN0'
	if(mNqmWlan1 > mNqmWlan0 and mNqmWlan0 > 3):
		return 'WLAN1'