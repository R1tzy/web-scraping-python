from urllib.parse import urlparse

url = "https://www.example.com/path/page?query=123#section"
schema = urlparse(url).scheme #https
netloc = urlparse(url).netloc #www.example.com
path = urlparse(url).path #/path/page
query = urlparse(url).query #query=123
fragment = urlparse(url).fragment #section

print(schema)
print(netloc)
print(path)
print(query)
print(fragment)
