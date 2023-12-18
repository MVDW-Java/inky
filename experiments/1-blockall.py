from pyicap import Server, BaseICAPRequestHandler

class MyICAPHandler(BaseICAPRequestHandler):
    def _handle_reqmod(self):
        # Implement your safety-checking logic here
        # For simplicity, let's assume we always block the request
        self.send_response(403)
        self.send_header('ISTag', '"W3E4R5T6Y7U8I9O0"')
        self.send_header('Encapsulated', 'req-hdr=0, null-body=8960')
        self.end_headers()
        self.send('HTTP/1.1 403 Forbidden\r\nContent-Length: 0\r\n\r\n')

    def _handle_resmod(self):
        # Implement response modification logic if needed
        self.send_response(204)
        self.send_header('ISTag', '"W3E4R5T6Y7U8I9O0"')
        self.send_header('Encapsulated', 'res-hdr=0, null-body=8960')
        self.end_headers()
        self.send('')  # Empty response body

icap_server = Server(handler=MyICAPHandler)
icap_server.run()
