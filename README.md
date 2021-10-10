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
<img width="501" alt="Screen Shot 2021-10-10 at 2 29 57 PM" src="https://user-images.githubusercontent.com/87035350/136713585-7a4f47ff-0608-4282-804c-dc409b9f0cdc.png">

```
df.describe()
```
<img width="684" alt="Screen Shot 2021-10-10 at 2 30 39 PM" src="https://user-images.githubusercontent.com/87035350/136713600-a77e4ce0-7a34-4467-a263-09e4d6a29228.png">

```
df.shape
```
<img width="130" alt="Screen Shot 2021-10-10 at 2 30 23 PM" src="https://user-images.githubusercontent.com/87035350/136713596-dcff4a92-f7a5-485e-afaf-e2efac8511c7.png">

```
df.head(2)
```
<img width="757" alt="Screen Shot 2021-10-10 at 2 30 51 PM" src="https://user-images.githubusercontent.com/87035350/136713606-bee9816f-d7a1-4c8e-8124-80a3fc411999.png">

```
df.head(2).T
```
<img width="327" alt="Screen Shot 2021-10-10 at 2 31 08 PM" src="https://user-images.githubusercontent.com/87035350/136713617-99ece31f-f19d-46ea-a08a-d4fbcb7acf8e.png">


### Any missing values? 
```
df.isnull().any()
```
<img width="284" alt="Screen Shot 2021-10-10 at 2 31 19 PM" src="https://user-images.githubusercontent.com/87035350/136713611-e70a1919-82fe-49e3-afd0-290592a68241.png">


## 2. Initial cleaning up
After having an intial sniff of the data, we need to use python functions to clean up the messy data. We could detect abnormalies and outliers, fixing missing values, and ensure data integrity before further modeling.

```
df['date'] = pd.to_datetime(df['date'])
```
<img width="471" alt="Screen Shot 2021-10-10 at 2 34 24 PM" src="https://user-images.githubusercontent.com/87035350/136713645-06c9a50e-6cc3-45d1-8fd0-75f728c40d41.png">

By using isnull().sum(), we could see how many rows in each column contains the missing value (NULL).
```
df.isnull().sum()
```
![image](https://user-images.githubusercontent.com/86521753/136712469-7e169bfa-c050-49e9-a5e5-fb074faaf76a.png)

Depending on different situations, we could fill out those missing values using zero, mean, median, or other specific values.
```
df.fillna(0, inplace=True)
```
![image](https://user-images.githubusercontent.com/86521753/136712473-44d3bf98-3f4e-45ad-8d5b-7719c62b98c7.png)

Also, in some cases, negative values should be considered as invalid data. We could use python fuctions to find them out and change their values.

![image](https://user-images.githubusercontent.com/86521753/136712482-df3c0bdf-2c93-477a-a096-9a1a98a2d0c0.png)

Other data cleaning methods could be used depending on the situations. For example, scatter plot could be used to deal with outliers, etc.

Data cleaning is a very critical step in EDA. In the reality, most of the data we obtained is very messy and might contain problematic data points. We could not do visualizations or apply the model to them easily. To data scientists, a structured and clean dataset would help a lot in future investigation steps.
## 3. Visualizations

In the modern era of BIG DATA, Data visualization plays an important role in extracting key insights from trillions of rows of data generated every day. Data visualization helps to tell stories by curating data into a form that is easier to understand. Below are two examples that clealy show how a good visualization helps to see the trend in data and the relationship between different features. 

### Scatter plot highlighting the trend in the number of covid cases in US
<img width=700 height=500 margin-left=300 margin-right= 300 alt="scatter_plot" src="https://github.com/askhan18/communication/blob/master/scatter_plot.png"></center>

### Heatmap to show the correlation between different numeric features in the data
<center><img width="500" height="500" alt="Heatmap" src="https://github.com/askhan18/communication/blob/master/Heatmap.png"></center>

## 4. Results/Conclusion

## 5. Further Work(Optional)
