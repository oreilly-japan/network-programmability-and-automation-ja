proxy:
  proxytype: napalm
  driver: nxos
  fqdn: nxos-spine1.dc.amers
  username: ntc
  password: ntc123
hostname: nxos-spine1
openconfig-bgp:
  bgp:
    global:
      config:
        as: 65001
        router_id: 172.17.17.1
