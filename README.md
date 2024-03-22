# EX01 Developing a Simple Webserver
## Date:29/02/2024

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
from http.server import HTTPServer, BaseHTTPRequestHandler
content ="""
```
<html>
<head>
    <h1>Top Five Companies by Revenue</h1>
</head>
<body>
   
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
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever() 

```

## OUTPUT:

![alt text](<Screenshot 2024-03-22 091829.png>)
![alt text](<Screenshot 2024-03-15 094448-1.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
