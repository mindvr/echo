#!/usr/bin/env python3

import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class EchoHandler(BaseHTTPRequestHandler):
    def do_request(self):
        response_data = {
            "method": self.command,
            "path": self.path,
            "headers": dict(self.headers),
            "client_address": f"{self.client_address[0]}:{self.client_address[1]}"
        }
        body = json.dumps(response_data, indent=2).encode('utf-8')

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def __getattr__(self, name):
        if name.startswith('do_'):
            return self.do_request
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")


def run_server(port=8080):
    httpd = HTTPServer(('', port), EchoHandler)
    print(f"HTTP echo server running on port {port}")
    print("Press Ctrl+C to stop")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()


if __name__ == '__main__':
    run_server()
