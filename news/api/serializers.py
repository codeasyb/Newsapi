from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist

# ------------------------------------------------------------------------------------------------------
# THE BEST AND EFFICENT WAY TO CREATE SERIALIZER 
# ------------------------------------------------------------------------------------------------------
class ArticleSerializer(serializers.ModelSerializer):
    
    time_since_publication = serializers.SerializerMethodField()
    # author = JournalistSerializer()
    # author = serializers.StringRelatedField()
    
    # this meta helps save all the lines below for the fields
    class Meta:
        model = Article
        exclude = ("id",)
        # fields = "__all__"
        
    # Self explanatory lol
    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, data):
        """ 
            Check that description and title are different
        """
        if data['title'] == data['description']:
            raise serializers.ValidationError('Title and descrption must be different')
        return data
    
    def validate_title(self, value):
        """
            Check that title is at least 60 chars long
        """    
        if len(value) < 30:
            raise serializers.ValidationError('The Title has to be at least 30 chars long')
        return value

class JournalistSerializer(serializers.ModelSerializer):
    
    articles = serializers.HyperlinkedRelatedField(many=True, 
                                                   read_only=True, 
                                                   view_name="article-detail")
    # articles = ArticleSerializer(many=True, read_only=True)
    class Meta:
        model = Journalist
        fields = "__all__"
        
    def validate(self, data):
        pass


# ------------------------------------------------------------------------------------------------------
#  All this code is so ambigious wow
# ------------------------------------------------------------------------------------------------------
# class ArticleSerializer(serializers.Serializer):
    
#     # this id field should be a read only field
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
    
#     def create(self, validated_data):
#         print(validated_data) # debuggin purposes and will print at the terminal
#         return Article.objects.create(**validated_data)
     
#     def update(self, instance, validated_data): 
#         instance.author = validated_data.get("author", instance.author)
#         instance.title = validated_data.get("title", instance.title)
#         instance.description = validated_data.get("description", instance.description)
#         instance.body = validated_data.get("body", instance.body)
#         instance.location = validated_data.get("location", instance.location)
#         instance.publication_date = validated_data.get("publication_date", instance.publication_date)
#         instance.active = validated_data.get("active", instance.active)
#         return instance
    
#     def validate(self, data):
#         """  
#             check that description and title are different
#         """    
#         if data['title'] == data['description']:
#             print("---------------------------_> Error")
#             raise serializers.ValidationError("Title and description must be different")
#         print("------> Sucess")
#         return data
    
    



# Serializing process

# Code: from news.models import Article
# Code: from news.api.serializer import ArticleSerializer
# now you can create instances of your articles 
# To serialize the data you want

# Code: serializer = ArticleSerializer(your_article_instance_you_created)
# To check the serialized data you can do so by
# Code: serializer.data
# One thing to note is that you can only use serializer.data to check one instance 
# a time becasue if you use objects.all() of all the articles serializer.data 
# will throw an errror

# Now we want to render the data
# Code: from rest_framework.renderers import JSONRenderer
# Code: json = JSONRenderer().render(serializer.data)
# now you see your data in json format print(json)

# Now lets parse the json data
# Code: import io
# Code: from rest_framework.parsers import JSONParser
# Code: stream_of_data = io.BytesIO(json)
# Code: data = JSONParser().parse(stream_of_data)
# Code: data <----
# you can also check for validation of your parsed data
# Code: serializer = ArticleSerializer(data=data) <----
# Code: serializer.is_valid()
# You can validate your parsed data
# Code: serializer.validated_data <-- this will validate the parsed data
# Also save your instance which creates a copy of your original instance
# sCode: erializer.save()
