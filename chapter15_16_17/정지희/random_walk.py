from random import choice

class RandomWalk:
    """랜덤 워크를 만드는 클래스"""

    def __init__(self, num_points=500):
        """속성을 초기화합니다"""
        self.num_points = num_points

        # 이동은 (0, 0)에서 시작합니다
        self.x_values = [0]
        self.y_values = [0]

    def fiil_walk(self):
        """랜덤 워크의 각 포인트를 계산합니다"""

        # 설정한 이동 수에 도달할 때까지 움직임을 반복합니다
        while len(self.x_values) < self.num_points:

            # 방향과 거리를 정합니다
            x_step = self.get_step()

            y_step = self.get_step()

            # 움직임이 없는 결정은 버립니다
            if x_step == 0 and y_step == 0:
                continue

            # 새 위치를 계산합니다
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        """각 단계의 방향과 거리를 결정합니다"""

        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = direction * distance

        return step