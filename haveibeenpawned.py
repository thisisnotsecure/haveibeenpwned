#!/bin/python

import requests
import sys
import re
import json


def main():
    try:
        if sys.argv[1]:
            #pwnedurl = 'https://haveibeenpwned.com/api/breachedaccount/'
            pwnedurl = 'https://haveibeenpwned.com/api/v2/breachedaccount/'
            headers = {'User-Agent': 'Porridge-Checker-for-Healthy-Minds'}

            with open(sys.argv[1]) as emails:
                for email in emails:
                    if re.match(r'[^@]+@[^@]+\.[^@]+', email):
                        req = requests.get(pwnedurl + email, headers=headers, verify=False)
                        print(req.content)


    except Exception as e:
        print('Please provide file with email column.')


if __name__ == "__main__":
    main()
