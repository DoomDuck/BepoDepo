"""
       ,~~.
      (  6 )-_,
 (\___ )=='-'
  \ .   ) )
   \ `-' /
~'`~'`~'`~'`~
"""

# Defining constants
HOST = input( "Host: " )
PORT = 8888
ENCODING = "utf8"

import socket

# Socket creation
print( "Initializating socket..." )
my_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# Error handeling
try:
    my_socket.connect( (HOST, PORT) )
except socket.error as msg:
    print("A problem occured during connection:\n{}".format( msg ))
    my_socket.close()

my_socket.setblocking( False )

# Waiting for the server to retrieve the client their ID
id = -1
while id == -1:
    try:
        msg = my_socket.recv( 1024 ).decode( "utf8" ).split('|')
        if msg[0] == "0" and msg[1] == "connection_success":
            id = int( msg[2] )
    except socket.error as _:
        continue

print( "Successfully connected to the server with id {}.".format(id) )

# Common functions
def send(to, type, data):
    to.send( ( str( id ) + "|" + str( type ) + "|" + str( data ) ).encode( ENCODING ) )

def recv():
    return my_socket.recv( 1024 ).decode( "utf8" ).split('|')

# Waiting for all users to connect
waiting = True
while waiting:
    try:
        msg = recv()
        if msg[1] == "users_connected":
            waiting = False
    except socket.error as _:
        continue

print( "All users are connected." )

my_socket.close()
