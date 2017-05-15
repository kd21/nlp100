# coding:utf-8

# 10. 行数のカウント
# 行数をカウントせよ．
# 確認にはwcコマンドを用いよ．
#
# shell command
# wc -l hightemp.txt

if __name__ == '__main__':
    print(len(open('hightemp.txt', 'r').readlines()))
