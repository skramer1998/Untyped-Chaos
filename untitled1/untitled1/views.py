from django.shortcuts import render
from django.views import View
from untitled1.models import YourClass # replace with driver when we have one written
# Create your views here.
class Home(View):
  def get(self,request):
    return render(request, 'main/index.html')
  def post(self,request):
    yourInstance = YourClass()
    commandInput = request.POST["command"]
    if commandInput:
      response = yourInstance.command(commandInput)
    else:
      response = ""
    return render(request, 'main/index.html',{"message":response})