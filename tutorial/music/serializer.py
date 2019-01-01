from rest_framework import serializers
from music.models import Album, Track



class TrackSerialzer(serializers.ModelSerializer):
    class Meta:
        model= Track
        fields = ('order','title','duration')

class AlbumSerializer(serializers.ModelSerializer):

    # StringRelatedField: 用String来呈现关系，这里调用的是__unicode__方法,最终生成的序列会成为一个数组，数组里全是string
    #tracks = serializers.StringRelatedField(many=True)

    # PrimaryKeyRelatedField: 生成的序列只显示ID
    #tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # HyperlinkedRelatedField: 生成的目标对象是URL链接集合。这里的slug的model里必须
    #tracks = serializers.HyperlinkedRelatedField( many=True, read_only=True, view_name='track-detail')

    # SlugRelatedField: 只显示相关联项目的字母相关项
    # tracks = serializers.SlugRelatedField(many=True, read_only=True,slug_field='title')

    # HyperlinkedIdentityField：生成的目标对象是单个URL链接
    #tracks = serializers.HyperlinkedIdentityField(view_name='track-list')

    # 多重层次
    tracks = TrackSerialzer(many= True, read_only=True)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'tracks')


'''
>>> album = Album.objects.create(album_name="The Grey Album", artist='Danger Mouse')
>>> Track.objects.create(album=album, order=1, title='Public Service Announcement', duration=245)
<Track: Track object>
>>> Track.objects.create(album=album, order=2, title='What More Can I Say', duration=264)
<Track: Track object>
>>> Track.objects.create(album=album, order=3, title='Encore', duration=159)
<Track: Track object>
>>> serializer = AlbumSerializer(instance=album)
>>> serializer.data
{
    'album_name': 'The Grey Album',
    'artist': 'Danger Mouse',
    'tracks': [
        {'order': 1, 'title': 'Public Service Announcement', 'duration': 245},
        {'order': 2, 'title': 'What More Can I Say', 'duration': 264},
        {'order': 3, 'title': 'Encore', 'duration': 159},
        ...
    ],
}
'''
