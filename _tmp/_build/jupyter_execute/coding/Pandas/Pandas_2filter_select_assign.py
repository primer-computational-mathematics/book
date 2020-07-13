# Filtering, selecting and assigning
``` {index} Pandas: filtering
```
Let's look at New Zealand earthquake data:

import pandas as pd
nz_eqs = pd.read_csv("../../geosciences/data/nz_largest_eq_since_1970.csv")
nz_eqs.head(4)

We would like to filter it, so that we only use earthquakes since 2000 and with magnitude higher than 5. To do that, we can include a conditional expression:

nz_eqs_2 = nz_eqs[(nz_eqs.year >= 2000) & (nz_eqs.mag >= 5.0)]
nz_eqs_2.shape

This operation reduced our DataFrame to 544 rows from 25,000. The symbol & is used for AND condition, while symbol | can be used for OR condition.

``` {index} Pandas: selecting
```

If we want to pick specific rows and colums we can use syntax:
    
    df.iloc[row_start:row_end:step, column_start:column_end:step]
where both row end and column end are not included.

nz_eqs.iloc[1:12:3, 6:9]

Pandas' built-in function .isin([list of values we look for]) allows us to select data whose specified values are in the given column. This function returns True/False. Isin can be used with:
    
    df.loc[df.col1.isin([value1, value2, ...])]
    
It will return a DataFrame filtered by the isin condition:

nz_eqs2 = nz_eqs.loc[nz_eqs.year.isin([2000])]
nz_eqs2.head()

Another built-in selectors are .isnull([list of values we look for]) and .notnull([list of values we look for]). These selectors look for either 'NaN' or not 'NaN' values.

``` {index} Pandas: assigning
```
If we want to create a new column, e.g. with depth in m, we can easily assign value to a new column:

nz_eqs["depth_m"] = nz_eqs["depth_km"]*1000
nz_eqs.head()

These calculations are done at once for each row. That means that there is no need to loop over elements in the DataFrame, which makes it very efficient!

# References
The notebook was compiled based on:
* [Pandas official Getting Started tutorials](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)
* [Kaggle tutorial](https://www.kaggle.com/learn/pandas)