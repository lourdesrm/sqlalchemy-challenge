# SQLAlchemy - Challenge

## What's up, Honolulu!??

![surfitup](https://www.surfertoday.com/images/stories/surfingdog.jpg)


I am going to Honolulu to celebrate my birthday. I am planning to stay in the island from 2017-07-05 to 07-07-15. But first, I want to monitor the climate to make sure I pack my bags accordingly. 

### Precipitation Analysis

-Design a query to retrieve the last 12 months of precipitation data.

-Select only the date and prcp values.

-Load the query results into a Pandas DataFrame and set the index to the date column.

-Sort the DataFrame values by date.

-Plot the results using the DataFrame plot method.

### Station Analysis


-Design a query to calculate the total number of stations.

-Design a query to find the most active stations.

-List the stations and observation counts in descending order.

-Which station has the highest number of observations?

-Design a query to retrieve the last 12 months of temperature observation data (tobs).

-Filter by the station with the highest number of observations.

-Plot the results as a histogram with bins=12.


### Finally, I will create a Flask API

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

-Use FLASK to create your routes.

- Routes


/


Home page.


List all routes that are available.

/api/v1.0/precipitation


-Convert the query results to a Dictionary using date as the key and prcp as the value.


-Return the JSON representation of your dictionary.


/api/v1.0/stations

-Return a JSON list of stations from the dataset.


/api/v1.0/tobs

query for the dates and temperature observations from a year from the last data point.

-Return a JSON list of Temperature Observations (tobs) for the previous year.


/api/v1.0/<start> and /api/v1.0/<start>/<end>


-Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.


-When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.


-When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

