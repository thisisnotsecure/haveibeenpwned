#!/bin/python

import requests
import sys

if not sys.argv[0]:
    print('no argument provided')

def main():
    pwnedurl = 'https://haveibeenpwned.com/api/breachedaccount/'
    headers = {'User-Agent': 'Porridge-Checker-for-Healthy-Minds'}
    usage = ''
    email = ''
    req = requests.get(pwnedurl + email, headers=headers, verify=False)
    print(req.content)


if __name__ == "__main__":
    main()
