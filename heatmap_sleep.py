import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sleep_health.csv')

bins_s = [0, 30, 60, 90, 120, 150, 180]
labs_s = ['0–30', '31–60', '61–90', '91–120', '121–150', '151–180']
bins_q = [0, 2, 4, 6, 8, 10]
labs_q = ['1–2', '3–4', '5–6', '7–8', '9–10']

df['sb'] = pd.cut(df['screen_time_before_bed_mins'], bins=bins_s, labels=labs_s)
df['qb'] = pd.cut(df['sleep_quality_score'], bins=bins_q, labels=labs_q)

pivot = df.pivot_table(index='qb', columns='sb', values='person_id',
                       aggfunc='count', fill_value=0)
pivot = pivot.reindex(index=labs_q[::-1], columns=labs_s)

fig, ax = plt.subplots(figsize=(8, 5))
im = ax.imshow(pivot.values, cmap='Blues', aspect='auto')

for i in range(pivot.shape[0]):
    for j in range(pivot.shape[1]):
        v = pivot.values[i, j]
        if v > 0:
            ax.text(j, i, str(v), ha='center', va='center', fontsize=10, fontweight='bold')

ax.set_xticks(range(len(labs_s))); ax.set_xticklabels(labs_s)
ax.set_yticks(range(len(labs_q))); ax.set_yticklabels(labs_q[::-1])
ax.set_xlabel('Screen Time Before Bed (minutes)')
ax.set_ylabel('Sleep Quality Score')
ax.set_title('Screen Time vs. Sleep Quality')
plt.colorbar(im, ax=ax, label='Participants')
plt.tight_layout()
plt.savefig('heatmap.png', dpi=150, bbox_inches='tight')
plt.show()
