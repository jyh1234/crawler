from  django.conf.urls import url
from . import views
app_name = 'function'

urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^count/',views.count,name='count'),
    url(r'^count1/',views.count1,name='count1'),
    url(r'^low_unprocessed_list_html/',views.low_unprocessed_list_html,name='low_unprocessed_list_html'),
    url(r'^high_unprocessed_list_html/',views.high_unprocessed_list_html,name='high_unprocessed_list_html'),
    url(r'^low_processed_list_html/',views.low_processed_list_html,name='low_processed_list_html'),
    url(r'^high_processed_list_html/',views.high_processed_list_html,name='high_processed_list_html'),
    url(r'^comment_list/',views.comment_list,name='comment_list'),
    url(r'^comment_content/',views.comment_content,name='comment_content'),
    url(r'^comment_content_high_processed/',views.comment_content_high_processed,name='comment_content_high_processed'),
    url(r'^comment_content_high_unprocessed/',views.comment_content_high_unprocessed,name='comment_content_high_unprocessed'),
    url(r'^comment_content_low_processed/',views.comment_content_low_processed,name='comment_content_low_processed'),
    url(r'^comment_content_low_unprocessed/',views.comment_content_low_unprocessed,name='comment_content_low_unprocessed'),
    url(r'^submit_newscore/',views.submit_newscore,name='submit_newScore'),
    url(r'^send_message/',views.send_message,name='send_message'),
    url(r'^changeitems/',views.changeitems,name='changeitems'),
    url(r'^admin/index$',views.admin,name='admin'),
    url(r'^save_train/', views.save_train, name='save_train'),
    url(r'^precision/', views.precision, name='precision'),
    url(r'^sys_all/', views.sys_all, name='sys_all'),
]