#!/usr/bin/python3
"""is a Fetches https://alx-intranet.hbtn.io/status fetches"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))

