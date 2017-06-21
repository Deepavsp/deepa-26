from pyModbusTCP.client import ModbusClient
import socket

#try: 	c = ModbusClient(host="localhost", port = 502, auto_open=True, auto_close=True)
#except ValueError:
#	print ("Error with host or port parameters")

def main():

	host="127.0.0.1"
	port=502

	s=socket.socket()
	s.connect((host,port))

	message=input("->")

	while message != 'close':
		s.send(message.encode('utf-8'))
		data = s.recv(1024).decode('utf-8')
		print("Received from server: " + data)
		message = input("->")
	
	s.close()

if __name__=="__main__":
	main()

#while True:
#	if c.is_open():
#		regs_list_1 = c.read-holding_registers(0, 10)
#		regs_list_2 = c.read_holding_resgisters(55, 10)
#	else:
#		c.open()
#	time.sleep(1)

#c = ModbusClient (host ="localhost", port = 502, debug= True)

#c.read_holding_registers(0, 4)
