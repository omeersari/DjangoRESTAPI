

from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailAPIView, GenericAPIView

urlpatterns = [
    #path('article/', article_list, name="article"),
    path('article/', ArticleAPIView.as_view(), name='APIView'),  # Class olduğu için as_view() ekledik.
    #path('article/<int:pk>/', article_detail, name='article_detail')
    path('article/<int:id>/', ArticleDetailAPIView.as_view(), name='article_detail'),
    path('generic/article/<int:id>/', GenericAPIView.as_view(), name='generic')
]
