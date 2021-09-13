
import http.server
from kitty.remote import RpcClient

class MyHttpServer(http.server.HTTPServer):

    def __init__(self, server_address, handler, fuzzer):
        http.server.HTTPServer.__init__(self, server_address, handler)
        self.fuzzer = fuzzer


class MyHttpHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        http.server.BaseHTTPRequestHandler.__init__(self, request, client_address, server)


    def do_GET(self):
        resp = None
        if self.path == '/fuzzed':
            resp = self.server.fuzzer.get_mutation(stage="GET fuzzed", data={})

        if resp is None:
            resp = self.default_response()
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print('response:')
        print(resp)
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        self.wfile.write(resp)

    
    def default_response(self):
        return """
            <html>
                <head>
                    <title>Under test</title>
                </head>
            </html>
        """

def main():
    '''The fuzzer process waits on port 26007'''
    agent = RpcClient(host='localhost', port=26007)

    '''Tell the fuzzer to start fuzzing (it will trigger connections to the http server)'''
    agent.start()

    server = MyHttpServer(('localhost', 8082), MyHttpServer, agent)

    while True:
        server.handle_request()


if __name__ == '__main__':
    main()
