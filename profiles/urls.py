from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from profiles.views import user
from profiles.views import profile
from profiles.views import topic
from profiles.views import api_root
from profiles.views import login
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^$', api_root.api_root),
    url(r'^profiles/$', profile.ProfileList.as_view(), name='profiles-list'),
    url(r'^profiles/create/$', profile.ProfileCreate.as_view(), name='profiles-create'),
    url(r'^profiles/(?P<pk>[0-9]+)/$', profile.ProfileDetail.as_view(), name='profile'),
    url(r'^users/$', user.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user.UserDetail.as_view()),
    url(r'^topics/$', topic.TopicList.as_view(), name='topics-list'),
    url(r'^topics/create/$', topic.TopicCreate.as_view(), name='topic-create'),
    url(r'^topics/(?P<pk>[0-9]+)/$', topic.TopicDetail.as_view(), name='topic'),
    url(r'^api-token-auth/', views.obtain_auth_token, name='get-token'),
    url(r'^sign-in/$', login.sign_in, name='signin'),
    url(r'^sign-up/$', login.sign_up, name='signup'),
    url(r'^logout/$', login.logout, name='logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
