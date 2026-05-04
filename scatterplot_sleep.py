import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('sleep_health.csv')

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df['screen_time_before_bed_mins'], df['sleep_quality_score'],
           alpha=0.4, s=25, color='steelblue')

m, b = np.polyfit(df['screen_time_before_bed_mins'], df['sleep_quality_score'], 1)
x = np.linspace(5, 180, 200)
ax.plot(x, m*x+b, color='red', linewidth=2)

ax.set_xlabel('Screen Time Before Bed (minutes)')
ax.set_ylabel('Sleep Quality Score')
ax.set_title('Screen Time vs. Sleep Quality')
plt.tight_layout()
plt.savefig('scatter_plot.png', dpi=150, bbox_inches='tight')
plt.show()