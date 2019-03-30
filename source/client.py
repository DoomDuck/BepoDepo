"""
       ,~~.
      (  6 )-_,
 (\___ )=='-'
  \ .   ) )
   \ `-' /
~'`~'`~'`~'`~

Ideas :
> Change variable names :
    - type ( allready a thing )
    - id ( same )

> Change function names :
    - recv ( don't use that name it's very particular to sockets )

> Create error function to handle errors :
    - It could handle an error log file
    - Use special streams for output ( ex : stderr )
    - Have it OS dependant

TODOs:
> Add things to the TODOs list

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
    print( f"A problem occured during connection:\n{msg}" )
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

print( f"Successfully connected to the server with id {id}." )

# Common functions
def send(to, type, data):
    to.send( ( f"{id}|{type}|{data}" ).encode( ENCODING ) )

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
