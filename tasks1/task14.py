# coding:utf-8

# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．
# head -n5 hightemp.txt

import sys

if __name__ == '__main__':
    args = sys.argv
    end_line = int(args[1])
    with open('hightemp.txt', 'r') as rf:
        for line in rf.readlines()[:end_line]:
            print(line.replace('\n', ''))
