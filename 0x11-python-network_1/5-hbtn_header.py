#!/usr/bin/python3
""" test """
if __name__ == "__main__":
    import requests
    import sys
    x = requests.get(sys.argv[1])
    try:
        print(x.headers['X-Request-Id'])
    except Exception:
        pass
