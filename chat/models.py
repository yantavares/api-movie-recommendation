from django.db import models
import numpy as np
import pandas as pd
from .chatbot import get_response
from .movie_rec_routine import movie_rec

similarity = pd.read_parquet('chat/similarity', engine='pyarrow')
similarity = np.array(similarity)


class Chat(models.Model):
    title = models.CharField(
        max_length=255, default="New recommendation about...")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def has_messages(self):
        return self.message_set.exists()


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    @staticmethod
    def create_message(chat, content):
        if content[:6].lower() == 'movie:':
            content = content[6:]
            bot_response = {'answer': movie_rec(content[6:], similarity)}
        else:
            response = get_response(content)
            bot_response = {'answer': response}

        message = Message(chat=chat, content=content,
                          bot_response=bot_response['answer'])
        message.save()
        return message
