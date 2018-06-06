from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # chapter/
    path('chapter/', views.chapter, name='chapter'),
    # chapter/3
    path('chapter/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
    # chapter/3/member
    path('chapter/<int:chapter_id>/member/', views.chapter_members, name='chapter_members'),
    # chapter/3/member/2
    path('chapter/<int:chapter_id>/member/<int:member_id>/', views.chapter_member, name='chapter_member'),
    # chapter/member/
    path('member/', views.member, name='member'),
    # chapter/member/2
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),
]
