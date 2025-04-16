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