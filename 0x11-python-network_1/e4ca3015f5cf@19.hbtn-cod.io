#!/usr/bin/python3
""" test """
if __name__ == "__main__":
    import requests
    import sys
    try:
        peram = sys.argv[1]
    except Exception:
        peram = ""
    x = requests.post("http://0.0.0.0:5000/search_user", data={'q': peram})
    try:
        myJson = x.json()
    except Exception:
        print('Not a valid JSON')
