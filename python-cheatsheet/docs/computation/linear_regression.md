# 🐍 Compute linear regression with scikit-learn

[Website](https://scikit-learn.org/stable/)

Theory info :
[linear_regression.md](../theory/linear_regression.md)


## Sample data

```python
new_films.head()
```

```python
Rank Release_Date         Movie_Title  USD_Production_Budget  \
153  2159   1970-01-01            Waterloo          25,000,000.00   
154  2270   1970-01-01        Darling Lili          22,000,000.00   
155  3136   1970-01-01              Patton          12,000,000.00   
156  3277   1970-01-01  The Molly Maguires          11,000,000.00   
157  4265   1970-01-01             M*A*S*H           3,500,000.00   

     USD_Worldwide_Gross  USD_Domestic_Gross  Domestic_Revenue  \
153                 0.00                0.00    -25,000,000.00   
154         5,000,000.00        5,000,000.00    -17,000,000.00   
155        62,500,000.00       62,500,000.00     50,500,000.00   
156         2,200,000.00        2,200,000.00     -8,800,000.00   
157        81,600,000.00       81,600,000.00     78,100,000.00   

     Worldwide_Revenue  Release_Date_Dec  
153     -25,000,000.00               197  
154     -17,000,000.00               197  
155      50,500,000.00               197  
156      -8,800,000.00               197  
157      78,100,000.00               197  
```

Our revenue linear regression will be:

$revenue=\Theta_0 + \Theta_1*budget$

where $\Theta_0$ is the _intercept_
and $\Theta_1$ is the _slope_

## Import

```python
from sklearn.linear_model import LinearRegression
```

## Create the linear regression object

```python
# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])
 
# Response Variable or Target
y = pd.DataFrame(new_films, columns=['USD_Worldwide_Gross']) 

regression = LinearRegression()

# Find the best-fit line
regression.fit(X, y)

regression = LinearRegression()

# Find the best-fit line
regression.fit(X, y)

#Theta0 intercept
regression.intercept_ #array([-8650768.00661042])

#Theta1 slope
regression.coef_ #array([[3.12259592]])

# R-squared
regression.score(X, y) #0.5577032617720403
```

How do we interpret the y-intercept? Literally, means that if a movie budget is $0, the estimated movie revenue is -$8.65 million. Hmm... so this is clearly unrealistic. Why would our model tell us such nonsense? Well, the reason is that we are specifying what the model should be ahead of time - namely a straight line - and then finding the best straight line for our data. Considering that you can't have negative revenue or a negative budget, we have to be careful about interpreting our very simple model too literally. After all, it's just an estimate and this estimate will be the most accurate on the chart where we have the most data points (rather than at the extreme left or right).

What about the slope? The slope tells us that for every extra $1 in the budget, movie revenue increases by $3.1. So, that's pretty interesting. That means the higher our budget, the higher our estimated revenue. If budgets are all that matter to make lots of money, then studio executives and film financiers should try and produce the biggest films possible, right? Maybe that's exactly why we've seen a massive increase in budgets over the past 30 years.

We see that our r-squared comes in at around 0.558. This means that our model explains about 56% of the variance in movie revenue. That's actually pretty amazing, considering we've got the simplest possible model, with only one explanatory variable. The real world is super complex, so in many academic circles, if a researcher can build a simple model that explains over 50% or so of what is actually happening, then it's a pretty decent model.


The object needs DataFrame objects so we have to create thoe