# Flight Price Prediction Calculator
## Description
<p>Holidays are right around the corner. It’s time for people to put their travel plans on the calendars. Whether you’re trying to make that last minute flight for Thanksgiving dinner or planning months in advance for that beach vacation trip, what will prices look like? The goal of this project is to predict the flight price on a particular future date using a machine learning algorithm that will train historical data.</p>

## Group Members
1. Aimee Vu
2. Robert Benedict (Bobby)
3. Chris Howard
4. Heesoo Oh
5. Sarje Page
6. Jarvis Lampton
7. Juvante Gant (Vante)
8. Steven Rufus
9. Juhita Vijjali

## Datasets:
* <a href="https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction">Kaggle Flight Price Prediction</a>
* <a href="https://www.transtats.bts.gov/fuel.asp">Bureau of Transportation Statistics</a>
* <a href="https://www.eia.gov/dnav/pet/hist/eer_epjk_pf4_rgc_dpgD.htm">US Energy Information Administration</a>

## Tasks:
* Database (PostGres) - Sarje, Juhita
* Python/Jupyter/Machine Learning - Bobby, Vante, Chris
* Supervised ML
* Tableau - Vante, Steven
* Flask API - Bobby
* JavaScript - Jarvis, Aimee, Heesoo
* HTML/CSS Front-end - Aimee, Heesoo
* PowerPoint/Slide Deck - Heesoo

## ETL Process: 
The ETL process of preparing and cleaning our data was a demanding task and took up the majority of the project's duration.
  1. Took the economy and business csv raw data from Kaggle, cleaned, and concatenated the datasets together, then converted the final Data Frame to a csv.
  
  ![image](https://user-images.githubusercontent.com/91276925/204409471-e8017d12-aedd-48d0-b4fe-eb137a002d86.png)

  2. Created and set up a Postgresql (relational) database that read in our data frames from Python into several different tables based off a normalized schema
  
  ![image](https://user-images.githubusercontent.com/91276925/204409570-8f4d46f4-8075-4d2f-8d46-d0d4e968d619.png)

  3. Built out the seperate data frames that would contain the proper data for the ML model.
  
  ![image](https://user-images.githubusercontent.com/91276925/204409644-6f2aa6ec-c14b-4e30-bb9d-7009d3ee1917.png)
  
  4. Constructed final SQL query containing the specific data for our predictive-pricing ML model, read the query into Postgresql, then converted the returned query    data into a dataframe and exported the csv file.

![image](https://user-images.githubusercontent.com/91276925/204410142-f1c921cd-5a38-435b-9bf8-bcee151e8b41.png)


## Machine Learning Algorithm:
We decided to utilize the K's Nearest Neighbors Regression model to predict a price based on the various options one would prefer when looking to book a flight. 
  1. took the final csv from our data and broke our data out into the proper training and testing data sets. 
  
  ![image](https://user-images.githubusercontent.com/91276925/204410660-d730d7d3-4100-492f-b1f0-74aeb4b80203.png)
  
  2. Created the KNN model by testing various numbers of neighbors in order to find the best number in which to predict our prices with

  ![image](https://user-images.githubusercontent.com/91276925/204410867-3f829325-d8c0-4d86-95f8-e45428f1cf96.png)
 
  3. Used the fitted model to predict the value of an input sample
  
  ![image](https://user-images.githubusercontent.com/91276925/204410960-fc9a9869-c39b-4ead-9cd4-62041eb76bdf.png)

## Website Tools:
1. <a href="https://bootstrapmade.com/">BootstrapMade</a>
Design Inspiration:
<img src="assets/imgs/Inspiration.jpg">

2. <a href="https://icons.getbootstrap.com/">Bootstrap Icons</a>
3. Google Fonts
4. <a href="https://coolors.co/">Coolors</a>
5. <a href="app.py">Flask API</a>
6. <a href="assets/js">JavaScript</a>

## Tableau Visualizations
<a href="https://public.tableau.com/app/profile/gant1855/viz/FlightPredictions_16687315951740/FlightPredicitionAnaylsis3">Tableau Public Link</a>

<h4>Total Revenue per Airline by Class</h4>

<img src="Tab WB images/Viz 1.png">

<p>Sum of Price for each Flight. Colors are displayed to show details about the two classes. This visualization represents the total revenue per airline and more-so broken down per class. With economy only averaging around 15 million per fiscal year and business class averaging around 45-47 million per year.</p>

<h4>Average Monthly Revenue per Airline</h4>

<img src="Tab WB images/Viz 2.png">

<p>Count of price for each airline broken down by class. Color shows details about each airline. Details are shown for flight and the data is filtered on median of price, which includes values less than or equal to 20,000 for monthly averages per airline.</p>

<h4>Economy Class vs Business Class</h4>

<img src="Tab WB images/Viz 3.png">

<p>This visualization details are shown and broken down by flights and the per dollar amoutn for said flights that each class member takes. The data is filtered on count of <a href="Resources/Clean_Dataset.csv">Clean_Dataset.csv</a>, which includes values less than or equal to 206,666. The view is filtered by class, flight, and lastly average price.</p>

<h4>Arrival vs Departure time in each city - Delhi</h4>

<img src="Tab WB images/Viz 4.png">

<p>Arrival and departure time has been filtered and broken down to cities that passengers on a regular basis. The data is filtered on destination city, which keeps 6 of 6 airlines.</p>

<h4>Average Sale Revenue per Airline for Econ Class</h4>

<img src="Tab WB images/Viz 5.png">

<p>In this visualization, we created a bin for an absolute median price for average sale per tickets for each airline economy class. The point for this investigation was to see the vast difference and/or trends compared to business class. The plot of average of price for price (bin) is broken down by date year. Color shows details about airline. Details are shown for date year.</p>

<h4>Average Price for Airline vs Stops per Class</h4>

<img src="Tab WB images/Viz 6.png">

<p>Average of price for each airline broken down by class and stops. Color shows details about airline. The data is filtered on flight to find a correlation on price affects the number of stops for 1,561 members. Looking at the data, there are different variables that can affect each class, however the trend and amount of revenue brought in from business class and economy class are applicable.</p>