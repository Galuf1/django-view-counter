from django.shortcuts import render
from datetime import datetime
import random

sessions = {}
def index(request):
    print(sessions)
    session_id_number = request.COOKIES.get('session_id_number')
    session = sessions.get(session_id_number)
    if not session:
        session_id_number = str(random.randint(100000,999999))
        
        sessions[session_id_number] = {
            'count': 1
        }
    else:
        sessions[session_id_number]['count'] += 1
    response = render(request, 'counter/index.html', sessions[session_id_number])
    response.set_cookie('session_id_number', session_id_number)
    return response