#!/usr/bin/python

# -*- coding: utf-8 -*-
# author:oh

'Main interface'

import daemon
import data_reader


def main():
	f = 'datafile.txt'
	
	with daemon.Daemon():
		data_reader.File_Watcher().boot(f)
	
	print('sen gör vi massa skit')


if __name__ == '__main__':
	main()
