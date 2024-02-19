import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.GnBu, s=10)

# 그래프 타이틀을 지정하고 축에 이름표를 붙입니다
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 틱 이름표 크기를 지정합니다
ax.tick_params(labelsize=14)

plt.show()