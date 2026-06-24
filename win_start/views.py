from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

# def main_a(request):
#   template = loader.get_template('dy_html/a_main_page.html')
#   print('v111')
#   return HttpResponse(template.render())


# Create your views here.
def main_a(request):
 conttex={"bucket":"bucket"}
 print('v111')
 return render(request ,"dy_html/start_01.html",conttex) 