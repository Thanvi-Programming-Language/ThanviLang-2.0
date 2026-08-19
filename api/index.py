from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(b"""
        <html>
        <head>
            <title>ThanviLang 2.0</title>
        </head>
        <body>
            <h1>Welcome to ThanviLang 2.0</h1>
            <p>Thanvi Programming Language WebApp</p>
            <p>Python-based development runtime</p>
        </body>
        </html>
        """)
