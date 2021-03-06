#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

# AF_INET == ipv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object

host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print( 'Got connection from', addr)
   c.send(b'Thank you for connecting')
   c.close()                # Close the connection