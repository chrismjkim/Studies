import random
    
length = int(input("정렬할 자료의 개수를 입력하세요. -> "))
num_array = [i for i in range(1, length+1)]

print("자료를 무작위로 섞겠습니다.")
random.shuffle(num_array)
print("자료를 무작위로 섞었습니다.")

stat_swap = 0          # 위치 교체 횟수
stat_comparison = 0    # 비교 연산 횟수

primary = [0] * length #섞어둔 초기 배열 상태 확인용
for i in range(length):
    primary[i] = num_array[i]

for i in range(1, length + 1):
    for j in range(i-1, 0, -1):
        stat_comparison += 1
        if(num_array[j]>=num_array[j-1]):
            break
        else:
            num_array[j], num_array[j-1] = num_array[j-1], num_array[j]
            stat_swap += 1
        print(num_array)
        

print("\n정렬 완료, swap 횟수 {}회, compare 횟수 {}회".format(stat_swap,stat_comparison))
print("\n초기 배열:", primary) #초기 배열 출력