from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.assure_connection, name='assure_connection'),
    url(r'^api/getVocabulary', views.get_data, name='get_data'),
    url(r'^api/getUsers', views.get_users, name='get_users'),
    url(r'^api/insertWord/(?P<german_word>[\w\-]+)/(?P<translation>[\w\-]+)/(?P<gender>[\w\-]+)/$', views.insert_word, name='insert_word'),
    url(r'^api/deleteWord/(?P<word_id>\d+)/$', views.delete_word, name='delete_word'),
    url(r'^api/insertUser/(?P<user_name>[\w\-]+)/(?P<password>[\w\-]+)/$', views.insert_user, name='insert_user'),
#    url(r'^api/deleteUser/(?P<word_id>\d+)/$', views.delete_word, name='delete_user'),

]
