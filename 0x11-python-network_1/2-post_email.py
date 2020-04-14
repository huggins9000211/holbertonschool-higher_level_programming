#!/usr/bin/python3
""" test """
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    datas = urllib.parse.urlencode(values)
    datas = datas.encode('utf8')
    with urllib.request.urlopen(url, data=datas) as response:
        html = response.read().decode('utf8')
        print(html)
