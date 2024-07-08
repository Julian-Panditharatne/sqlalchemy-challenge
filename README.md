# SQLAlchemy Challenge

This challenge consists of two main parts:

1. Analyzing and Exploring Climate Data for Honolulu, Hawaii.

2. Designing a Climate App.

## Part 1: Analyzing and Exploring Climate Data

In this section, I used SQLAlchemy ORM queries, Pandas, and Matplotlib to perform basic precipitation and station data analysis and exploration of the provided climate database.

The precipitation analysis and exploration was performed in the following manner:

- I found the most recent date in the measurement table.

- Used that date to query the previous 12 months of precipitation data.

- Loaded the query results into a Pandas DataFrame, and then sorted it by 'date'.

- Plotted the results by using the DataFrame plot method.

The station data analysis and exploration was performed in the following manner:

- I designed a query to calculate the total number of stations in the dataset.

- I designed another query to find the most active stations (that is, the stations that have the most rows, i.e., the greatest number of observations/measurements).

- Another query was designed that calculated the lowest, highest, and average temperatures, filtered on the most active station found in the previous query.

- I designed one last query get the previous 12 months of temperature observation (TOBS) data, filtered on the most active station.

- The results of the final query were plotted as a histogram with twelve bins.

## Part 2: Designing a Climate App



---

## Repository Files and Folders



---

## References

*API reference — pandas 1.4.2 documentation*. (2024, April 10). Pandas Documentation. <https://pandas.pydata.org/pandas-docs/stable/reference/index.html#api>

Python Software Foundation. (2024, July 5). *datetime — Basic date and time types*. Python Documentation. <https://docs.python.org/3/library/datetime.html#>

The SQLAlchemy authors and contributors. (2024, July 6). *SQLAlchemy Documentation — SQLAlchemy 2.0 Documentation*. Docs.sqlalchemy.org. <https://docs.sqlalchemy.org/en/20/>

*User Guide — pandas 2.1.1 documentation*. (2024, April 10). Pandas Documentation. <https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html#user-guide>
