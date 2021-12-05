# def solution(s):
#     ans=''
#     n=len(s)
#     cnt=0
#     i=0
#     dic={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
#     if s[0]=='1':
#         ans='1'
#     for j in range(n):##0~n-1
#         if(s[i]==s[j]):
#             cnt+=1
#         else:
#             ans=ans+dic[cnt]
#             i=j
#             cnt=1
#     ans=ans+dic[cnt]
#     return ans
def solution(s):
    ans=''
    n=len(s)
    cnt=0
    if s[0]=='1':
        ans='1'
    for i in range(n):##0~n-1
        if(s[i]==s[i+1]):
            cnt+=1
        else:
            tmp=ord('A')+cnt##ord:문자의 아스키코드값을 돌려주는 함수
            ans=ans+chr(tmp)##chr:아스키코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
            cnt=0
    ##n번째
    tmp=ord('A')+cnt
    ans=ans+chr(tmp)
    return ans
			
s=input()
ans=solution(s)
print(ans)