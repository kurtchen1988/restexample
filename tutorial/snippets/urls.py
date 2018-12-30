from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

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

]

'''
# 普通的url写法
path('snippets/', views.snippet_list),
path('snippets/<int:pk>/', views.snippet_detail),
'''

# 通过这个对url的设置，可以显示各种格式的数据
urlpatterns = format_suffix_patterns(urlpatterns)

# 加上了权限功能，这样页面上可以看到登录的选项
urlpatterns += [path('api-auth/', include('rest_framework.urls')),]
