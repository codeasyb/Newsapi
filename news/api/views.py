from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response 

from news.models import Article
from news.api.serializers import ArticleSerializer

# FIRST END POINT
@api_view(['GET', 'POST'])
def article_list_create_api_view(request):
    if request.method == "GET":
        articles = Article.objects.filter(active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    # this process is to create new instances and send data to the api
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


# SECOND END POINT 
@api_view(['GET', "PUT", 'DELETE'])
def article_detail_api_view(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExit:
        return Response({"error": {
            "code": 404,
            "message": "Article not found!"
        }}, status=status.HTTP_404_NOT_FOUND)
    
    # this point the article does exists
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# AT THIS POINT AFTER THIS YOU WANT TO GO AND DEFINE YOUR NEW END POINT IN urls.py




# ERROR Information

# Thing to note if you get the error of 
# The serilaizer field might be named incorrectly and not mathc any attributes of key
# on the `QuerySet` instance
# Original exception text was: `QuerySet` object has no attribute 'author' is to check 
# your function article_list_create_api_view(request)
# def article_list_create_api_view(request):
#     if request.method == "GET":
#         articles = Article.objects.filter(active=True)
#         serializer = ArticleSerializer(articles) <----- Fixed solution add [ many=True ]
#         return Response(serializer.data)

# that our serializer know that to serve the whole QuerySet