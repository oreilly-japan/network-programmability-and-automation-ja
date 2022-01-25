from jinja2 import Environment, FileSystemLoader
import yaml

ENV = Environment(loader=FileSystemLoader('.'))

template = ENV.get_template("template.j2")

with open("data.yml") as f:
    interfaces = yaml.load(f)
    print(template.render(interface_list=interfaces))