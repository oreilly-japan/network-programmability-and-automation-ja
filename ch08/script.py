#!/usr/bin/env python3.9
from pyeapi.client import Node as EOS
from pyeapi import connect
import yaml

def main():

    creds = yaml.load(open('credentials.yml'), Loader=yaml.SafeLoader)

    un = creds['username']
    pwd = creds['password']

    conn = connect(host='eos-npab', username=un, password=pwd)
    device = EOS(conn)

    output = device.enable('show version')
    result = output[0]['result']

    print('Arista Switch Summary:')
    print('---------------------')
    print('OS Version:' + result['version'])
    print('Model:' + result['modelName'])
    print('System MAC:' + result['systemMacAddress'])

if __name__ == "__main__": 
    main()