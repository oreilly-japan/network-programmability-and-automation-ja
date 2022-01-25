from pyeapi import connect_to

if __name__ =="__main__":

    device = connect_to('eos-spine1')
    rsp = device.enable('show vlan brief')
    vlans = rsp[0]['result']['vlans']

    print('{:12}{:<10}'.format('VLAN ID', 'NAME'))
    for vlan_id, config in vlans.items():
        print('{:<12}{:<10}'.format(vlan_id, config['name']))
