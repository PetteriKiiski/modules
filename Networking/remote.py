class Remote:
	def __init__(self, ip, port):
		self.address = (ip, port)
	def send_data():
		SizeStruct = struct.Struct("!I")
		info = pickle.dumps(data)
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect(self.address)
			sock.sendall(SizeStruct.pack(len(info)))
			sock.sendall(info)
			sock.close()
		except socket.error as err:
			print (err)
class Receiver(socketserver.StreamRequestHandler):
	def handle(self)
#class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):pass
#class RequestHandler(socketserver.StreamRequestHandler):
#	def handle(self):
#		try:
#		SizeStruct = struct.Struct('!I')
#		size_data = self.rfile.read(SizeStruct.size)
#		size = SizeStruct.unpack(size_data)
#		size = size[0]
#		data = pickle.loads(self.rfile.read(size))
#		print (data[0])
#		print (CallDict[data[0]])
#		print ((self, *data[1:]))
#		with CallLock:
#			reply = CallDict[data[0]](self, *data[1:])
#		print (reply)
#		reply = pickle.dumps(reply, 3)
#		print (reply)
#		self.wfile.write(SizeStruct.pack(len(reply)))
#		self.wfile.write(reply)
#		except Exception as err:
#			print ('HANDLE ERROR:', err)
#			sys.exit(1)
#	def write(self, text, ip):
#		global messages
#		messages += [[ip, text]]
#	def read(self, ip):
#		rval = []
#		for message in messages[:]:
#			if message[0] == ip:
#				continue
#			rval += [message[1]]
#			del messages[messages.index(message)]
#		return rval
#	def online(self, id, isOnline):
#		online[id] = isOnline
#	def is_online(self, id):
#		return online[id]
