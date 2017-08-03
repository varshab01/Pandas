from datetime import datetime

from matplotlib import pyplot

import pandas

data = pandas.read_csv("weather_year.csv")#named the csv data

data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
               "mean_dew", "min_dew", "max_humidity", "mean_humidity",
             "min_humidity", "max_pressure", "mean_pressure",
            "min_pressure", "max_visibilty", "mean_visibility",
             "min_visibility", "max_wind", "mean_wind", "min_wind",
          "precipitation", "cloud_cover", "events", "wind_dir"]#renamed the columns 

ax = data.max_temp.plot(title = "Min and Max Temperatures")#gets the data thats under the column max temp.
data.min_temp.plot(style = "red" , ax = ax)#sets color but default is blue and takes it from min column
ax.set_ylabel("Temperature (F)")#labels
