import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
traget_address= "127.0.0.1"
port_no = 2525
complete_address=(traget_address,port_no)
file=open("my.txt","r")
message=file.read()
while True:
    # message=input("Enter The messge: ")
    enc_message=message.encode('ascii')
    # enc_file=mydata.encode('ascii')
    user_input=input("Do want to quit:")
    if user_input =="Y" or user_input =="y":
     False
    else:
       s.sendto(enc_message,complete_address)