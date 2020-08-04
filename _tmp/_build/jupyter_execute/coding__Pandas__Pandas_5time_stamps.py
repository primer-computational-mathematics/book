(pandas_date_time)=
# Creating date-time stamps
``` {index} Pandas: date-time stamps
```
Let's create columns with hours, minutes and seconds from utc_time column (contains strings) in format:

    HH:MM:SS
    
by splitting the strings with a colon and creating float columns.

Let's load New Zealand earthquake data:

import pandas as pd

nz_eqs = pd.read_csv("../../geosciences/data/nz_largest_eq_since_1970.csv")
nz_eqs.head(4)

nz_eqs["hour"] = nz_eqs["utc_time"].str.split(':').str.get(0).astype(float)
nz_eqs["minute"] = nz_eqs["utc_time"].str.split(':').str.get(1).astype(float)
nz_eqs["second"] = nz_eqs["utc_time"].str.split(':').str.get(2).astype(float)

With to_datetime() function, we can easily create date time stamp used by pandas:

nz_eqs["datetime"] = pd.to_datetime(nz_eqs[['year', 'month', 'day', 'hour', 'minute', 'second']])
nz_eqs.head(4)

The datetime column is not yet recognised as index so we can simply use:

nz_eqs = nz_eqs.set_index('datetime')

This timestamp will be useful for plotting data.

# References
The notebook was compiled based on:
* [Pandas official Getting Started tutorials](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)
* [Kaggle tutorial](https://www.kaggle.com/learn/pandas)