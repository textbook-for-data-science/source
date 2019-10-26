#배달의 민족

print("----------------------------------------------")
print("                   <배달의 민족>              ")
print("----------------------------------------------")
menu=input("메뉴(치킨, 피자, 짜장 중 선택) : ")
price=10000
count=int(input("수량: "))
if(count>=10):
    price=count*price*0.7
elif(count>=5):
    price=count*price*0.8
elif(count>=3):
    price=count*price*0.9
else:
    price=count*price

price=int(price)
print("--------------------------------------------------------------")
print("주문한 메뉴:",menu,", 수량:",count,"개, 가격:",price,"입니다.")
print("--------------------------------------------------------------")

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


#시간구하기
time=13579
hour=time//(60*60)
minute=(time%(60*60))//60
second=time%60
print(time,"초는",hour,"시간",minute,"분",second,"초이다")

#이름입력

name=input("이름: ")
print(name+"님 안녕하세요?")

school=input("학교명: ")
print(school+"에 오신걸 환영합니다.")

#놀이공원 입장료
age=int(input("나이:"))
if(age<8 or age>62):
    result="무료입니다"
elif(age>=8 and age<14):
    result="1,000원입니다"
elif(age>=14 and age<62):
    result="15,000입니다"
else:
    result="다시입력하시오"
print(result)

