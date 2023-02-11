import random
    
length = int(input("정렬할 자료의 개수를 입력하세요. -> "))
num_array = [i for i in range(1, length+1)]

print("자료를 무작위로 섞겠습니다.")
random.shuffle(num_array)
print("자료를 무작위로 섞었습니다.")

primary = [0] * length #섞어둔 초기 배열 상태 확인용
for i in range(length):
    primary[i] = num_array[i]

stat_swap = 0
stat_comparison = 0

for i in range(length): #i는 0~9
    target = num_array[i]
    for j in range(i+1,length): #j는 1~9
        if target>=num_array[j]: 
            target=num_array[j]
        stat_comparison += 1
    x = num_array.index(target) #최솟값이 있던 index
    num_array[x] = num_array[i]
    num_array[i] = target
    stat_swap += 1
    print(num_array)

print("\n정렬 완료, swap 횟수 %d회, compare 횟수 %d회"%(stat_swap,stat_comparison))
print("\n초기 배열:", primary) #초기 배열 출력