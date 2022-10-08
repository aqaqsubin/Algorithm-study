# 또리는 여름을 맞아 바닷가에서 인명 구조요원으로 일하게 되었습니다.
# 직교 좌표계로 바다를 나타내면 y좌표가 양수인 부분이 육지, 나머지는 바다입니다.
# 또리는 자연수 N에 대해 좌표 (0, N)에 위치합니다.
# 또리는 육지에서 10m/s 로 달릴 수 있고, 바다에서 5m/s 로 헤엄칠 수 있습니다.
# 단, 또리는 정수좌표에서만 입수할 수 있습니다.
# 물에 빠진 사람을 가장 빨리 도와줄 수 있는 입수 위치의 좌표를 출력하는 프로그램을 작성해주세요.
# 단, 육지와 바다에서 모두 직선으로 움직이는 게 가장 빠르다고 가정합니다.

# 예제 입력1
# 1
# 10 -5
# 예제 출력1
# 7

# 예제 입력2
# 1
# 0 -2
# 예제 출력2
# 0

# 입력값 설명
# 첫째줄에 또리의 위치를 나타내는 정수 N (1 ≤ N ≤ 100) 이 주어집니다.
# 둘째줄에 물에 빠진 사람의 좌표를 나타내는 두 정수 x, y (-100 ≤ x ≤ 100, -100 ≤ y ≤ -1) 가 주어집니다.

# 출력값 설명
# 또리가 물에 빠진 사람을 가장 빨리 도와줄 수 있는 입수 위치의 x좌표를 출력하세요.
# x는 정수여야 합니다.