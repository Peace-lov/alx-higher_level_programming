#!/usr/bin/python3
""" sends a POST request and finally displays the body of the response.
Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
