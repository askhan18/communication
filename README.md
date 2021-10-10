# Exploratory Data Analysis w/ Pandas

Exploratory Data Analysis is a process that stands for exploratory data analysis where data scientists and alike try to make sense of data. 

This repository has code that walks through a general process of understanding data using Pandas, a data analysis library, in Python. We selected three steps, describing, cleaning, and visualizing, to demonstrate EDA. Each of these steps will be applied to a subsampled covid19 dataset from [Our World In Data](https://github.com/owid/covid-19-data/tree/master/public/data/). 

## The Data

Data is pulled up to August 21st, 2021. 
| Column                           | Description                                                           |
|:---------------------------------|:----------------------------------------------------------------------|
| `iso_code`                    |  ISO 3166-1 alpha-3 – three-letter country codes              |
| `date`                    |   Date of observation   |
| `new_cases`                      | New confirmed cases of COVID-19                           |
| `new_deaths`             | New deaths attributed to COVID-19                       |
| `icu_patients`        |  Number of COVID-19 patients in intensive care units (ICUs) on a given day              |
| `hosp_patients`          |  Number of COVID-19 patients in hospital on a given day              |
| `people_vaccinated` | Total number of people who received at least one vaccine dose  |
| `people_fully_vaccinated` |Total number of people who received all doses prescribed by the vaccination protocol |

# Requirements
This project was done on: 
 - pandas 1.3.2
 - jupyter-notebook 6.4.3

 # Usage
 We recommend installing pandas and jupyter through [Anaconda](https://www.anaconda.com/products/individual). Both libraries should already be installed. But the following code can be run in the terminal to install the libraries again.  
 ```
conda install pandas notebook
 ```
The notebook can be opened by running the following code after navigating to the *.ipynb file. 
```
jupyter notebook
```

# What is EDA?
"Exploratory Data Analysis refers to the critical process of performing initial investigations on data so as to discover patterns,to spot anomalies,to test hypothesis and to check assumptions with the help of summary statistics and graphical representations." — Prasad Patil 

## 1. Get an initial sniff of the data

When given a dataset, we need to know some basic information of this dataset, including shape, columns information and type, missing values. We will use some functions from pandas to explore these features.

### How big is this data and what are the column names and their datatypes?
```
df.info()
```
```
df.describe()
```
```
df.shape
```
```
df.head(2)
```

### Any missing values? 
```
df.isnull().any()
```

## 2. Initial cleaning up

## 3. Visualizations

## 4. Results/Conclusion

## 5. Further Work(Optional)
