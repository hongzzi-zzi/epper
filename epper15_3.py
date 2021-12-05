def solution(n,m):
    ans=0
    while True:
        n-=1
        ans+=1
        if ans%m==0:
            n+=1
        if n==0:
            break
    return ans

n,m=map(int, input().split())##정수형으로하려고 map 사용, ' '로 구별하려고 split()사용
ans=solution(n,m)
print(ans)