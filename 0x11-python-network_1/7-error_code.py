#!/usr/bin/python3
""" test """
if __name__ == "__main__":
    import requests
    import sys
    x = requests.get(sys.argv[1])
    errCode = x.status_code
    if errCode >= 400:
        print("Error code: {}".format(errCode))
    try:
        print(x.text)
    except Exception:
        pass
