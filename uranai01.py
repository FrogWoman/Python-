# conding: utf-8
import random

#ユーザネーム
name = input("あなたの名前 : ")

num = random.randint(0,2)

if num == 0:
  print(name + "さんの今日の運勢は良きです")
elif num == 1 :
  print(name + "さんの今日の運勢は普通です")
else :
  print(name + "さんの今日の運勢は悪きです")
