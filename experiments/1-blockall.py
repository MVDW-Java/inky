import pyicap
from pyicap import BaseICAPRequestHandler, ICAPServer

class URLBlockerHandler(BaseICAPRequestHandler):
    def options(self):
        self.set_icap_response(200)
        self.set_icap_header('Methods', 'REQMOD')

    def reqmod(self):
        # Get the original HTTP request
        http_request = self.get_enc_req()

        # Extract the URL from the request
        url = http_request.headers.get('Host', '') + http_request.uri

        # List of blocked domains
        blocked_domains = ["example.com"]

        print("request: ", url)


        # Check if the requested URL is in the blocked domains list
        if any(domain in url for domain in blocked_domains):
            # If the URL is blocked, respond with HTTP 403 Forbidden
            self.set_icap_response(403)
            self.send_headers()
            self.send_response(b'Access to this URL is blocked')
        else:
            # If the URL is not blocked, pass the request through
            self.no_adaptation_required()

if __name__ == "__main__":
    server = ICAPServer(('127.0.0.1', 1344), URLBlockerHandler)
    try:
        print("ICAP server started on icap://127.0.0.1:1344")
        server.serve_forever()
    except KeyboardInterrupt:
        print("ICAP server stopped.")
