from http.client import HTTPConnection

conn = HTTPConnection("cleverprogrammer.com")

conn.request("GET", "/")

result = conn.getresponse()

# Retrieve the entire contents

contents = result.read()

print(contents) 
