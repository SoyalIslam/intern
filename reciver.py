import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address="127.0.0.1"
port_no =  2525
address = (ip_address,port_no)
s.bind(address)
while True:
   data = s.recvfrom(100)
   message = data[0]
   ip_address=data[1][0]
   message = message.decode('ascii')
   print(ip_address,">>>>>>>>",message)