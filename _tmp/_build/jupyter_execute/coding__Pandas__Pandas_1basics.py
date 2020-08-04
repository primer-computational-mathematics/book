(pandas_intro)=
# Introduction

```{index} Pandas: basics
```


[Pandas](https://pandas.pydata.org/docs/) is an open source library for Python that can be used for data manipulation and analysis. If your data can be put into a spreadsheet, Pandas is exactly what you need!

Pandas is a very powerful tool with highly optimised performance. The full documentation can be found [here](https://pandas.pydata.org/docs/index.html).

To start working with pandas you can simply import it. A standard alias used for pandas is "pd":

import pandas as pd

(pandas_objects)=
## Pandas objects

**DataFrame** is a 2D data structure with columns and rows, much like a table or Excel spreadsheet. To manually create a DataFrame, we can create a dictionary of lists. The keys are used as a table header and values in each list as rows:

df = pd.DataFrame({
     "Rock_type": ["granite",
                   "andesite",
                   "limestone"],
     "Density": [2.6, 2.8, 2.3],
     "Main_mineral": ["quartz",
                      "feldspar",
                      "calcite"]})

# Use df.head() to display
# top rows
df.head()

To extract data from specific column, we can call the column name in two ways:

# First method
# Similar to calling dictionary keys
# Works for all column names
print(df["Rock_type"])

# Second method
# This will only work if the column name
# has no spaces and is not named like
# any pandas attribute, e.g. T will mean
# transpose and it won't extract a column
print(df.Rock_type)

pd.Series(["granite", "andesite", "limestone"])

(reading_files)=
## Reading files

``` {index} Pandas: reading and writing files
```
Most of the time we will want to load data in different file formats, rather than manually creating a dataframe. Pandas have a very easy syntax for reading files:

    pd.read_*
    
where * can be [csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html), [excel](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html), [html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html), [sql](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql.html) and so on. For .txt file extentions we can use

    pd.read_csv(file_name, delimiter=" ") or pd.read_fwf(file_name)
   
In this example we will look at New Zealand earthquake data in .csv format from [IRIS](https://ds.iris.edu/ieb/). With .head() we can specify how many rows to print, in this case, we want to display first 4 rows (that includes header):

nz_eqs = pd.read_csv("../../geosciences/data/nz_largest_eq_since_1970.csv")
nz_eqs.head(4)

We can check DataFrame shape by using:

nz_eqs.shape

We have 25,000 rows and 11 columns, that's a lot of data!

(writing_files)=
## Writing files

Let's say we want to export this data as an excel spreadsheet but we only want to export magnitude, latitude, longitude and depth columns:

nz_eqs.to_excel("../../geosciences/data/nz_eqs.xlsx",
                sheet_name="Earthquakes",
                columns=["mag", "lat", "lon",
                        "depth_km"])

ExcelWriter object allows us to export more than one sheet into the same file:

with pd.ExcelWriter("../../geosciences/data/nz_eqs.xlsx") as writer:
    nz_eqs.to_excel(writer, sheet_name="Earthquakes",
                   columns=["mag", "lat", "lon",
                        "depth_km"])
    nz_eqs.to_excel(writer, sheet_name="Extra info",
                   columns=["region", "iris_id",
                            "timestamp"])

# References
The notebook was compiled based on these tutorials:
* [Pandas official Getting Started tutorials](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)
* [Kaggle tutorial](https://www.kaggle.com/learn/pandas)