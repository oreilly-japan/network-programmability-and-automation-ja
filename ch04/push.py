#!/usr/bin/env python3.9

def get_commands(vlan, name):
    """VLAN設定のためのコマンドを取得します。

    引数：
        vlan (int): VLAN ID
        name (str): VLAN名

    戻り値：
        コマンドのリストが返されます。
    """
    
    commands = []
    commands.append('vlan ' + vlan)
    commands.append('name ' + name)
    return commands

def push_commands(device, commands):
    print('Connecting to device: ' + device)
    for cmd in commands:
        print('Sending command: ' + cmd)

if __name__ == "__main__":

    devices = ['switch1', 'switch2', 'switch3']

    vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},
             {'id': '30', 'name': 'WLAN'}]

    for vlan in vlans:
        vid = vlan.get('id')
        name = vlan.get('name')
        print('')
        print('CONFIGURING VLAN:' + vid)
        commands = get_commands(vid, name)
        for device in devices:
            push_commands(device, commands)
            print('')