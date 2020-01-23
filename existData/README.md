# Exist Data

A non-public source provided data on their resting heart rate and consumption of Xanax, as recorded in their [Exist](https://exist.io) subscription.

## Question

1. Is resting heart rate correlated with the amount of Xanax consumed per day?

*Finding*

Both Pearson and Spearman correlations showed a low to moderate negative correlation between milligrams of xanax consumed per day and the recorded resting heartrate in that day.

```
Pearson
           mg-zscore  hr-zscore
mg-zscore   1.000000  -0.388441
hr-zscore  -0.388441   1.000000

Spearman
           mg-zscore  hr-zscore
mg-zscore   1.000000  -0.421702
hr-zscore  -0.421702   1.000000
```