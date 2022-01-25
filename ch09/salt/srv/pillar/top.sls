base:
  csr1:  # ミニオンID
    - csr1_pillar  # 割り当てられるピラー
  vmx1:
    - vmx1_pillar
  nxos-spine1:
    - nxos_spine1_pillar
  eos-spine1:
    - eos_spine1_pillar

# グレインを用いた場合
#  'G@vendor:juniper':
#    - junos
#  'G@os:ios and G@version:16*':
#    - ios_16
#  'E@(.*)-spine(\d)':
#    - spine
#
# Jinjaテンプレートを用いた場合
#{% for region in ['emea', 'amers', 'apac'] -%}
#  'N@{{ region }}':
#    - communities_{{ region }} {% endfor -%}