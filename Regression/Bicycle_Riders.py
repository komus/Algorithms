import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar

"""
   Objective:

Predict bike traffic for each day;
Explain which features affect the number of cyclists most;
Tips:

Use weather dataset for feature engineering.
Engineer additional features such as: weeekday, daylight_hrs, is_holiday, temp_celcius, is_dry_day, explain why.
"""

counts = pd.read_csv('https://data.seattle.gov/api/views/65db-xm6k/rows.csv', index_col='Date', parse_dates=True)
weather = pd.read_csv('https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/BicycleWeather.csv',  index_col='DATE', parse_dates=True)

daily = counts.resample("d").sum()

cal = USFederalHolidayCalendar()
holidays = cal.holidays('2012', '2016')
daily = daily.join(pd.Series(1, index=holidays, name='holiday'))
daily['holiday'].fillna(0, inplace=True)
