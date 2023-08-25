import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from flask import Flask, render_template, request
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

user_game_ratings = pd.read_csv('final_rating.csv')

piv_norm = user_game_ratings.pivot(index='games', columns='User_id', values='rating').fillna(0)

game_similarity = cosine_similarity(piv_norm)

def recommend_games(user_id):
    user_ratings = piv_norm[user_id]  # User's ratings
    user_similarity = game_similarity.T.dot(user_ratings) / (game_similarity.T.sum(axis=1) + 1e-8)
    
    # Sort indices based on similarity values in descending order
    recommended_games = piv_norm.index[user_similarity.argsort()[::-1]]
    
    return recommended_games

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recommendation',methods=['POST'])
def recommendation():
    user_id = request.form.get('user_id')
    try:
        recommended_games = recommend_games(int(user_id))
        recommended_games = recommended_games[:10]
        return render_template('index.html', recommended_games=recommended_games)
    
    except(ValueError, KeyError):
        error_message = 'Invalid User ID. Please enter a valid user ID'
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=False)


