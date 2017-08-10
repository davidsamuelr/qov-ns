import threading as t
import os, Queue
from qovns import getDelay, getJitter, getPacketsLoss
from decisor import calcNQM, mediaNQM, calcHandoff
from util import onlyTimes, onlyPackets

paramPing = ' -c 10 -i 0.2 '

class Monitor(t.Thread):

	def __init__(self, i, h, q):
		t.Thread.__init__(self)
		self.interface = i
		self.host = h
		self.queue = q

	def run(self):
		self.ping = os.popen('ping' + paramPing + self.host).read()
		nqmWlan = calcNQM(getDelay(onlyTimes(self.ping)), getJitter(onlyTimes(self.ping)), getPacketsLoss(onlyPackets(self.ping)))
		avg = mediaNQM(nqmWlan)
		self.queue.put(avg)

q0 = Queue.Queue()
q1 = Queue.Queue()

m0 = Monitor('WLAN0', '74.125.234.88', q0)
m0.start()

m1 = Monitor('WLAN1', '74.125.234.89', q1)
m1.start()

print calcHandoff(q0.get(), q1.get())