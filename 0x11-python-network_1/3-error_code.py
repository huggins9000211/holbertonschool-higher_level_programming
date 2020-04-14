#!/usr/bin/python3
""" test """
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import urllib.error
    import sys
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf8')
            print(html)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
