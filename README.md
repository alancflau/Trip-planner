# Trip planner

Do you love travelling? Do you procrastinate while scheduling your travel plans? This trip planner may be a great scheduling device for you to plan your trip.

<h3> How it works </h3>

<h4> Part 1: Retrieving data </h4>
We will be retrieving data from [google travel](https://www.google.com/search?client=firefox-b-d&sxsrf=ACYBGNS5D-TqcccpH4QA4VQuluFU92TEaQ%3A1583122697057&ei=CYlcXpCNA-amggfvxLS4Dw&q=github+adding+a+title+to+the+link+in+paragraph&oq=github+adding+a+title+to+the+link+in+paragraph&gs_l=psy-ab.3..33i160.94046.95249..95373...0.2..0.145.1373.7j6......0....1..gws-wiz.......0i71j33i22i29i30j33i21.5WLfRJycIX4&ved=0ahUKEwjQtfnP9_rnAhVmk-AKHW8iDfcQ4dUDCAo&uact=5). The driver.py module already provides the implementation of web scraping. The function inside the module, google_search, takes in one parameter that takes in a location. When calling the module, the user will call this function and enter a city location they are interested in going as one of the parameters.

<p>The script will retrieve data of the user's city attractions, ratings, categories, reviews, and a description of the attraction. The data will be represented in a dataframe.</p>

Using Selenium, Selenium requires a driver to interface with the chosen browser. The chosen browser is based on a person's preference. For more information how installation drivers, please visit this [link](https://selenium-python.readthedocs.io/installation.html).

<h4> Part 2: Data Manipulation </h4>

<p> There are some duplicate rows in the dataframe because attractions may belong into different categories. The script scrapes data based on categories; therefore some attractions will have duplicates. We will be manipulating the data such that there are no duplicates and when an attraction is shown, it will show all the possible categories it belongs. Some regular expression will be modified for cleaner representation.
  
<h4> Part 3: Feature Engineering </h4>
 
Based on the names of the attractions, we want to grab the geological location coordinates and address. In order to grab the neccessary details, we will be using the geocoding API from google. In order to use the Geocoding API, you must have an API key. For more information how to request an API key, follow this [link](https://developers.google.com/maps/documentation/geocoding/get-api-key)

<h4> Part 4: Sampling </h4>

<p> There are many ways to sample the list of attractions one wants to go. Sample a number of attractions you want to go, you may filter based on the ratings, reviews of the attractions or include certain attractions that you may want to visit during your trip. </p>

<h4> Part 5: Clustering </h4>

Based on the number of attractions and the number of days you will be spending at a city of your desire, we will perform clusters to perform the most optimal schedule. We will be using the following clustering algorithms.
- Kmeans
- DBSCAN
- HDBSCAN
- Hierarchy clustering

<p> By using multiple clustering algorithms, we can see what points belong to what clusters and depending on our time schedule, we can choose to prefer one algorithm over another. </p>




