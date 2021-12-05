def solution(S,E,n):
    ans=0
    e1=e2=-1##e1, e2: 각 자리 의미
	##학생들을 종료시간 빠른 순으로 정렬
    for i in range(n):##0~n-1
        for j in range(n-1):##0~n-2 -> j+1이 인덱스 n-1이 될때가 끝이니까
            if(E[j]>E[j+1] or (E[j]==E[j+1] and S[j]>S[j+1])):##끝나는시간이 같은 경우에는 시작시간이 더 빠른 순서대로
				## 버블정렬(이중포문i,j -> j와 j+1 비교 후 바꾸기)
				## 현재학생과 다음학생의 시간들을 바꿔줌 ->종료시간 빠른 순으로 정렬됨
                S[j],S[j+1]=S[j+1],S[j]
                E[j],E[j+1]=E[j+1],E[j]##시작/종료 모두 swap
    ##greedy algo사용
    for i in range(n):##학생 수(n)만큼 반복
        if e1<=S[i]:##1번자리가 비었다면 학생 할당
            e1=E[i]##1번자리의 학생의 종료시간 대입
            ans+=1##학생 1명 할당 ->ans 더해주기
        elif e2<=S[i]:##2번자리가 비었다면 학생 할당
            e2=e1##1번 자리의 값을 2번으로 대입하여 이미 자리에 할당된 학생의 종료시간 
            e1=E[i]##1번자리에 학생의 종료시간 대입 왜? 이 2줄 대신 그냥 e2=E[i]하면 안되는 이유가 뭘까
            ## 1번자리가 먼저 비어있는지 체크하기 때문에 ....(?).애초에 종료 빠른 순으로정렬되어있어서 1번보다 2번이 늦게끝남
            ## 가장 늦은 종료시간(2번)을 먼저 체크해주고 다음번자리로 넘어와야함(greedy)
            ## 2번자리는 기존 1번자리 학생의 종료시간을 저장
            ## 그 후 1번자리에 학생을 배정
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
	