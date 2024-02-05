from django.shortcuts import render

# Create your views here.
def fun1(request):
  title = 'templates'
  # data = [123,234,'applw','wefww']
  data = {'a':'apple','b':'ball','c':'cat','d':'dog','title':title}  
  return render(request,'Tapp2.html',{'mydata' : data} )


