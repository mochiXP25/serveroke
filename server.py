import http.server
import socketserver

PORT = 3000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    '''
    dit code block past de HTTP GET-verzoek aan, zodat wanneer het root pad verzoek
    ("/") wordt ontvangen, de site wordt omgeleid naar de 'html' folder waar het 'index.html' bestand zich bevindt.
    '''
Handler = MyHttpRequestHandler
def run():
    try:
        httpd = socketserver.TCPServer(("", PORT), Handler)
        print("Server start op localhost:" + str(PORT))
        print("druk op ctrl+c om de server te stoppen")
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
        print("Server is gestopt.")

'''
Deze functie maakt gebruik van de `socket`-library om een server 
te starten op poort 3000 en laat deze continu draaien
totdat er op CTRL+C wordt gedrukt, 
waarna de server stopt zonder de gehele code te onderbreken.'''