"""

       ,~~.
      (  6 )-_,
 (\___ )=='-'
  \ .   ) )
   \ `-' /
~'`~'`~'`~'`~
"""

# Defining constants
HOST = "192.168.43.137"
PORT = 8888

import socket

# Socket creation
print( "Creating socket ..." )
my_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# Error handeling
try:
    my_socket.connect( (HOST, PORT) )
except socket.error as msg:
    print("A problem occured during connection:\n{}".format( msg ))

print( "Connection success..." )

quitting = False
while not(quitting):
    data = input().encode("utf8")
    my_socket.send(data)
    if data == "QUIT": quitting = True

print( "Stopping the connection..." )

my_socket.close()
