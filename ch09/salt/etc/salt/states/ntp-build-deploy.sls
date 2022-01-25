generate_config:
  file.managed:
    - name: /home/admin/ntp_generated.conf
    - source: salt://ntp_template.j2
    - template: jinja
ntp_peer_example:
  netconfig.managed:
    - template_name: /home/admin/ntp_generated.conf
    - require:
      - file: /home/admin/ntp_generated.conf
