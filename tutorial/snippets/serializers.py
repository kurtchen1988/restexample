from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


'''
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template':'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):

        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('title', instance.code)
        instance.linenos = validated_data.get('title', instance.linenos)
        instance.language = validated_data.get('title', instance.language)
        instance.style = validated_data.get('title', instance.style)
        instance.save()
        return instance

    class Meta:
        fields = "__all__"
'''

'''
class SnippetSerializer(serializers.ModelSerializer):
    # 用ModelSerializer来序列化模型, 这里要注意的是这个类只会做两件事情：
    # 1. 显示所有的fields
    # 2. 自动实现create和update方法
    class Meta:
        model = Snippet
        fields = ('id','title','code','linenos','language','style')
'''

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # 用链接类目写的序列器
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url','id', 'highlight','owner','title','code','linenos','language','style')

'''
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
'''

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # 用链接类目写的序列器
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url','id','username','snippets')