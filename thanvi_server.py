from http.server import BaseHTTPRequestHandler, HTTPServer
import html
import re
from pathlib import Path


class ThanviWebApp:
    def __init__(self, source):
        self.source = source
        self.app_name = "Thanvi WebApp"
        self.routes = {}

    def parse(self):
        app_match = re.search(
            r'app\s+"([^"]+)"',
            self.source
        )

        if app_match:
            self.app_name = app_match.group(1)

        route_pattern = re.compile(
            r'route\s+"([^"]+)"\s*\{(.*?)\}',
            re.DOTALL
        )

        for match in route_pattern.finditer(self.source):
            path = match.group(1)
            body = match.group(2)

            page = {
                "title": self.app_name,
                "heading": "",
                "text": "",
                "button": ""
            }

            title = re.search(r'title\s+"([^"]+)"', body)
            heading = re.search(r'heading\s+"([^"]+)"', body)
            text = re.search(r'text\s+"([^"]+)"', body)
            button = re.search(r'button\s+"([^"]+)"', body)

            if title:
                page["title"] = title.group(1)

            if heading:
                page["heading"] = heading.group(1)

            if text:
                page["text"] = text.group(1)

            if button:
                page["button"] = button.group(1)

            self.routes[path] = page

        return self

    def render(self, path):
        page = self.routes.get(path)

        if page is None:
            return self.not_found(path)

        button_html = ""

        if page["button"]:
            if page["button"].lower() == "home":
                button_html = '<a href="/" class="button">Home</a>'
            elif page["button"].lower() == "get started":
                button_html = '<a href="/about" class="button">Get Started</a>'
            else:
                button_html = (
                    f'<button class="button">'
                    f'{html.escape(page["button"])}'
                    f'</button>'
                )

        return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(page["title"])}</title>

<style>
* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: #0f172a;
    color: white;
}}

.container {{
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 30px;
}}

.card {{
    max-width: 800px;
    width: 100%;
    padding: 50px;
    text-align: center;
    border-radius: 24px;
    background: #1e293b;
    box-shadow: 0 20px 60px rgba(0,0,0,.35);
}}

h1 {{
    font-size: 48px;
    margin-bottom: 20px;
}}

p {{
    font-size: 20px;
    line-height: 1.6;
    color: #cbd5e1;
}}

.button {{
    display: inline-block;
    margin-top: 25px;
    padding: 14px 26px;
    border: 0;
    border-radius: 10px;
    background: #2563eb;
    color: white;
    text-decoration: none;
    font-size: 16px;
    cursor: pointer;
}}

.button:hover {{
    opacity: .85;
}}
</style>
</head>

<body>
<div class="container">
    <div class="card">
        <h1>{html.escape(page["heading"])}</h1>
        <p>{html.escape(page["text"])}</p>
        {button_html}
    </div>
</div>
</body>
</html>
"""

    def not_found(self, path):
        return f"""<!DOCTYPE html>
<html>
<head>
<title>404 - ThanviLang</title>
</head>
<body style="font-family:Arial;text-align:center;padding:80px">
<h1>404</h1>
<p>Route {html.escape(path)} was not found.</p>
<a href="/">Go Home</a>
</body>
</html>
"""


def run_thanvi_webapp(filename="examples/webapp.thanvi", port=8000):
    source = Path(filename).read_text(encoding="utf-8")

    app = ThanviWebApp(source)
    app.parse()

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            content = app.render(self.path)

            data = content.encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()

            self.wfile.write(data)

        def log_message(self, format, *args):
            print(f"[ThanviWebApp] {args[0]}")

    server = HTTPServer(("0.0.0.0", port), Handler)

    print()
    print("===================================")
    print("       ThanviLang WebApp 2.0")
    print("===================================")
    print(f"App: {app.app_name}")
    print(f"Server: http://localhost:{port}")
    print("Press CTRL+C to stop.")
    print()

    server.serve_forever()


if __name__ == "__main__":
    run_thanvi_webapp()
