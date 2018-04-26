from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_data, name='get_data'),
    url(r'^insert/(?P<german_word>[\w\-]+)/(?P<english_translation>[\w\-]+)/(?P<gender>[\w\-]+)/$', views.insert_word, name='insert_word'),
    url(r'^delete/(?P<word_id>\d+)/$', views.delete_word, name='delete_word'),

]