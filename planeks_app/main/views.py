import time

from django.http import FileResponse
from django.shortcuts import render, redirect
from rest_framework import generics
from django.contrib.auth import logout
from rest_framework import permissions
from celery.result import AsyncResult
from .tasks import make_file
from .models import CeleryStatus


# Create your views here.
class Mains(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        log_out = request.GET.get('logout')
        """ start celery app"""
        if request.GET.get('rows'):
            req = int(request.GET.get('rows'))
            task = make_file.delay(req=req)
            task_id = task.id
            status = AsyncResult(task_id).ready()
            CeleryStatus.objects.create(status=task_id)
            data = {'res': status}
            return render(request, 'main/main.html', data)
        """download csv"""
        if request.GET.get('download'):
            filename = '/Users/priest/PycharmProjects/PLANEKS/planeks_app/csv_files/my_file.csv'
            response = FileResponse(open(filename, 'rb'))
            return response

        """logout"""
        if log_out == 'logout':
            logout(request)
            return redirect('login')
        user = str(request.user)
        message = f'{user}'
        status = AsyncResult(f"{CeleryStatus.objects.all().last()}").ready()
        data = {'message': message,
                'res': status}
        return render(request, 'main/main.html', data)
