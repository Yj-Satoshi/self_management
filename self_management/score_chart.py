import matplotlib.pyplot as plt
from monthly_goal.models import MonthlyGoal


fig = plt.figure()
ax = fig.add_subplot(111, xlabel='Month', ylabel='目標達成Score')

ax.plot(df['H'])
ax.plot(goal_score_ave, 'rs:', label='HR', ms=10, mew=5, mec='green')
ax.plot(goal_score_ave, marker='^', linestyle='-.')

fig.savefig('goal_score.png')
