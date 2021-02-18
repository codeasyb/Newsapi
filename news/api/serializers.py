from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.Serializer):
    
    # this id field should be a read only field
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        print(validated_data) # debuggin purposes and will print at the terminal
        return Article.objects.create(**validated_data)
     
    def update(self, instance, validated_data): 
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.body = validated_data.get("body", instance.body)
        instance.location = validated_data.get("location", instance.location)
        instance.publication_date = validated_data.get("publication_date", instance.publication_date)
        instance.active = validated_data.get("active", instance.active)
        return instance
    
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
