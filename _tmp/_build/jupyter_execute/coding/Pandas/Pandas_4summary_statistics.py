# Summary statistics
``` {index} Pandas: summary stats
```
Pandas have built-in functions that can calculate simple statistics:

    df.describe()
    
For numeric data, this will return count, median, standard deviation, minimum, maximum, 25, 50 and 75 percentiles. For strings/timestamps, this will return count, unique, top and frequency.

Let's load New Zealand earthquake data:

import pandas as pd
nz_eqs = pd.read_csv("../../geosciences/data/nz_largest_eq_since_1970.csv")
nz_eqs.head(4)

nz_eqs.describe()

Pandas also has separate built-in functions that can calculate these statistics, e.g. to get mean magnitude we can simply call:

nz_eqs["mag"].mean()

For full tutorial see [Descriptive Statistics](https://pandas.pydata.org/docs/getting_started/basics.html#descriptive-statistics) chapter in Pandas documentation.

# References
The notebook was compiled based on:
* [Pandas official Getting Started tutorials](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)
* [Kaggle tutorial](https://www.kaggle.com/learn/pandas)