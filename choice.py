#모임 공지

print("----------------------------------------------")
print("              < 모이면 싸진다 >              ")
print("----------------------------------------------")
menu=input("공구물건 (필통, 노트,  참고서  중 선택) : ")
price=5000
count=int(input("공구 인원: "))
if(count>=20):
    price=count*price*0.7
elif(count>=10):
    price=count*price*0.8
elif(count>=5):
    price=count*price*0.9
else:
    price=count*price

price=int(price)
print("--------------------------------------------------------------")
print("공구 물건:",menu,", 공구인원:",count,"명, 비용:",price,"입니다.")
print("--------------------------------------------------------------")
