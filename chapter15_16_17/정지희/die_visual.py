import plotly.express as px

from die import Die

# 6면체 주사위와 10면체 주사위를 만듭니다
die_1 = Die()
die_2 = Die(10)

# 몇 회 굴린 결과를 리스트에 저장합니다
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 결과를 분석합니다
frequencies =[]
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 결과를 시각화합니다
title = "Results of Rolling One D6 and D10 50,000 Tiems"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# 추가 커스텀
fig.update_layout(xaxis_dtick=4)

# fig.show()
fig.write_html('dice_visual_d6d10.html')