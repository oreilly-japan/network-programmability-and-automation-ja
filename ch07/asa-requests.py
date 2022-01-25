#!/usr/bin/env python3.9

# 送受信されるJSONオブジェクトのエンコード/デコードのためにjsonモジュールを取り込みます。
# 本スクリプトの中ではJSONオブジェクトはPythonディクショナリとして扱われますが、API呼び出し
# の際にはJSONの文字列データとして送受信されます。ネットワーク装置上のWebサーバーが解釈できる
# ように、ディクショナリを文字列に変換する必要があります。逆にJSONの文字列としてエンコードされ
# たレスポンスをネットワーク装置から受け取った場合は、Pythonでの処理のためにディクショナリへと
# 変換する必要があります。これらの処理にjsonモジュールを利用します。
import json

# requestsライブラリは、HTTPベースAPIを利用するためのものです。
# HTTPBasicAuthは、認証を簡単に行うためのヘルパー関数です。
import requests
from requests.auth import HTTPBasicAuth

# ここから先は、本スクリプトが直接呼び出された場合にのみ実行されます。
if __name__ == "__main__":

    # ヘルパー関数であるHTTPBasicAuthを使い、認証オブジェクトを生成します。ネットワーク装置
    # がBasic認証に対応している場合にこの認証オブジェクトを利用することができます。ここでは
    # authという名前をつけていますが、他の変数名と同様に、何か特別な意味があるわけではあ
    # りません。ここではrequestsライブラリで使われていた変数名と揃えるためauthという名前に
    # しています。もし仮にHTTPBasicAuthを利用しない場合には、auth=(ntc, ntc123)のように
    # 認証情報をタプルとして用意してget関数に渡すことも可能です。
    auth = HTTPBasicAuth('ntc', 'ntc123')

    # ここではAPI呼び出しの中で使われるHTTPリクエストヘッダーを定義します。
    # Content-TypeとAcceptの2つヘッダーを指定します。
    # これらヘッダーについてはPostmanを使った例でも利用しています。
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # URLを変数urlに格納することで、プログラムをモジュール化すると同時に、
    # 以降のプログラムをシンプルにします。
    url = "https://asav/api/interfaces/physical"

    # 最後にrequestsを使ってAPIを実行します。requestsライブラリでは
    # HTTPリクエストの種類ごとにそれぞれ関数が用意されています。
    # 今回はGETリクエストを実行するためにrequestsライブラリのget関数を利用します。
    # get関数では引数を4つ指定します。1つ目は必ずURLを指定する必要があり、
    # 以降の3つはキーワード引数（key=valueの形式）です。
    # キーワード引数として指定しているのはauth、headers、verifyです。
    # authとheadersについては、先ほど定義した同名の変数をそのまま渡しています。
    # verifyについては、Cisco ASAネットワーク装置では自己署名証明書を利用しており
    # 正確性を検証できないため、verifyにFalseを指定しています。
    response = requests.get(url, auth=auth, headers=headers, verify=False)