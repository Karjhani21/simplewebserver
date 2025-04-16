# EX01 Developing a Simple Webserver
## Date:16-04-2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.
<<<<<<< HEAD
=======

>>>>>>> 22dc9406955c48c8394cd7360912d228124cccd9

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<html>
<body bgcolor="skyblue">
    <h1 align="center"><u>
          LIST OF PROTOCOLS
    </h1></u>
    <h3 align="center">NAME:KARJHANI PRIYANKA S B</h3>
    <h3 align="center">REG NO:212224040150</h3>
    <b><u>
         APPLICATION LAYER
    </b></u> 
    <ol>
    <li>HTTP-Hypertext Transfer Protocol</li>
    <li>FTP-File Tramsfer Protocol</li>
    <li>SMTP-Simple Mail Transfer Protocol</li>
    <li>SNMP-Simple Network Management Protocol</li>
    <li>DNS-Domain Name System</li>
    <li>Telnet-Telecommunications Network</li>
    </ol>

    <b><u>
         TRANSPORT LAYER
    </b></u> 
   <ol>
  <li>TCP - Tramsmission Control Protocol</li>
  <li>UDP - User Datagram Peotocal</li>
  </ol>
  <b><u>
      INTERNET LAYER
  </b></u>
  <ol>
  <li>ICMP - Internet Control Message Protocol</li>
  <li>IGMP - Intenet Group Management Protocol</li>
 <li>IPV4 - Intenet Protocol Version4</li>
 <li>IPV6 - Intenet Protocol Version6</li>
 </ol>
 <b><u>
        NETWORK ACEESS LAYER
 </b></u> 
<ol>
<li> MAC /Ethernet</li>
<li>FDDI</li>
<li>Frame Relay</li>
</ol>
</body>
</html>

'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2025-04-16 192120.png>)
![alt text](<Screenshot 2025-04-16 192133.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
