# Jinja2ライブラリとPyYAMLを読み込みます
from jinja2 import Environment, FileSystemLoader
import yaml

# テンプレートの環境を表すオブジェクト
ENV = Environment(loader=FileSystemLoader('.'))

def get_interface_speed(interface_name):
    """ インタフェース名に含まれるキーワードを元に
    インタフェースのデフォルトの通信速度をメガビット毎秒単位で返します
    """

    if 'gigabit' in interface_name.lower():
        return 1000
    if 'fast' in interface_name.lower():
        return 100

# ENVオブジェクトを宣言した後に、フィルターを追加します。
# フィルターを表すget_interface_speed関数自体を渡しており、
# ここで関数を呼び出しているわけではありません。
# template.render()が呼び出されたタイミングで
# テンプレートエンジンによってget_interface_speedが実行されます
ENV.filters['get_interface_speed'] = get_interface_speed
template = ENV.get_template("template_3.j2")

# YAMLファイルを読み込み、テンプレートに渡して出力を行います
with open("data.yml") as f:
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)
    print(template.render(interface_list=interfaces))