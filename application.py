#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

while True:
	p = subprocess.Popen(['python','collector.py'], stdout=subprocess.PIPE)
	p.wait()
	print p.communicate()[0]