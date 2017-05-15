# coding: utf-8

# 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ


def c_bigrams_set(text):
    c_bigrams = []
    for i in range(len(text)-1):
        c_bigrams.append(text[i:i+2])
    return set(c_bigrams)


def find_word(set, set_name, word):
    if word in set:
        return word + ' exist in ' + set_name
    else:
        return word + ' does not exist in ' + set_name

if __name__ == '__main__':
    text0 = 'paraparaparadise'
    text1 = 'paragraph'
    X = c_bigrams_set(text0)
    Y = c_bigrams_set(text1)
    x_and_y = X & Y
    x_or_y = X | Y
    x_diff_y = X - Y

    print('X and Y', x_and_y)
    print('X or Y', x_or_y)
    print('X diff Y', x_diff_y)
    print(find_word(X, 'X', 'se'))
    print(find_word(Y, 'Y', 'se'))
