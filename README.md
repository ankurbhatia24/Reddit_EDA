# Reddit_EDA
This repository contains Flair Prediction on reddit posts of r/india, also includes EDA.

## To Test the Application part 1:<br>
1. Visit: http://13.234.217.64/
2. Enter a reddit post from r/India Subreddit.<br>
![Application Part 1](Media/Route_1.gif)

## To Test the Application part 2:<br>
1. Clone the repository: **git clone https://github.com/ankurbhatia24/Reddit_EDA.git**
2. Edit the file test.txt with the subreddit(india) posts links in each line.
3. Run the python file: **python3 post_text_file.py** <br>
![Application Part 2](Media/Route-2.gif)

## To Reproduce the Developement Environment:<br>
1. Clone the repository: **git clone https://github.com/ankurbhatia24/Reddit_EDA.git**
2. Create a virtual environment: **virtualenv env**
3. Activate virtual environment: **source env/bin/activate**
4. Install the requirements: **pip3 install -r requirements.txt**
5. "Flair_csv" is the Database file: To collect your own data, execute the "Reddit Data Collection.ipynb". Change the reddit instance credentials accordingly.(Read https://towardsdatascience.com/scraping-reddit-with-praw-76efc1d1e1d9 to setup reddit app)
6. After installation of the required libraries, you can test the code in the 'IPYNB' <br> directory. 

## Understanding Models
### In the 'Data_pre-procesing and Model Evaluation.ipynb', there are three models defined after the preprocessing of the Data.
#### Process: 
1. The Reddit data collected is cleaned and Preprocessed according to the models needs.<br>
The text is cleaned for any punctuations, emojis, special characters, STOPWORDS(A stop word is a commonly used word (such as “the”, “a”, “an”, “in”)), etc.2
2. The raw text is tokenized (each word/token is assigned a number according to a dictionary) and converted from word to vector using GloVe embeddings (300d).
3. The Flairs (**flairs = ["AskIndia", "Coronavirus", "Non-Political", "Scheduled", "Photography", "Science/Technology", "Politics", "Business/Finance", "Policy/Economy", "Sports", "Food", "AMA"]**) to be predicted are converted to One-Hot encodings.
4. Finally the data is splitted into Training and Testing.
## 1. Convolution Model
![](Media/midasl_1.jpg)

![](Media/midasl_2.jpg)
## 2. LSTM Model
![](Media/midasl_3.jpg)
## 3. Bidirectional LSTM Model
![](Media/midasl_4.jpg)

