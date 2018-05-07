
import re

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from AXF.models import User


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        patterns = (
            r'^/axf/user/*',
            r'^/axf/home/*',
        )

        path = request.path
        for pattern in patterns:
            if re.match(pattern, path):
                return None

        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/axf/user/login/')
        users = User.objects.filter(ticket=ticket)
        if not users:
            return HttpResponseRedirect('/axf/user/login/')

        request.user = users[0]