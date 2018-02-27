# 目的
DataDomain作業の効率化


# 使い方
以下の環境を想定
ホストOS: Windows10
Python: 3.6
virtualenv: 
pip: 9.0.1
Git: 2.11

mkdir git (ディレクトリはなんでも可)
cd git
git clone https://github.com/KI1208/DD-Automation.git
cd DD-Automation

virtualenv env
env\Scripts\activate
pip install -r requirements.txt

mkdir autosupport
mkdir config
mkdir proc
mkdir result
mkdir upload

python ui.py

IEでhttp://127.0.0.1:6000/にアクセス


# その他
## 使用しているライブラリ
エクセルの読み込みは、xlrd  
対抗馬は、openpyxl(2003形式NG,重い?)
pandas(未確認だが、実体はxlrd/openpyxlらしい)  
xlsxwriter(書き込みのみ)  

参考として  
http://www.python-excel.org

### xlrd

### テキストテンプレート
組み込みのTemplateモジュールを使う  
https://stackoverflow.com/questions/6385686/python-technique-or-simple-templating-system-for-plain-text-output

