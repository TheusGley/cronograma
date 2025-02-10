from django.shortcuts import render
from datetime import datetime
import calendar 
from .models import Evento
from babel.core import Locale
from babel.dates import format_date


# Create your views here.
def homeView (request):
   
        now = datetime.now()
        year = now.year
        month = now.month

        cal = calendar.TextCalendar(calendar.SUNDAY)

        year_month = cal.formatmonthname(year, month, width=0)

        days_of_month = [day for day in cal.itermonthdays(year, month) if day != 0]

        eventos = Evento.objects.filter(data__year=year, data__month=month)
        
        desired_locale = Locale('pt_BR')
        data_atual= datetime.today()
        
        mes_atual_str = format_date(data_atual, format='MMMM', locale=desired_locale)
        
        dias_com_agendamentos = []

        for evento in eventos:
            if evento.servidor:
                dias_com_agendamentos.append(evento.data.day)
                 
        

        dias_com_agendamentos = list(set(dias_com_agendamentos))
        
        context = {
            'year_month' : year_month ,
            'days_of_month':days_of_month,
            'eventos' : eventos,
            'mes_atual_str':mes_atual_str,
            'dias_com_agendamentos':dias_com_agendamentos,
            }
        

        return render(request,'home.html',context)