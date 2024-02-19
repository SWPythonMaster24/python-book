import plotly.express as px

from die import Die

# 6면체 주사위 두 개를 만듭니다
die_1 = Die(6)
die_2 = Die(6)

# 몇 회 굴린 결과를 리스트에 저장합니다(리스트 내포 문법 활용)
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# 결과를 분석합니다(리스트 내포 문법 활용)
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_result+1)
frequencies =[results.count(value) for value in poss_results]

# 결과를 시각화합니다
title = "Results of Rolling One D6 1,000 Tiems"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# 추가 커스텀
fig.update_layout(xaxis_dtick=2)

fig.show()