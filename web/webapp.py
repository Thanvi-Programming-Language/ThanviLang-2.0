from http.server import BaseHTTPRequestHandler, HTTPServer


HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Thanvi WebApp</title>

    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #070b14;
            color: white;
        }

        nav {
            padding: 20px;
            border-bottom: 1px solid #263246;
        }

        nav a {
            color: #5ee7ff;
            margin-right: 20px;
            text-decoration: none;
        }

        .hero {
            text-align: center;
            padding: 100px 20px;
        }

        h1 {
            font-size: 60px;
            color: #5ee7ff;
        }

        p {
            color: #aab7ca;
            font-size: 18px;
        }

        button {
            padding: 14px 25px;
            border: 0;
            border-radius: 8px;
            background: #5ee7ff;
            cursor: pointer;
            font-weight: bold;
        }

        .features {
            display: flex;
            justify-content: center;
            gap: 20px;
            padding: 40px 20px;
            flex-wrap: wrap;
        }

        .card {
            width: 250px;
            padding: 25px;
            background: #101827;
            border: 1px solid #263246;
            border-radius: 12px;
        }

        footer {
            text-align: center;
            padding: 40px;
            color: #718096;
        }
    </style>
</head>

<body>

<nav>
    <b>ThanviLang</b>
    <br><br>

    <a href="/">Home</a>
    <a href="/docs">Docs</a>
    <a href="/github">GitHub</a>
</nav>

<section class="hero">
    <h1>Build with Thanvi</h1>

    <p>
        Create modern web applications using Thanvi.
    </p>

    <button>Get Started</button>
</section>

<section class="features">

    <div class="card">
        <h2>Simple</h2>
        <p>Clean and readable Thanvi syntax.</p>
    </div>

    <div class="card">
        <h2>WebApp</h2>
        <p>Build websites and web applications.</p>
    </div>

    <div class="card">
        <h2>Modern</h2>
        <p>Designed for modern developers.</p>
    </div>

</section>

<footer>
    © 2026 Thanvi Programming Language
</footer>

</body>
</html>
"""


class ThanviHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)

        self.send_header(
            "Content-Type",
            "text/html; charset=utf-8"
        )

        self.end_headers()

        self.wfile.write(
            HTML.encode("utf-8")
        )


def start_server(
    host="127.0.0.1",
    port=8080
):
    server = HTTPServer(
        (host, port),
        ThanviHandler
    )

    print(
        f"Thanvi WebApp running at "
        f"http://{host}:{port}"
    )

    server.serve_forever()


if __name__ == "__main__":
    start_server()
