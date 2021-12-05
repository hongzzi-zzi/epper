def solution(arr, start, end):
    	global ans
	if start==end or start>end:##수정핦필요없음
		return ans
	if(arr[start]==arr[end]):##대칭->다음원소확인(재귀호출)
		return solution(arr,start+1,end-1)
	else:##대칭 아닌 경우
		if arr[start]<arr[end]:##작은원소와 인접원소를 더해서 저장(start가 작은 경우)
			arr[start+1]=arr[start]+arr[start+1]
			ans+=1##수정횟수증가
			return solution(arr,start+1,end)##함수다시호출
		else:##(start가 큰 경우)
			arr[end-1]=arr[end]+arr[end-1]
			ans+=1
			return solution(arr,start,end-1)

n = int(input())
# arr = []
# arr.append(int(input())

ans = 0
arr=list(map(int,input().split()))
if len(arr)!=n:
	exit(0)
	
start = int(0)
end = int(n-1)
print(solution(arr, start, end))
