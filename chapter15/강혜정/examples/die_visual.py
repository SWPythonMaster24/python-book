import plotly.express as px

from die import Die

# 6면체 주사위를 만듭니다
die = Die()

# 몇 회 굴린 결과를 리스트에 저장합니다
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 결과를 분석합니다
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 결과를 시각화합니다
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()