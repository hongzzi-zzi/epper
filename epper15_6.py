####testcase: 통과 : 오답
def solution(m,numstr):
    ans=0
    stk=[]
    numlist=numstr.split()
    # print (numlist)
    for i in numlist:
        if(i.isdigit()):##isdigit() 함수는 단일 글자가 '숫자' 모양으로 생겼으면 무조건 True/isdecimal() 함수는 주어진 문자열이 int형으로 변환이 가능한지 알아내는 함수/isnumeric() 함수는 숫자값 표현에 해당하는 문자열까지 인정
            stk.append(i)
        else:
            n2=int(stk.pop())
			# if len(stk)==0:
            if not stk:##스택이 비어있으면
                n1=ans
            else:
                n1=int(stk.pop())
                if i=='+':
                    ans=n1+n2
                elif i=='-':
                    ans=n1-n2
                elif i=='*':
                    ans=n1*n2
                elif i=='/':
                    ans=n1/n2
    return int(ans)
	
m=int(input())
numstr=input()
r=solution(m,numstr)
print(r)