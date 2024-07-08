'''
🍪문제 번호 :
4장 실전 문제 - 게임 개발

🍈문제 정의 :
NxM배열(게임맵)에서 캐릭터가 메뉴얼에 따라 이동했을 때 방문한 칸의 수를 출력하기.
- 입력값은 N,M, 맵에서 출발 좌표, 방향(0,1,2,3), 맵지형(0,1)
- 캐릭터는 현재위치에서 해당 방향 기준으로 LDRU순으로 움직이며, 이미 가본 칸 or 바다이면 방향을 유지한 채 뒤로 1칸간다.

🍊풀이 시간 :
1시간

🍒풀이 방법 :
동서남북 방향에 대한 이동 딕셔너리를 생성하고
입력된 게임맵 배열을 활용하여 캐릭터가 방문한 공간은 3으로 표시한다.
시작좌표를 시작으로 방향for문으로 DFS 실행.

- 캐릭터가 바라보는 방향에 대한 정보 설정과 방향 딕셔너리 연결에서 헤맸다. info에 동서남북에 대한 좌표이동만 설정했는데, 추가로 해당 움직임에 대한 바라보는 방향 정보도 같이 설정하여 해결.
- 방문한 칸(visited) 개수를 확인하는 부분에 대해, local변수 설정 오류가 계속 발생하여 오류 해결에 시간이 걸렸다. 
- DFS 알고리즘에 대한 감이 떨어져서 다시 기억하는 데 시간이 걸렸다.

'''

class Solution:
    visited = 0
    def game(self):
        
        # 설정
        info = {"R": [0,1,1],"L":[0,-1,3],"U":[-1,0,0],"D":[1,0,2]}     # [x,y,방향pair숫자]
        direction = {0:'LDRU',1:"ULDR",2:'RULD',3:"DRUL"}

        # 입력
        N,M = map(int,input("NXM 입력 : ").split())
        x,y,d = map(int,input("시작 좌표, 방향 : ").split())
        
        game_map = []
        for _ in range(N) :
            game_map += list(map(int,input().split())),
        
        # 실행
        def move(row,col,int_d):
            # 현재 위치 방문 처리
            game_map[row][col] = 3
            self.visited +=1
            
            for ch in direction[int_d] :
                # ch : "L", "D",,, 방향
                x_,y_,d_ = info[ch] # 해당 방향에 대한 x,y좌표와 바라보고 있는 방향 숫자
                
                if row+x_ < 0 or row+x_ > N or col+y_<0 or col+y_ > M :
                    continue
                if game_map[row+x_][col+y_] == 3 or game_map[row+x_][col+y_] == 1 : 
                    # 바다거나 방문했다면
                    continue
                
                row += x_
                col += y_
      
                # 이동              
                move(row,col,d_)
            
            return
        
        move(x,y,d)
        print()
        print("# 결과 : ",self.visited)

test=Solution()
test.game()
        