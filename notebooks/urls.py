from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import NotebookList, NotebookDetail, UsersList, UserDetail, GroupList, GroupDetail
from .views import UserNotebookList
urlpatterns = [
    url(r'^notebooks/$', NotebookList.as_view(), name='notebook-list'),
    url(r'^notebooks/(?P<pk>\d+)/$', NotebookDetail.as_view(), name='notebook-detail'),
    url(r'users/$', UsersList.as_view(), name='users-list'),
    url(r'users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail-pk'),
    url(r'users/(?P<pk>\d+)/notebooks/$', UserNotebookList.as_view(), name='user-notebook-list'),
    url(r'users/(?P<username>[\w_]{1,150})/$', UserDetail.as_view(), name='user-detail-username'),
    url(r'groups/$', GroupList.as_view(), name='group-list'),
    url(r'groups/(?P<pk>\d+)/$', GroupDetail.as_view(), name='group-detail'),
    url(r'groups/(?P<name>[\w_]{1,80})/$', GroupDetail.as_view(), name='group-detail-name')
]

urlpatterns = format_suffix_patterns(urlpatterns)