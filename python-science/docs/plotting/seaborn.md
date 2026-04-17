# 🐍 Visualize data with Seaborn

[Seaborn](https://seaborn.pydata.org/) is built on top of Matplotlib and it makes creating certain visualisations very convenient.

```python
import seaborn as sns
```

Example

```python
plt.figure(figsize=(8,4), dpi=200)
 
ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget', 
                     y='USD_Worldwide_Gross')
 
ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions')
 
plt.show()
```

![seaborn_scattered.png](seaborn_scattered.png)

Or 

```python
plt.figure(figsize=(8,4), dpi=200)

with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data_clean,
                    x='Release_Date',
                    y='USD_Production_Budget',
                    hue='USD_Worldwide_Gross',
                    size='USD_Worldwide_Gross',)

    ax.set(ylim=(0, 450000000),
           xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')
```
![seaborn_scattered_2.png](seaborn_scattered_2.png)

Inline math: $x^2$