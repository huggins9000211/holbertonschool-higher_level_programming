#!/usr/bin/python3
""" test """
if __name__ == "__main__":
    import requests
    import sys
    x = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    try:
        print(x.text)
    except Exception:
        pass
