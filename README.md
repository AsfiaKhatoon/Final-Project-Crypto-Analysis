# Cryptocurrency Analysis Project
## Introduction
The aim of this project is to have a basic understanding of the cryptocurrency, what is it? the History behind it/
Then dive into some more analysis to find top ranking cryptos from a historica dataset .
Finally with this basic understanding , find whether there is a correlation between Bitocoin, stocks (for example i have taken TESLA prices) and Gold market

For the prediction challenge of this project, i have tried prediction using Linear Regression and LSTM (Long Shart-Term Memory)
## Creation of new anaconda environment

Created a new conda environment 'Crypto-Analysis' to start with the project and added some necessary folders.
the following folders were setup as suggested as I progressed with the project

*[folder structure'](images/folder structure.PNG)



## Data extraction

Data is from 
qandl
kaggle (for historical dataset - Tableau analysis)
and yahoo finance (yfinance)

## Data transformation and loading

 Step 1 : After data extraction, data was cleaned and transformed and saved into a csv file 'BTC.csv'.

Step 2 : On the AWS cloud, created a RDS and S3 bucket. 

Step 3 : Loaded the BTC.csv file into the S3 bucket

Step4 : set up the necessary config file '_config.template.bat

Step5 : Created tabels in postgres

Step 6 : tested data load locally

Step 7 : changed enpoint settings and deployed the ETL to AWS Lambda

## Data Analysis

Data Analyis has been done using Tableau.
Following are the tableau files published in Tableau Public



## Machile Learning

Machine learning model was created and test and train data was scaled and saved in the below folder
*[test train](images/modelSAVE.PNG)

##  Prediction

Prediction was applied using Linear regression and LSTM model
here are the .ipynb files  for reference

*[linear regression](model/prediction_Linearreg.ipynb)

*[LSTM](model/LSTM.ipynb)

## HTML AND CSS
The folowing  web pages were created to put everything together 

* [html pages](images/htmlpages.PNG)

## flask app
flask app creation code 'app.py'


 * [flask app code](images/flaskapp.PNG)



## AWS deplotyment

Step 1 : stored the commands into build.bat and run the file to crea a zip file

Step2 : Created an application in Elastic Beanstalk and configured it as per the instuctions given.

please click the following link to view the app.


###............................The End.........................................................................



