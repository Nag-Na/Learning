from django.shortcuts import render

# Create your views here.
def function(request):
  # title = 'main page'
  # numbers = [10,20,30,40,50]    # we couldn't access it, we must have arrange them in single dict 
  
  # languages = ['php','python','java']
  
    # title = 'main page'
    # nbrs = [10,20,30,40,50]    
    # lang = ['php','python','java'] # not only list , use tuples also
  
    return render(request,'Tapp1.html',{'a':'apple','b':'ball','c':'cat','d':'dog'}) #,'title':title,'numbers':nbrs,'languages':lang