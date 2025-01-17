# 가영이와 친구들이 좀비 게임을 하고 있습니다. 좀비 게임의 규칙은 다음과 같습니다. 
# 1. 먼저 술래를 한 명 정합니다. 
# 2. 놀이가 시작되면 술래가 술래가 아닌 아이들을 쫓아다니며 몸을 터치합니다. 
# 3. 2에서 터치된 아이도 같이 술래가 됩니다. 
# 나영이는 창 밖의 아이들이 좀비 게임을 하는 것을 보며 서로 터치가 일어난 아이들을 시간 순서대로 기록했습니다. 나영이의 기록을 토대로 좀비 게임이 끝나고 술래가 총 몇 명이 되었을 지 알아내는 프로그램을 작성해주세요.
# 술래끼리 혹은 술래가 아닌 아이끼리도 터치는 할 수 있지만 이 경우에는 아무 일도 일어나지 않는다는 점에 주의해주세요.

# 예제 입력1
# 5 1
# 3
# 1 2
# 2 3
# 4 5
# 예제 출력1
# 3

# 예제 입력2
# 5 1
# 5
# 1 5
# 2 3
# 5 4
# 2 4
# 2 1
# 예제 출력2
# 4

# 입력값 설명
# 첫 번째 줄에 좀비 게임을 하는 아이들의 수를 나타내는 정수 N과 좀비 게임의 첫 술래를 나타내는 정수 A가 주어집니다. (2 ≤ A ≤ N ≤ 1,000)
# 두 번째 줄에 좀비 게임을 하는 동안 아이들끼리 터치가 일어난 횟수 M이 주어집니다. (1 ≤ M ≤ 1,000)
# 세 번째 줄부터 M개의 줄에 걸쳐서 서로 터치가 일어난 아이들의 번호가 X, Y로 주어집니다. (1 ≤ X, Y ≤ N, X ≠ Y)

# 출력값 설명
# 첫 번째 줄에 게임이 끝나고 술래가 총 몇 명인지 출력합니다.