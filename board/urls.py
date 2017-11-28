from django.conf.urls import url, include
from board.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^korea/$', KoreaBoard.as_view(), name='korea'),
    url(r'^korea/(?P<pk>\d+)/$', PostDetail.as_view(), name='post_detail'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    #url(r'^korea/(?P<pk>\d+)/', add, name='add_comment'),

# 11/9 글쓰기 기능 구현 위해 작성
    url(r'^add/$', PostAdd.as_view(), name='post_add'),
    url(r'^korea/(?P<pk>\d+)/edit/$', PostEdit.as_view(), name='post_edit'),
    url(r'^korea/(?P<pk>\d+)/delete/$', PostDelete.as_view(), name='post_delete'), 
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

