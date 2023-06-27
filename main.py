# import numpy as np
# import pandas as pd
# from chatbot import get_response
# from movie_rec_routine import movie_rec

# similarity = pd.read_parquet('similarity', engine='pyarrow')
# similarity = np.array(similarity)
# while True:
#     text = input()
#     if text[:6].lower() == 'movie:':
#         message = {'answer': movie_rec(text[6:], similarity)}
#     else:
#         response = get_response(text)
#         message = {'answer': response}

#     print(message)