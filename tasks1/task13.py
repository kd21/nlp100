# coding: utf-8

# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．
# paste task12result/col1.txt task12result/col2.txt

if __name__ == '__main__':
    data_dir = 'task12result'
    with open(data_dir + '/' + 'col1.txt', 'r') as rf1, open(data_dir + '/' + 'col2.txt', 'r') as rf2:
        col1and2_text = []
        for line1, line2 in zip(rf1.readlines(), rf2.readlines()):
            col1and2_text.append(line1.replace('\n', '') + '\t' + line2)

    save_dir = 'task13result'
    with open(save_dir + '/' + 'col1and2.txt', 'w') as wf:
        wf.writelines(col1and2_text)
