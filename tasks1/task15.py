# coding:utf-8

# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．
# tail -n5 hightemp.txt

import sys

if __name__ == '__main__':
    args = sys.argv
    head_line = int(args[1])
    file_name = 'hightemp.txt'
    with open(file_name, 'r')as rf:
        for line in rf.readlines()[head_line:]:
            print(line.replace('\n', ''))
