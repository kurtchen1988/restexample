from django.urls import path, include
from . import views
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='test api')

'''
urlpatterns = [

    # 重写API的url写法
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>', views.SnippetDetail.as_view()),

    # 查询用户接口
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    # 最底层的url
    path('', views.api_root),
    # 为查询snippets的highlight的接口
    path('snippets/<int:pk>/highlight/', views.SnipetHighlight.as_view())

    # 用Hyperlink的方式写url  
]
'''
snippet_list = SnippetViewSet.as_view({
    'get':'list',
    'post':'create',
})

snippet_detail = SnippetViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy',
})

snippet_highlight = SnippetViewSet.as_view({
    'get':'highlight',
}, renderer_classes = [renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get':'list',
})

user_detail = UserViewSet.as_view({
    'get':'retrieve',
})

urlpatterns = format_suffix_patterns([
    path('schema/', schema_view),
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list,name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])

'''
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnipetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(),name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
])
'''

'''
# 普通的url写法
path('snippets/', views.snippet_list),
path('snippets/<int:pk>/', views.snippet_detail),
'''

# 通过这个对url的设置，可以显示各种格式的数据
#urlpatterns = format_suffix_patterns(urlpatterns)

# 加上了权限功能，这样页面上可以看到登录的选项
urlpatterns += [path('api-auth/', include('rest_framework.urls')),]
