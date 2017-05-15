# coding: utf-8

# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ
# ．ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand
#  what I was reading : the phenomenal power of the human mind ."）
# を与え，その実行結果を確認せよ．


import random

if __name__ == '__main__':
    text = "I couldn't believe that I could actually understand" \
           " what I was reading : the phenomenal power of the human mind ."
    words = text.split(' ')
    typoglycemia_text = ''
    for word in words:
        if len(word) > 4:
            word_top = word[0]
            word_bottom = ''.join(random.sample(word[1:-1], len(word[1:-1])))
            word_end = word[-1]
            typoglycemia_text += word_top + word_bottom + word_end + ' '
        else:
            typoglycemia_text += word + ' '
    print(typoglycemia_text)
