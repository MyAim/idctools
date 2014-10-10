#!/usr/bin/python
import pexpect
import re
import tempfile
import threading
class distinguish_device(threading.Thread):
	def __init__(self,ip,username,password):
		threading.Thread.__init__(self)
		self.ip = ip
		self.username = username
		self.password = password
		#this function include the process of err login failed... 
		self.session_flag = 'success'
		self.device_info = 'unkonw'

	def run(self):
		self.myspawn = pexpect.spawn('telnet '+ self.ip,timeout=2)
		index = self.myspawn.expect(["login:", "Username:","(?i)Unknown host","Unknown server error",pexpect.EOF, pexpect.TIMEOUT])
	
		if index == 0:
			self.myspawn.sendline(self.username)
			self.myspawn.expect("Password:")
			self.myspawn.sendline(self.password)
		elif index == 1:
			self.myspawn.sendline(self.username)
			self.myspawn.expect("Password:")
			self.myspawn.sendline(self.password)
			i = self.myspawn.expect(['% Login failed!','>'])
			if i == 0:
				self.session_flag = 'wrong password'
				self.myspawn.close()
			else:
				self.myspawn.sendline('n')
				index2 = self.myspawn.expect([" % Incomplete command*","syntax error*"])
				if index2 == 0:
					self.device_info = "h3c"
	
		elif index == 2 or index == 3: 
			self.session_flag = 'unknown host'
		elif  index == 5 or index == 4:
			self.session_flag = 'timeout'	
			
	
	#	return device_info,myspawn,session_flag
