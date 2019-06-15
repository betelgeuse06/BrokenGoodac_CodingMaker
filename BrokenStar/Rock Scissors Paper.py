import random

for i in range(5):
     num=int(input("0.가위 1.바위 2.보 중 하나를 선택하세요>>\n"))
     com=random.randrange(1,3)

     if num>2:
          print("잘못 누르셨습니다")
     elif num==com:
          print("비겼습니다")
     elif num+1==com or (num==2 and com==0):
          print("컴퓨터 승리")
     else:
          print("내가 승리")

     #내가 가위내면(num=0)-> com=1(진다),com=2(이긴다)
     #내가 바위내면 (num=1)-> com=0(이긴다), com= 2(진다)
     #내가 보 내면(num=2) -> com=1(이긴다),com=0(진다)

com=random.randrange(1,3)
print(com)
