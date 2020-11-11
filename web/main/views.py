from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  # return HttpResponse(f'hello world')
  return render(request, 'blog/index.html', {})