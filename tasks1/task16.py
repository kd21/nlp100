#coding:utf-8

# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．
# split -l5 hightemp.txt > task16result/result.

import sys

if __name__=='__main__':
    args = sys.argv
    line = args[1]
    with open('hightemp.txt', 'r') as rf:
