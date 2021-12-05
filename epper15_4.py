def solution(numbers):
    ans=[]
    sumn=0
    for i in range(9):
        sumn+=numbers[i]
	for i in range(8):
            for j in range(i+1,9):
                if (sumn-numbers[i]-numbers[j]==100):
                    numbers[i]=-1
                    numbers[j]=-1
	for i in range(9):
            if(numbers[i]!=-1):
                ans.append(numbers[i])
	return ans
numbers = list(map(int, input().split()))##리스트로 int 형식으로 ' '로 나눠서 한번에 입력받기
r=solution(numbers)
for i in range(7):##0~6
	print(r[i],end=' ')