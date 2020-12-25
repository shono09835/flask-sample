# 概要
本リポジトリはCFにおけるPython開発を簡単にまとめたものです。  
PythonではApache,PHPの設定が不要なことから.bp-configを使用しません。  
そのためcomposer相当の記述を行うだけになります。  
詳細は[公式](https://docs.cloudfoundry.org/buildpacks/python/index.html)を参照


## Pythonバージョンを指定する
Pythonランタイムのバージョンは、runtime.txtファイルに含めることで指定できます。例えば：
```
python-3.9.1
```
のようにすると固定でき
```
python-3.9.*
```
のような形にするとマイナーアップデートレベルは最新で利用ができます。

※Pythonビルドパックのリリースノートに記載されている安定した[Pythonバージョン](https://github.com/cloudfoundry/python-buildpack/releases)のみをサポートします。  

## 開始コマンドを指定する
Pythonビルドパックは、アプリのデフォルトの開始コマンドを生成しません。

Procfileに記載することで利用可能です。
```
web: python hello.py
```
```
web: gunicorn hello:app --log-file -
```

## 注意点
Flaskではデフォルトだと8080で起動することが想定されてます。
そこでCFが起動を想定するPORTを環境変数から読み取ってから起動するように修正する必要があります。
```
from flask import Flask
import os

app = Flask(__name__)
cf_port = int(os.getenv("PORT", 8080))

@app.route('/')
def hello():
    return 'Hello World.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=cf_port, debug=True)
```

## 参考
本サンプルでは上記に加えて/varsを参照することで使用中の変数を確認する箇所を加えています。  
また以下にFlaskを使う上でのノウハウが公開されているのでよければ参考にしてください。
```
https://qiita.com/yuta_h3/items/4798ec83a26391c5627f
```

