from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import NotebookList, NotebookDetail, UsersList, UserDetail

urlpatterns = [
    url(r'^notebooks/$', NotebookList.as_view(), name='notebook-list'),
    url(r'^notebooks/(?P<pk>\d+)/$', NotebookDetail.as_view(), name='notebook-detail'),
    url(r'users/$', UsersList.as_view(), name='users-list'),
    url(r'users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail-pk'),
    url(r'users/(?P<username>[\w_]+)/$', UserDetail.as_view(), name='user-detail-username'),
]

urlpatterns = format_suffix_patterns(urlpatterns)