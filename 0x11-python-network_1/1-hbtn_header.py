#!/usr/bin/python3
""" test """
if __name__ == "__main__":
    import urllib.request
    import sys
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        header = dict(response.info())
        print(header['X-Request-Id'])
