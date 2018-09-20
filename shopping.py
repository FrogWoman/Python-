# coding: utf-8

money = 1000
RedBull_price = 200

print("----- いらっしゃいませ ----")
print("あなたの所持金は"+str(money)+"円です")
input_count = input("RedBullを何個お買い求めですか? : ")
count = int(input_count)

total_price = RedBull_price*count

if total_price < money :
    print("RedBullを" + str(count) + "個お買い上げですね")
    print("合計で" + str(total_price) + "円です")
    print("お釣りは" + str(money-total_price) + "円です")
elif total_price == money :
    print("RedBullを" + str(count) + "個お買い上げですね")
    print("合計で" + str(total_price) + "円です")
    print("お釣りはありません")
else :
    print(str(total_price-money) + "円足りません")

print("ご利用ありがとうございました")
