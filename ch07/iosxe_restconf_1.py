#!/usr/bin/env python3.9

import json
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    auth = HTTPBasicAuth('ntc', 'ntc123')
    headers = {
        'Accept': 'application/vnd.yang.data+json',
        'Content-Type': 'application/vnd.yang.data+json'
    }

    url = 'http://ios-csr1kv/restconf/api/config/native?deep'
    response = requests.get(url, headers=headers, auth=auth)

    response = json.loads(response.text)
    print(json.dumps(response, indent=4))