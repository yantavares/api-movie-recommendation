from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ChatSerializer, MessageSerializer, CreateMessageSerializer
from .models import Chat, Message
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def chats(request):

    if request.method == 'DELETE':
        Chat.objects.all().delete()
        return Response({"msg": "All chats were deleted!"}, status=204)

    if request.method == 'GET':
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        last_chat = Chat.objects.order_by('-created_at').first()

        if last_chat is None or last_chat.has_messages():
            serializer = ChatSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            serializer = ChatSerializer(last_chat)
            return Response(serializer.data, status=200)


@api_view(['GET', 'PATCH', 'DELETE'])
@csrf_exempt
def chat_by_id(request, id):
    try:
        chat = Chat.objects.get(pk=id)
    except Chat.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ChatSerializer(chat)
        return Response(serializer.data)

    if request.method == 'PATCH':
        serializer = ChatSerializer(chat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        chat.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
@csrf_exempt
def messages(request, id):
    try:
        chat = Chat.objects.get(pk=id)
    except Chat.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        messages = Message.objects.filter(chat=chat)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CreateMessageSerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.validated_data['content']
            message = Message.create_message(chat, content)
            message_serializer = MessageSerializer(message)
            return Response(message_serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
