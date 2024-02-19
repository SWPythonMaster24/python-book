import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 랜덤 워크를 생성합니다
rw = RandomWalk(50_000)
rw.fiil_walk()

# 랜덤 워크의 포인트를 그립니다
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=3)
ax.set_aspect('equal')

plt.show()