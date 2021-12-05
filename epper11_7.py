def solution(arr):
    	ans=0
	n=len(arr)
	if n==1:
		ans=arr[0]
		return ans
	arr.sort()##오름차순정렬(12345)
#  for i in range(n-1):
# 		for j in range(1,n-1):
# 			if arr[j]>arr[j+1]:
# 				arr[j],arr[j+1]=arr[j+1],arr[j]
	ans=(arr[0]+arr[1])/2
	for i in range(2,n):
		ans=(ans+arr[i])/2##가장작은수부터 더해서 평균만들기시작해야 가장 큰 평균값 나옴
	return ans
n=int(input())
arr=[]
for i in range(n):
	x=int(input())
	arr.append(x)
print("%.6f"%solution(arr))##소숫점6자리까지 출력
