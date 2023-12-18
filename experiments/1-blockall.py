from icaplib import Server, Response

class MyICAPHandler:
    def __init__(self):
        pass

    def reqmod(self, icap):
        print(icap)

        icap.set_icap_response(Response.CONTINUE)
        icap.set_enc_status("HTTP/1.1 403 Forbidden")
        icap.set_enc_header("Content-Type", "text/html")
        icap.set_enc_header("Content-Length", "0")
        icap.send_headers()
        icap.send_content()
        icap.done()

    def respmod(self, icap):
        icap.done()

icap_server = Server(handler=MyICAPHandler(), port=1344)
icap_server.run()