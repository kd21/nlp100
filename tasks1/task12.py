# coding: utf-8

# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．
# cut -f 1 hightemp.txt
# cut -f 2 hightemp.txt


def save_col_data(r_file_name, col, s_file_name):
        with open(r_file_name, 'r') as rf:
            col_text = []
            for line in rf.readlines():
                col_text.append(line.split('\t')[col] + '\n')
        with open(s_file_name, 'w') as wf:
            wf.writelines(col_text)

if __name__ == '__main__':
    dir_name = 'task12result'
    save_col_data('hightemp.txt', 0, dir_name + '/' + 'col1.txt')
    save_col_data('hightemp.txt', 1, dir_name + '/' + 'col2.txt')
