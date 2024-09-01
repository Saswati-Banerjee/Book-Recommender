# Book-Recommender
**Book Recommender System using Machine Learning**
**Objectives**: The main objective is to create a book recommendation system for users using collaborative filtering based method.
**Methods** : Descriptive Statistics Data Visualization Machine Learning and python web app using Flask
**Technologies** : Python, pandas , matplotlib, seaborn , numpy , sci-kit learn, flask
**Overview of the Project** : book recommendation system has a utility and in this blog we would be discussing on how can we create a book recommendation system using two approaches:
Popularity based - provides generalized recommendation to every user depending on the popularity or average ratings. Whatever is more popular among the general public that is more likely to be recommended. Here , we have chosen only those top 50 books which have got ratings more than 500 .
Collaborative filtering based -It works by considering user ratings and finds cosine similarities in ratings by several users to recommend books. To implement this, we took only those books' data that have at least 50 ratings in all (because of limited resources) and also those userrs who have rated more than 200 books.
**Dataset** : Collected from kaggle (Link: )
Three datasets were available - Books
                                Users
                                Ratings
Dataset pre-processing and cleaning :
First all the null and duplicated values are checked in three datasets. Some data were misiing which were filled before implementing ML models on thse datasets.
I have considered books which got ratinhgs higher than 0 .
Then EDA ( Exploratory Data Anaysis ) were performed based on book ratings>0 , most read books , average rating of most read books , Number of books with a specific title length , Top 30 years of publishing , Top 30 Authors according to most books , Top 30 Publishers according to most books , Number of users according to user age . 
In popularity based model top 50 books with highest avarage rating were selected. Also, to avoid biasness only books qith at least 200 ratings are chosen only. 
 Collaborative filtering uses a matrix to map user behavior for each item in its system. The system then draws values from this matrix to plot as data points in a vector space. Various metrics then measure the distance between points as a means of calculating user-user and item-item similarity.Cosine similarity signifies the measurement of the angle between two vectors. Compared vectors comprise a subset of ratings for given user or item. The cosine similarity score can be any value between -1 and 1. The higher the cosine score, the more alike two items are considered.We would take the ratings of the users who have rated over 200 books i.e. have studied and reviewed high amount of books with the highest priority.We would only recommend books that have more than 50 ratings i.e. popular and famous books.
We filter the users who have rated over 200 books using count( ) and books with more than 50 ratings using count( ) as well.We would then make a pivot table of users and books. 
We make each book as a point made by a vector using the users. That means each books is represented as rating by the user that have made more than 200 votes. Here, 816 users.After representing them as cosine vectors we then proceed to use the cosine similarity as the measure of similarity.
The URL of the Book Recommender web-app : https://saswati.pythonanywhere.com/
