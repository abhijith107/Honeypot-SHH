# http_honeypot.py

import http.server
import socketserver

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        with open("http_log.txt", "a") as logfile:
            logfile.write("%s - - [%s] %s\n" % (self.client_address[0], self.log_date_time_string(), format%args))


def main():
    http_port = 8080  # Choose a port for your HTTP honeypot

    # Start HTTP server
    with socketserver.TCPServer(("", http_port), HTTPRequestHandler) as httpd:
        print(f"HTTP honeypot listening on port {http_port}")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
