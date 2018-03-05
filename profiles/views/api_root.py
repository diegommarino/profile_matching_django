from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'profiles': reverse('profiles-list', request=request, format=format),
        'topics': reverse('topics-list', request=request, format=format),
        'token': reverse('get-token', request=request, format=format),
    })
