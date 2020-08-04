(merging_combining_grouping_sorting)=
# Merging, combining, grouping and sorting
(merging)=
## Merging
``` {index} Pandas: merging
```
Let's look at New Zealand earthquake data:

import pandas as pd
import numpy as np

nz_eqs = pd.read_csv("../../geosciences/data/nz_largest_eq_since_1970.csv")
nz_eqs.head(4)

Let's create a second DataFrame that has latitude, longitude and depth (km) columns. And add an extra column with square root of depth:

nz_eqs = pd.read_csv("../../geosciences/data/nz_largest_eq_since_1970.csv")
nz_eqs.head(4)

nz_eqs2 = nz_eqs.iloc[:,5:8]
nz_eqs2["depth_sqrt"] = np.sqrt(nz_eqs2.depth_km)
nz_eqs2.head()

Now, we would like to join the original 'nz_eqs' and 'nz_eqs2' DataFrames by common columns. We can use merge function that takes two DataFrames as arguments and we can decided which columns to merge with. In our case, nz_eqs and nz_eqs2 share three data columns: lat, lon, depth_km. If we choose to merge with latitude, longitude, the final DataFrame would keep depth_km columns from both DataFrames, named depth_km_x and depth_km_y. If we wanted to merge DataFrames with all three common columns, we can use:

nz_eqs_merged = pd.merge(nz_eqs, nz_eqs2, how="left",
                         on=["lat", "lon", "depth_km"])

nz_eqs_merged.head()

(combining)=
## Combining
``` {index} Pandas: combining
```
If we want to join the same data from two tables, we can use the concat() function. Let's split the original data into two DataFrames and try to combine them back together:

# Extract two overlapping DataFrames
nz_eqs3 = nz_eqs.iloc[:15000,:]
nz_eqs4 = nz_eqs.iloc[12000:,:]

print("Shapes of two DataFrames:", nz_eqs3.shape, nz_eqs4.shape)

# Reset the index from original DataFrame
nz_eqs4.reset_index(drop=True, inplace=True)

# Concatenate DataFrames
# Use ignore_index to create a new index
nz_eqs_concat = pd.concat([nz_eqs3, nz_eqs4], ignore_index=True)

# Drop duplicates in the new DataFrame
nz_eqs_concat_unique = nz_eqs_concat.drop_duplicates()

print("Original DataFrame shape:", nz_eqs.shape)
print("Concatenated DataFrame with duplicates shape:",
      nz_eqs_concat.shape)
print("Concatenated DataFrame without duplicates shape:",
      nz_eqs_concat_unique.shape)

(grouping)=
## Grouping
``` {index} Pandas: grouping
```
If we wanted to count how many times specific regions in New Zealand were hit by an earthquake, we can use groupby() function and count():

nz_eqs.groupby('region').region.count()

This analysis is also equivalent to pandas built-in value_counts() function:

nz_eqs.region.value_counts()

We can also groupby two columns, e.g. region and year based on count, maximum and minimum depth in that year and region:

nz_eqs.groupby(['region', 'year']).depth_km.agg([len, min, max]).head()

(sorting)=
## Sorting
``` {index} Pandas: sorting
```
Groupby() function returns the values in the index order. Suppose we would like to know count of earthquakes in each year in descending order. We can use function sort_values() for that:

nz_eqs_years = nz_eqs.groupby(['year']).depth_km.agg([len, min, max])
nz_eqs_years_sorted = nz_eqs_years.sort_values(by="len", ascending=False)
nz_eqs_years_sorted.head()

# References
The notebook was compiled based on:
* [Pandas official Getting Started tutorials](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)
* [Kaggle tutorial](https://www.kaggle.com/learn/pandas)