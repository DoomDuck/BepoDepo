"""
First attempt at creating a socket server.

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
MAX_CONNECTION_COUNT = int( input( "User count: " ) )

# Common functions
def send(to, type, data = "", id = 0):
    to.send( ( str( id ) + "|" + str( type ) + "|" + str( data ) ).encode( ENCODING ) )

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
    print("A problem occured during binding:\n{}".format( msg ))
    my_socket.close()

# Listening to new connection
print( "Waitting for {} user(s) to connect...".format( MAX_CONNECTION_COUNT ) )
my_socket.listen( MAX_CONNECTION_COUNT )

# User connection variables
users = []

# Waiting for the users to connect
while len(users) < MAX_CONNECTION_COUNT:
    try:
        conn,addr = my_socket.accept()
        users.append(( conn, addr ))
        send(conn, "connection_success", len(users))
        print( "New connection: {}:{}".format( addr[0], addr[1] ) )
    except socket.error as _:
        continue

for (conn,_) in users:
    send( conn, "users_connected" )

print( "All users are connected." )
my_socket.close()
