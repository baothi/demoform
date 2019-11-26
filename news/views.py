from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View

# Create your views here.

# def index(request):
#     return HttpResponse("xin chao")

class IndexClass(View):
    """docstring for ClassName"""
    def get(self, request):
        ketqua = "12323345"
        return HttpResponse(ketqua)
        

# def add_post(request):
#     # return HttpResponse("them bai viet")
#     a = PostForm()
#     return render(request, 'news/add_news.html',{'f':a })

class PostClass(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html',{'f':a })

class ClassSaveNews(View):
    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('luu ok')
        else:
            return HttpResponse('khong duoc validate')

def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f': b})

def process_email(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid():
            # tieude = m.cleaned_data['title']
            # cc = m.cleaned_data['cc']
            # noidung = m.cleaned_data['content']
            # email = m.cleaned_data['email']
            # context = { 'td':tieude, 'c':cc, 'nd':noidung, 'email':email}
            # return render(request, 'news/print_email.html', context)
            context2 = {'email_data':m}
            return render(request, 'news/print_email.html', context2)
        else:
        	return HttpResponse('form no valid')
    else:
    	return HttpResponse('khong phai post server')
