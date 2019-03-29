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
PORT = 8888
HOST = ""
MAX_CONNECTION_COUNT = 1

import socket

# Socket creation
print( "Creating socket ..." )
my_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )


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
    conn,addr = my_socket.accept()
    users.append(( conn, addr ))
    print( "New connection: {}:{}".format( addr[0], addr[1] ) )

go_on = True

my_socket.setblocking( False )

while go_on:
    for conn,addr in users:
        data = conn.recv( 1024 )
        msg = data.decode("utf8")
        print( msg )
        if msg == "QUIT":
            go_on = False

print( "Well done !!!" )
my_socket.close()
