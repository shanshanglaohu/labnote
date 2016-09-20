from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import NotebookList, NotebookDetail,users_list

urlpatterns = [
    url(r'^notebooks/$', NotebookList.as_view(), name='notebook-list'),
    url(r'^notebooks/(?P<pk>\d+)/$', NotebookDetail.as_view(), name='notebook-detail'),
    url(r'users-list$', users_list, name='users-list')
]

urlpatterns = format_suffix_patterns(urlpatterns)