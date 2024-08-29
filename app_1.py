from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
import zipfile

books_zip_file= "books.zip"

with zipfile.Zipfile(books_zip_file,'r') as zip_ref:
    with zip_ref.open('books.pkl') :
        books= pd.read_pickle('books.pkl','infer')
        
popular_df = pd.read_pickle('popular.pkl','infer')
pt = pd.read_pickle('pt.pkl','infer')
similarity_scores = pd.read_pickle('similarity_scores.pkl','infer')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['bookTitle'].values),
                           author=list(popular_df['bookAuthor'].values),
                           image=list(popular_df['imageUrlM'].values),
                           votes=list(popular_df['Numrating'].values),
                           ratings=list(popular_df['avgrating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['bookTitle'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('bookTitle')['bookTitle'].values))
        item.extend(list(temp_df.drop_duplicates('bookTitle')['bookAuthor'].values))
        item.extend(list(temp_df.drop_duplicates('bookTitle')['imageUrlM'].values))
        data.append(item)
    print(data)
    return render_template('recommend.html',data=data)


if __name__ =='__main__':
    app.run(debug=True)


