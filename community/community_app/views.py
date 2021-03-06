#from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
#from community_app.models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import *
#from community_app.models import Service

# Create your views here.
def index(request):
    data={
        'name':'rushi',
        'age' : 23,
        'location' : 'mumbai'
    }
    return render(request, 'index.html',data)

def register(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return redirect('home')
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username taken!')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'email already exist.')
            return redirect('register')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Successfully Registered!')
            return redirect('register')
    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def service(request):
    service_list = Service.objects.all()
    return render(request, 'service.html', {'service_list': service_list})

def add_service(request):
    if request.method == "POST":
        service_name = request.POST['service_name']
        service_provider = request.POST['service_provider']
        price = request.POST['price']
        contact_no = request.POST['contact_no']
        Service.objects.create(service_name=service_name, service_provider_name=service_provider, price=price,
                               contact_no=contact_no, posted_by=request.user)
        return redirect('service')
    return render(request, 'add_service.html')


def queries(request):
    query_list = Query.objects.filter(approved=True)
    print(query_list)
    return render(request,'queries.html' , {'query_list': query_list})

def ask_question(request):
    if request.method == "POST":
        category = request.POST['category']
        question = request.POST['question']
        Query.objects.create(que_category=category, question=question, posted_by=request.user)
        messages.success(request, "We received your query, It will be live here after it will be approved by the authorised staff. ")
        return redirect('queries')
    return render(request, 'ask_question.html')

def discussion(request, pk):
    que = get_object_or_404(Query, pk=pk)
    que_id = que.id
    answer_list = Answer.objects.filter(que_id=que.id)
    if request.method == "POST":
        answer = request.POST['answer']
        Answer.objects.create(que_id=que_id, answer=answer, posted_by=request.user)
        return redirect('discussion', pk=pk)
    return render(request, 'discussion.html', {'que': que, 'answers': answer_list})



def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        Contact.objects.create(name=name, email=email, phone=phone, desc=desc)
        return redirect('contact')
    return render(request,'contact.html')

def about(request):
    return render(request, 'about.html')




