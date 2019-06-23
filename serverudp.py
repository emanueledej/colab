import socket
HOST = '192.168.0.111'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
client1=''
client2=''
msg1=''
msg2=''
while (client1=='' or client2 ==''):
  msg, cliente = udp.recvfrom(1024)
  if client1 == '' :
    client1=cliente
    msg1=msg
    print(cliente, msg)
  
  if client2 == '' and cliente != client1:
    client2=cliente
    msg2=msg
    print(cliente, msg)

while (client1!='' and client2 !=''):
  udp.sendto('ping'.encode(),client2)
  udp.sendto('pong'.encode( ),client1)

udp.close()