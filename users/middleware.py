from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

class ExpeClubMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            expe = int(request.POST.get('expe'))
            if expe < 1:
                return HttpResponseBadRequest("У вас мало опыта, приходитье поднабрав опыта.")
            elif 1 <= expe <= 3:
                request.club = 'Зарплата 1000$'
            elif 3 < expe <= 7:
                request.club = 'Зарплата 2000$'
            elif 7 < expe <= 10:
                request.club = 'Зарплата 5000$'
            else:
                return HttpResponseBadRequest("Для вас нет работы")
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'club', 'Клуб не определен')