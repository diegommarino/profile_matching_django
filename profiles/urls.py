from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from profile_matching.profiles.views import user
from profile_matching.profiles.views import profile
from profile_matching.profiles.views import topic
from profile_matching.profiles.views import api_root
from profile_matching.profiles.views import login
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^$', api_root.api_root),
    url(r'^profiles/$', profile.ProfileList.as_view(), name='profiles-list'),
    url(r'^users/$', user.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user.UserDetail.as_view()),
    url(r'^topics/$', topic.TopicList.as_view(), name='topics-list'),
    url(r'^api-token-auth/', views.obtain_auth_token, name='get-token'),
    url(r'^sign-in/', login.sign_in, name='signin'),
    url(r'^sign-up/', login.sign_up, name='signup'),
    url(r'^logout/', login.logout, name='logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
