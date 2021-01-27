import json
from posts import get_all_posts, get_single_post
from http.server import BaseHTTPRequestHandler, HTTPServer



# A class responsible for responding to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        # Check if there is a query string parameter
        if "?" in resource:

            param = resource.split("?")[1]
            resource = resource.split("?")[0]
            pair = param.split("=")
            key = pair[0]
            value = pair[1]

            return ( resource, key, value )

        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass # No route parameter exists
            except ValueError:
                pass # Request had trailing slash

        return (resource, id)

    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)

        response = {}

        # Parse UTL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        # Response from parse_url() is a tuple with 2 items
        if len(parsed) == 2:
            ( resource, id ) = parsed

            if resource == "categories":
                # if id is not None:
                #     response = f"{get_single_category(id)}"
                # else:
                #     response = f"{get_all_categories()}"
                response = f"{get_all_categories()}"
            elif resource == "comments":
                # if id is not None:
                #     response = f"{get_single_comment(id)}"
                # else:
                #     response = f"{get_all_comments()}"
                response = f"{get_all_categories()}"
            elif resource == "posts":
                if id is not None:
                    response = f"{get_single_post(id)}"
                else:
                    response = f"{get_all_posts()}"
            elif resource == "tags":
                # if id is not None:
                #     response = f"{get_single_tag(id)}"
                # else:
                #     response = f"{get_all_tags()}"
                response = f"{get_all_tags()}" 
            elif resource == "users":
                # if id is not None:
                #     response = f"{get_single_user(id)}"
                # else:
                #     response = f"{get_all_users()}"
                response = f"{get_all_users()}" 

        # Response from parse_url() is a tuple with 3 items
        elif len(parsed) == 3:
            ( resource, key, value ) = parsed

            # Stretch goal queries 

        self.wfile.write(response.encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Inititialize new post item
        new_item = None

        if resource == "categories":
            new_item = create_category(post_body)
        if resource == "comments":
            new_item = create_comment(post_body)
        if resource == "posts":
            new_item = create_post(post_body)
        if resource == "tags":
            new_item = create_tags(post_body)
        
        # Encode the item and send in repsonse
        self.wfile.write(f"{new_item}".encode())

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
