import time
import re

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from AXF.models import User
from user.models import Cookies


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        patterns = (
            r'^/user/*',
            r'^/axf/*',
        )

        path = request.path
        for pattern in patterns:
            if re.match(pattern, path):
                return None

        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/user/login/')
        users = Cookies.objects.filter(ticket=ticket)
        if not users:
            return HttpResponseRedirect('/user/login/')
        times = users[0].create_time
        now_time = int(time.time())
        if now_time > times + 3600:
            users[0].delete()
            return HttpResponseRedirect('/user/login/')
        id = users[0].u_id
        try:
            user = User.objects.get(id=id)
        except Exception as e:
            return HttpResponseRedirect('/user/login/')

        request.user = user
