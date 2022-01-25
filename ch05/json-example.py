# Pythonでは、JSONを扱うための便利なツールが標準ライブラリとして提供されています
import json

# JSONファイルを読み込み、dataという名前の変数にデータを格納します
with open("json-example.json") as f:
    data = f.read()

# json.loadsを使い、JSONデータをディクショナリに変換します
json_dict = json.loads(data)

# ディクショナリに含まれるデータをprint関数で表示します
print("このJSONドキュメントは {0} 型として読み込まれます。\n".format(type(json_dict)))
print("JSONドキュメント内の item とそれに含まれる型を表示しています。")
for k, v in json_dict.items():
    print(
        "-- keyである {0} には valueとして {1} 型が含まれています。".format(str(k), str(type(v)))
    )