from jinja2 import Environment, FileSystemLoader
import yaml

ENV = Environment(loader=FileSystemLoader('.'))

template = ENV.get_template("template_2.j2")

with open("data.yml") as f:
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)
    print(template.render(interface_list=interfaces))