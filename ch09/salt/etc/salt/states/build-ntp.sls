build_config:
  file.managed:
    - name: /home/admin/ntp_generated.conf
    - source: salt://ntp_template.j2
    - template: jinja