"""
First attempt at creating a socket server.

       ,~~.
      (  6 )-_,
 (\___ )=='-'
  \ .   ) )
   \ `-' /
~'`~'`~'`~'`~


# This is allmost a copy/paste form the client.py file
Ideas :
> Change variable names :
    - type ( allready a thing )
    - id ( same )

> Change function names :
    - send ( don't use that name it's very particular to sockets )

> Create error function to handle errors :
    - It could handle an error log file
    - Use special streams for output ( ex : stderr )
    - Have it OS dependant


"""

# Defining constants
HOST = input( "Host: " )
PORT = 8888
ENCODING = "utf8"
MAX_CONNECTION_COUNT = int( input( "User count: " ) )

# Common functions
def send(to, type, data = "", id = 0):
    to.send( ( f"{id}|{type}|{data}" ).encode( ENCODING ) )

def recv():
    return socket.recv( 1024 ).decode( "utf8" ).split('|')

import socket

# Socket creation
print( "Initializating socket..." )
my_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
my_socket.setblocking( False )

# Error handeling
try:
    my_socket.bind( (HOST, PORT) )
except socket.error as msg:
    print( f"A problem occured during binding:\n{msg}" )
    my_socket.close()

# Listening to new connection
print( f"Waitting for {MAX_CONNECTION_COUNT} user(s) to connect..." )
my_socket.listen( MAX_CONNECTION_COUNT )

# User connection variables
users = []

# Waiting for the users to connect
while len(users) < MAX_CONNECTION_COUNT:
    try:
        conn,addr = my_socket.accept()
        users.append(( conn, addr ))
        send(conn, "connection_success", len(users))
        print( f"New connection: {addr[0]}:{addr[1]}" )
    except socket.error as _:
        continue

for (conn,_) in users:
    send( conn, "users_connected" )

print( "All users are connected." )
my_socket.close()
