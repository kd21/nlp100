# coding: utf-8

# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．


def cipher(text):
    cipher_text = ''
    for c in text:
        if c.islower():
            cipher_text += chr(219 - ord(c))
        else:
            cipher_text += c
    return cipher_text

if __name__ == '__main__':
    text = 'hogeHoge'
    print(cipher(text))
