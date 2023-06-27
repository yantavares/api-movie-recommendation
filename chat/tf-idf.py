# Installing and loading necessary packages -----------------------
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Loading data
movies_data = pd.read_csv('C:\\Users\\guilh\\Dev\\Back-end\\api-movie-recommendation\\chat\\movies.csv')

# Selecting important features
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director', 'title', 'release_date', 'index']

# Treating missing values
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Joining all the selected features for analysis
combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + \
                    movies_data['cast'] + ' ' + movies_data['director']

# Transforming the text data into feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Cosine similarity ----------------------------------------------------------------------------------------------------
# Getting the similarity scores
similarity = pd.DataFrame(cosine_similarity(feature_vectors)).round(3)
similarity.columns = similarity.columns.astype(str)

# Saving files
similarity.to_parquet('similarity', engine = 'pyarrow', compression = 'gzip')
