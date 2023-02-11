import random

def bubblesort(i): #정렬 1회분
    global list
    global compare
    if list[i]<=list[i+1]: #정렬되어있을 때
        global count 
        count += 1
    else: #정렬되어있지 않을 때
        global swapped
        list[i], list[i+1] = list[i+1], list[i]
        swapped += 1
    compare += 1

n = int(input("정렬할 자료의 개수를 입력하세요. -> "))
list = [i for i in range(1,n+1)]

print("자료를 무작위로 섞겠습니다.")
random.shuffle(list)
print("자료를 무작위로 섞었습니다.")

listb = [0 for i in range(n)] #섞어둔 초기 배열 상태 확인용
for i in range(n):
    listb[i] = list[i]

count = 0 #완전정렬이 되었는지 확인하는 변수
compare = 0 #비교연산 횟수
swapped = 0 #위치 바꾼 횟수

while(count!=n-1): #count=n-1까지 반복
    count = 0
    for i in range(n-1): #오른쪽 끝까지 한 번 돌기
        bubblesort(i)
        for j in range(n): #배열 출력(중간상태)
            print(list[j], end=' ')
        print("\n")

print("정렬 완료, swap 횟수 %d회, compare 횟수 %d회"%(swapped,compare))
print("초기 배열:",listb) #초기 배열 출력