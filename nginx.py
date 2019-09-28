#!/usr/bin/python

## Importing the subprocess library to run shell commands via python.

import subprocess
import os

'''
	Checking if the nginx process is running using the following command
	(and storing its output in a dict);
'''
command="ps -A | grep nginx"
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output, error = process.communicate()
try:

	## Status = 0 if nginx is running and vice versa
	if output:
	   print('nginx is running:\n'+output)

	else:
	    print('nginx is not running' + error)

	    ## Starting nginx
	    os.system("service nginx start")
            print('nginx is now running.')
except Exception as error:
	print('An error occured while trying to check if nginx was running: ' + error)
