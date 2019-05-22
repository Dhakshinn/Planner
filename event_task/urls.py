from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^remember/',views.remember,name="remember"),
    url(r'^add_remember/',views.remember_add.as_view(),name="add_remember"),
    url(r'^update_remember/(?P<pk>[0-9]+)/$',views.remember_update.as_view(),name="update_remember"),
    url(r'^delete_remember/(?P<pk>[0-9]+)/$',views.remember_delete.as_view(),name="delete_remember"),
    url(r'^add_event/',views.event_add.as_view(),name="add_event"),
    url(r'^update_event/(?P<pk>[0-9]+)/$',views.event_update.as_view(),name="update_event"),
    url(r'^delete_event/(?P<pk>[0-9]+)/$',views.event_delete.as_view(),name="delete_event"),
    url(r'^add_document/',views.document_add.as_view(),name="add_document"),
    url(r'^update_document/(?P<pk>[0-9]+)/$',views.document_update.as_view(),name="update_document"),
    url(r'^delete_document/(?P<pk>[0-9]+)/$',views.document_delete.as_view(),name="delete_document"),
    url(r'^event/$',views.events,name="event"),
    url(r'^document/$',views.document,name="document"),
    url(r'^task/(?P<month>[0-9]+)/(?P<year>[0-9]+)/$',views.task,name="task"),
    url(r'^update_task/(?P<pk>[0-9]+)/$',views.task_update.as_view(),name="update_task"),
    url(r'^add_task/(?P<date_code>[0-9]+)/(?P<month_code>[0-9]+)/(?P<year_code>[0-9]+)/$',views.add_task,name="add_task"),
    url(r'^add_new_task/',views.new_task.as_view(),name="new_task"),
]

