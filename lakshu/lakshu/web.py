<table>
    <thead>
        <tr>
            <th>Rank</th>
            <th>Company</th>
            <th>Revenue (in billions)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>Walmart</td>
            <td>$559.15</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Github</td>
            <td>$550.13</td>
        </tr>
        <tr>
            <td>3</td>
            <td>MongoDB</td>
            <td>$384.23</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Dropbox</td>
            <td>$379.13</td>
        </tr>
        <tr>
            <td>5</td>
            <td>DataDog</td>
            <td>$352.11</td>
        </tr>
    </tbody>
</table>
""" class myhandler(BaseHTTPRequestHandler): def do_GET(self): print("request received") self.send_response(200) self.send_header('content-type', 'text/html; charset=utf-8') self.end_headers() self.wfile.write(content.encode()) server_address = ('',8000) httpd = HTTPServer(server_address,myhandler) print("my webserver is running...") httpd.serve_forever()