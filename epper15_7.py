def solution(S,E,n):##하나도이해못함
	ans=0
	i=j=tmp=e1=e2=-1##e1, e2: 각 자리 의미
	for i in range(n):##학생들을 종료시간 오름차순으로 정렬
		for j in range(n-1):##동일케이스는 시작시간 오름차순
			if(E[j]>E[j+1] or (E[j]==E[j+1] and S[j]>S[j+1])):##끝나는시간이 같은 경우에는 시작시간이 더 빠른 순서대로
				##버블정렬. 현재학생과 다음학생의 시간들을 바꿔줌
				# tmp=S[j]
				# S[j] = S[j + 1]
				# S[j + 1] = tmp
				# tmp = E[j]
				# E[j] = E[j + 1]
				# E[j + 1] = tmp
				S[j],S[j+1]=S[j+1],S[j]
				E[j],E[j+1]=E[j+1],E[j]
	for i in range(n):##학생 수(n)만큼 반복
		if e1<=S[i]:##1번자리가 비었다면 학생 할당
			e1=E[i]##1번자리의 학생의 종료시간 대입
			ans+=1##학생 1명 할당 ->ans 더해주기
		elif e2<=S[i]:##2번자리가 비었다면 학생 할당
			e2=e1##1번 자리의 값을 2번으로 대입하여 이미 자리에 할당된 학생의 종료시간 보존
			e1=E[i]##1번자리에 학생의 종료시간 대입
			ans+=1##학생 1명 할당 ->ans 더해주기
	return ans
n=int(input())
S=list(map(int, input().split()))
E=list(map(int, input().split()))##리스트로 int 형식으로 ' '로 나눠서 한번에 입력받기
if len(S)==n and len(E)==n and n>=0 and n<=1000:
	ans=solution(S,E,n)
	print(ans)
else:
	exit()
	