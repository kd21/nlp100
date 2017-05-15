# coding: utf-8

# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．


if __name__ == '__main__':
    text = 'I am an NLPer'
    texts = text.replace(' ', '')
    words = text.split(' ')

    # character bi-gram
    c_bigrams = []
    for i in range(len(text)-3):
        c_bigrams.append(texts[i:i+2])

    # word bi-gram
    w_bigrams = []
    for i in range(len(words)-1):
        w_bigrams.append(words[i]+words[i+1])

    print('character bigram\t', c_bigrams)
    print('word bigram\t', w_bigrams)
