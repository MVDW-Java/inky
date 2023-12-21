# Created by Max van der Wolf
import socketserver

from pyicap import *

class ThreadingSimpleServer(socketserver.ThreadingMixIn, ICAPServer):
    pass

class ICAPHandler(BaseICAPRequestHandler):


    def serv_OPTIONS(self):
        self.set_icap_response(403)
        #self.set_icap_header("Methods", "RESPMOD")
        self.set_icap_header("Methods", "REQMOD")
        self.set_icap_header("Preview", "0")
        self.set_icap_header("Service", "Inky Experimental")
        self.send_headers(False)

    # TODO: Fix issue REQMOD getting "Connection reset by peer" error
    def serv_REQMOD(self):
        self.set_icap_response(403)
        print("test")

    def serv_RESPMOD(self):
        print("test")
        self.set_icap_response(403)
        self.no_adaptation_required()
        

port = 1344

server = ThreadingSimpleServer(("", port), ICAPHandler)
try:
    while 1:
        server.handle_request()
        print("server killed")
except KeyboardInterrupt:
    print("Exited")
