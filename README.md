# DotaAnalysis
Data visualization and analysis of DotA 2 matches and heros.

The goal of this project was to fetch data from an existing API and explore the data using MySQL, Pandas, Matplotlib and Seaborn. Also to possibly gain insight on my DotA career and what decisions I can make to influence a WIN, cause losing sucks.

All of my match/hero data was gathered from OpenDota, an open-source data platform that gets its data directly from Steam. OpenDota provides an API for users to build their own applications with. The data I'll be working with comes from two GET requests to the API; one for my match data, and one for general hero data. I loaded this data into a MySQL database and exported it into two CSV files - one with my match data joined with hero data and one with the hero data on its own - which I'll work with using Python's Pandas module.

All of my visualization and analysis lies in the data_structuring.ipynb(Jupyter Notebook). The MySQL setup folder works to set the tables. The Three mysql.py files are python scripts to formulate the data fetched from OpenDota. The three CSV files are where I created my Pandas Dataframe.
