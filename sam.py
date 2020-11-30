 #式を入力させる
print("式を入力：")
x = input()

#エラー処理
def error():
 print("数字を一番先に入力してください")

#リストの添字の最初を初期化
n = 0
#リスト作成
def num():
    numlist(range(0,10,1))

#0～9のどの番号かを判別し、「number」に置き換える
while x[n] in numlist:
    x[n] = "number"
    n += 1
    break

#どの計算記号かを判別し、それぞれの文字に置き換える
def sym():
    symbol = ['+', '-', '*', '/', '=']
while x[n] in symbol:
        if x[n] == + :
            x[n] = "plus"
            n += 1
            elif  x[n] == - :
                    x[n] = "minus"
                    n += 1
                elif  x[n] == * :
                        x[n] = "multiplied"
                        n += 1
                    elif x[n] == / :
                            x[n] = "divided by"
                            n += 1
                        elif x[n] == = :
                                x[n] = "equal"
                                n += 1
                        break

    #配列の最後に「EOF」を加える
    x[n+1] = "EOF":

#結果出力
print(x):

        

