from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from profile_matching.profiles.views import user
from profile_matching.profiles.views import profile
from profile_matching.profiles.views import topic
from profile_matching.profiles.views import api_root


urlpatterns = [
    url(r'^$', api_root.api_root),
    url(r'^profiles/$', profile.ProfileList.as_view(), name='profiles-list'),
    url(r'^users/$', user.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user.UserDetail.as_view()),
    url(r'^topics/$', topic.TopicList.as_view(), name='topics-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
