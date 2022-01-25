import json
import sys
import requests
from requests.auth import HTTPBasicAuth

def issue_request(device, commands):
    """EOSスイッチのAPIリクエストを実行し、レスポンスをJSONとして返します"""

    auth = HTTPBasicAuth('ntc', 'ntc123')
    url = 'http://{}/command-api'.format(device)
    payload = {
        "jsonrpc": "2.0",
        "method": "runCmds",
        "params": {
            "format": "json",
            "timestamps": False,
            "cmds": commands,
            "version": 1
        },
        "id": "EapiExplorer-1"
    }

    response = requests.post(url, data=json.dumps(payload),  auth=auth)

    return json.loads(response.text)

def get_lldp_neighbors(device):
    """ネイバーのリストを取得します

    レスポンスの例として、各ネイバーは以下のように表現されます
        {
          "ttl": 120,
          "neighborDevice": "eos-spine2.ntc.com",
          "neighborPort": "Ethernet2",
          "port": "Ethernet2"
        }
    """
    commands = ['show lldp neighbors']
    response = issue_request(device, commands)
    neighbors = response['result'][0]['lldpNeighbors']

    # ネイバーを表すディクショナリのリストを返します
    return neighbors

def configure_interfaces(device, neighbors):
    """対象のネットワーク装置ごとにAPIを呼び出し、インタフェースの設定を行います
    """

    command_list = ['enable', 'configure']
    for neighbor in neighbors:
        local_interface = neighbor['port']
        if local_interface.startswith('Eth'):
            # ここではマネジメントポートは除外します。
            description = 'Connects to interface {} on neighbor {}'.format(
                neighbor['neighborPort'],
                neighbor['neighborDevice'])
            description = 'description ' + description

            interface = 'interface {}'.format(local_interface)
            cmds = [interface, description]
            command_list.extend(cmds)
    response = issue_request(device, command_list)

if __name__ == "__main__":
    # ネットワーク装置のホスト名（FQDN）
    devices = ['eos-spine1', 'eos-spine2']
    for device in devices:
        neighbors = get_lldp_neighbors(device)
        configure_interfaces(device, neighbors)
        print('{}のインタフェースを自動設定しました。'.format(device))
