# SQLAlchemy Challenge

This challenge consists of two main parts:

1. Analyzing and Exploring Climate Data for Honolulu, Hawaii.

2. Designing a Climate App.

## Part 1: Analyzing and Exploring Climate Data

In this part, I used SQLAlchemy ORM queries, Pandas, and Matplotlib to perform basic precipitation and station data analysis and exploration of the provided climate database.

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

In this part, I designed a Flask API based on the queries developed in part 1, which involved using Flask to create the following routes:

/

- Start at the homepage.

- List all the available routes.

/api/v1.0/precipitation

- Convert the query results from the precipitation analysis (i.e. retrieving only the last 12 months of data) to a dictionary using date as the key and prcp as the value.

- Return the JSON representation of the dictionary.

/api/v1.0/stations

- Return a JSON list of stations from the database.

**/api/v1.0/tobs**:

- Query the dates and temperature observations of the most active station for the previous year of data.

- Return a JSON list of temperature observations for the previous year.

**/api/v1.0/< start >** and **/api/v1.0/< start >/< end >**:

- Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start to the most recent date in the database or a specified start-end range.

---

## Repository Files and Folders

Besides this README file, there are six other files and two folders within this repository.

The folder, which is named *SurfsUp*, contains three of the six files along with the other folder named *Resources*.

- **app.py**: The python file containing the script of the Flask API design.

- **climate.ipynb**: The jupyter notebook file containing the script run to analyze and explore the climate and station data from the SQLite Database file, **hawaii.sqlite**.

- **climate_starter.ipynb**: The jupyter notebook file containing the starter code used in the data analysis and exploration script file, **climate.ipynb**.

The *Resources* folder contains the other three files.

- **hawaii.sqlite**: The SQLite Database file containing all the climate and station data used in the **app.py** and **climate.ipynb**. script files.

- **hawaii_measurements.csv**: The csv file containing data from the measurements table of the database.

- **hawaii_stations.csv**: The csv file containing data from the stations table of the database.

---

## References

*API reference — pandas 1.4.2 documentation*. (2024, April 10). Pandas Documentation. <https://pandas.pydata.org/pandas-docs/stable/reference/index.html#api>

Python Software Foundation. (2024, July 5). *datetime — Basic date and time types*. Python Documentation. <https://docs.python.org/3/library/datetime.html#>

The SQLAlchemy authors and contributors. (2024, July 6). *SQLAlchemy Documentation — SQLAlchemy 2.0 Documentation*. Docs.sqlalchemy.org. <https://docs.sqlalchemy.org/en/20/>

*User Guide — pandas 2.1.1 documentation*. (2024, April 10). Pandas Documentation. <https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html#user-guide>
