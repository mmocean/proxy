#!/usr/bin/env python   
# -*- coding:utf-8 -*- 

#to be honest, this is not a good proxy, but it works.

import socket;  
import sys;  
  
if "__main__" == __name__:  
	if ( len(sys.argv) < 3 ):
		print("parameters error")
		exit(-1)
	else:
		listenport = sys.argv[1]	#listening prot
		host = sys.argv[2]			#remote server IP
		port = sys.argv[3]			#remote server port
	print "listenport:%s"%listenport
	print "host:%s"%host
	print "port:%s"%port

	while True:
		#server
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);  
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		#sometimes 'localhost' does not work, you should use absolute IP address
		server.bind( ('130.81.9.17', int(listenport)) )	
		server.listen( 5 )
		
		print("listen......")	
		conn, address = server.accept()
		print("accept successfully");

		#client
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM);  
		client.connect( (host, int(port)) );  
		print("connecting successfully");  

		while True:
			try:
				client.settimeout(5)
				conn.settimeout(5)
				data = conn.recv(4096)
				if data:
					print"downstream data, length:%d"%(len(data))
					client.send(data)
				else:
					print"no data, close socket"
					break
				data = client.recv(4096)
				if data:
					print"forward transfer data, length:%d"%(len(data))
					conn.send(data) 	
				else:
					print"no data, close socket"
					break
		 	except socket.timeout:   
        	    		print 'time out'   
		conn.close();
		client.close();  
		server.close();

	# 
	conn.close();
	client.close();  
	server.close();
	print("end of connecting");  


