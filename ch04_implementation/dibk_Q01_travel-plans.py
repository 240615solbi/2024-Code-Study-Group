'''
🍪문제 번호 :
4장 예제 문제 - 상하좌우

🍈문제 정의 :
여행가A를 NXN맵에서 이동시키는데, 입력값은 움직임(LRUD)이고 해당 입력값에 결과로 도착하는 위치(좌표)를 구하기.

🍊풀이 시간 :
20분

🍒풀이 방법 :
R,L,U,D의 딕셔너리 생성 후, 초기 값(1,1)에서 해당 입력값의 이동을 +,-한다.
*임의의 공간(배열)을 생성하지 않고 계산으로만 실행해보기.

'''
class Solution :
    def travel_plans(self) :
        
        # 이동 딕셔너리 생성
        move = {"R": [0,1],"L":[0,-1],"U":[-1,0],"D":[1,0]}
        
        # 초기값
        x,y = 1,1
        
        N = int(input("맵의 크기를 입력하기(NXN) : "))
        movement = list(map(str,input('입력하기(RLUD) : ').split()))
        
        for m in movement :
            x_,y_ = move[m]
            
            if x+x_ > N or x+x_ < 1 or y+y_ > N or y+y_ < 1:
                # 정사각형 공간을 벗어나는 움직임은 무시.
                continue
            
            x +=x_
            y +=y_
        
        print("도착 위치(좌표) : ",x,y)

test = Solution()
test.travel_plans()
