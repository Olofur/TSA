#!/usr/bin/python

# -*- coding: utf-8 -*-
# author:oh

'Daemon that activates when data is appended to a file'

import os
import sys
import time
import datetime


class File_Watcher:
	def __init__(self,
		     refresh_rate=1,
		     timeout=86400):
		self.program_start_time = time.time()
		self.refresh_rate = refresh_rate
		self.timeout = self.program_start_time + timeout

	
	def set_refresh_rate(self, refresh_rate):
		self.refresh_rate = refresh_rate
		return

	
	def set_timeout(self, timeout):
		self.timeout = timeout
		return
	

	def watch_file(self, 
		       filename):
		while True:
			modify_time = os.stat(filename).st_mtime
			
			if modify_time > self.last_modify_time:	
				print('File modified!')
				# do stuff
							
			if time.time() > self.timeout:
				return
			
			self.last_modify_time = modify_time	
			time.sleep(self.refresh_rate)


	def boot(self, 
		 filename):
		self.last_modify_time = os.stat(filename).st_mtime
	
		self.watch_file(filename)


def main():
	f = 'datafile.txt'
	D = File_Watcher().boot(f)		


if __name__ == '__main__':
	main()
