import pandas as pd
import difflib

movies_data = pd.read_csv('C:\\Users\\guilh\\Dev\\Back-end\\api-movie-recommendation\\chat\\movies.csv')
list_of_all_titles = movies_data['title'].tolist()

def movie_rec(movie_name, similarity):

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if find_close_match == []:
        return "I'm embarrassed, I don't know this movie yet, I'm sorry. Try another movie, I'll be happy to help you this time!"

    close_match = find_close_match[0]

    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    sorted_similar_movies = sorted(
        similarity_score, key=lambda x: x[1], reverse=True
    )[:6]

    movie_sugestion = 'Based on the movie "'
    i = 1
    for movie in sorted_similar_movies:

        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        release_from_index = movies_data[movies_data.index == index]['release_date'].values[0]

        if (i==1):
            movie_sugestion = movie_sugestion + (
                (
                    (
                        (
                            (title_from_index + '" (' + release_from_index[:4])
                            + '), directed by '
                        )
                        + movies_data[movies_data.index == index][
                            'director'
                        ].values[0]
                    )
                    + ", I recommend you see: "
                )
            )
            i+=1
            continue

        if (i<7):
            movie_sugestion = movie_sugestion + (
                f"{str(i - 1)}. "
                + title_from_index
                + " ("
                + release_from_index[:4]
                + ")"
            )
            i+=1
    return movie_sugestion