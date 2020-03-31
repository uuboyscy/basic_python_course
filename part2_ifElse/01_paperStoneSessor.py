# 利用if/else跟電腦玩剪刀石頭布
import random

print('輸入 1. 剪刀  2. 石頭  3.布')
player = int(input())
computer = random.randint(1,3)

print('\n你出%s'%(player))
print('電腦出%s'%(computer))

if player == computer:
    print('平手')
elif player > computer and abs(player - computer) == 1:
    print('你贏了！')
elif player == 1 and computer == 3:
    print('你贏了！')
else:
    print('你輸了！')
