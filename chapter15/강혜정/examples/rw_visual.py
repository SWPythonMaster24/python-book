import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 프로그램이 실행 중이면 랜덤 워크를 계속 새로 만듭니다
while True:
    # 랜덤 워크를 생성합니다
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # 랜덤 워크의 포인트를 그립니다
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    ax.set_aspect('equal')

    # 시작점과 끝점을 강조합니다
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 축을 제거합니다
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break