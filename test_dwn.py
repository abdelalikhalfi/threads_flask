from urlparse import urlparse

url = "http://www.google.com/sfgfgfgf"

parsed_url = urlparse(url)

print(parsed_url.netloc)
