def solution(left,right):
    	##모든경우에서 lefr<=right여야함 그래야 올바른배열ㅇㅇ
	if(left==0 and right==0):##둘 다 쓴 경우
		return 1
	else:##하나라도 남아있는경우..이때 left<=right임
		if(left==0):##right만남은경우->한가지방법
			return 1
		elif(left<right):##right가 더많이남아있는경우
			##왼쪽괄호하나사용하고 재귀호출하는경우+오른쪽괄호하나사용하고 재귀호출하는경우
			return solution(left-1,right)+solution(left,right-1)
		else:##둘다 똑같이남아있는경우->일단 왼쪽괄호하나 사용후 재귀호출
			return solution(left-1,right)
	
n=int(input())##n쌍의 괄호배열
print(solution(n,n))
