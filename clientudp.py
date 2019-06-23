import socket
HOST = '192.168.0.111'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print('Para sair use CTRL+X\n')
while True:
  udp.sendto ('AAA'.encode(),dest)
  msgServer, server = udp.recvfrom(1024)
  print(msgServer)

udp.close()