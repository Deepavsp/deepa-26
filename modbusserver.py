from pymodbus3.server.sync import StartTcpServer
from pymodbus3.server.sync import StartUdpServer
from pymodbus3.server.sync import StartSerialServer

from pymodbus3.device import ModbusDeviceIdentification
from pymodbus3.datastore import ModbusSequentialDataBlock
from pymodbus3.datastore import ModbusSlaveContext, ModbusServerContext

import socket
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

store = ModbusSlaveContext(
	di = ModbusSequentialDataBlock(0, [17]*100),
	co = ModbusSequentialDataBlock(0, [17]*100),
	hr = ModbusSequentialDatablock(0, [17]*100),
	ir = ModbusSequentialDatablock(0, [17]*100))
context = ModbusServerContext(slaves=store, single=True)

StartTcpServer(context, identity=identity, address=("localhost", 502))

def main():
	host = '127.0.0.1'
	port = 502
	s = socket.socket()
	s.listen(1)
	c, addr= s.accept()
	print("Connection from: " + str(addr))
	
	while True:
		data = c.recv(1024).decode('utf-8')
		if not data:		
			break
		print("Received from client:" + data)
		data = data.upper()
		c.send(data.encode('utf-8'))

	c.close()

if __name__=="__main__":
	main()


