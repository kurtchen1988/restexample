from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


if __name__ == '__main__':

    snippet = Snippet(code='foo = "bar"\n')
    snippet.save()

    snippet = Snippet(code='print "hello, world"\n')
    snippet.save()

    serializer = SnippetSerializer(snippet)
    serializer.data
    # 显示被解析的序列器

    content = JSONRenderer().render(serializer.data)
    content
    # 最终被序列化的实例

    import io

    stream = io.BinaryIO(content)
    data = JSONParser().parse(stream)
    # 反序列化

    serializer = SnippetSerializer(data=data)
    serializer.is_valid()
    serializer.validated_data
    serializer.save()
    # 通过序列器序列化数据，数据正确的情况下处理数据，并保存序列化数据

    serializer=SnippetSerializer(Snippet.objects.all(), many=True)
    serializer.data
    # 用模型查询结果序列化

    from snippets.serializers import SnippetSerializer
    serializer = SnippetSerializer()
    print(repr(serializer))


