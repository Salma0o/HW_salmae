from http.server import CGIHTTPRequestHandler, HTTPServer
handler = CGIHTTPRequestHandler
handler.cgi_directories = ["/html.HW"]
server = HTTPServer(("localhost", 8081), handler)
server.serve_forever()
