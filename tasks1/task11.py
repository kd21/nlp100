# coding:utf-8

# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．
# 確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
# sed s/$'\t'/' '/g hightemp.txt
# tr '\t' ' ' < hightemp.txt
# expand -t 1 hightemp.txt

if __name__ == '__main__':
    with open('hightemp.txt', 'r') as r:
        data = r.read().replace('\t', ' ')
    print(data)
