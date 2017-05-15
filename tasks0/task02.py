# coding: utf-8

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

if __name__ == '__main__':
    text0 = 'パトカー'
    text1 = 'タクシー'
    output_text = ''
    for letter0, letter1 in zip(text0, text1):
        output_text += letter0+letter1
        
    print(output_text)
