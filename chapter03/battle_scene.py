import random

# 自分のヒットポイント
my_hit_point = 15
# スライムのヒットポイント
slime_hit_point = 8
# こうげきの順番
# ここでは自分から攻撃するものとする
index = 0
# どちらかのヒットポイントがあるまで戦う
# ヒットポイントが0以下になると繰り返しが終わる
while slime_hit_point > 0 and my_hit_point > 0:
    # ランダムに与えるダメージを決定
    attack = random.randint(1, 7)
    # 自分とスライムが交互に攻撃をする
    if index % 2 == 0:
        print('スライムに ' + str(attack) + ' のダメージ')
        slime_hit_point -= attack
    else:
        print('ゆうしゃに ' + str(attack) + ' のダメージ')
        my_hit_point -= attack
    index += 1

# whileを抜けたらどっちかが死んでる
# 自分のヒットポイントが残ってれば、スライム撃破！
if my_hit_point > 0:
    print('スライムをやっつけた')
else:
    print('ゆうしゃは死んでしまった')
