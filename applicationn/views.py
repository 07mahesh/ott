from django.shortcuts import render, redirect
from .models import Movie
from applicationn.forms import MovieForm
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# def page_request(request):
#     total_pages = Movie.objects.all()
#     no_pages = Paginator(total_pages, 4)
#     page_number = request.GET.get('page')
#     page_obj = no_pages.get_page(page_number)
    
#     return render(request, 'htmlfiles/home.html', {'page_obj': page_obj})



from django.core.paginator import Paginator

def home(request):
    # model1 = Movie.objects.filter(rating__gte=5).order_by('-rating')[:2]
    model1 = Movie.objects.filter(rating__gte=5).order_by('?') # for random elements
    total_pages = Movie.objects.all()
    page = Paginator(total_pages, 2)
    page_num = request.GET.get('page')
    page_obj = page.get_page(page_num)
    return render(request, 'htmlfiles/home.html', {'model1': model1, 'page_obj': page_obj})

from django.shortcuts import render


def search_movie(request):
    if request.method =="POST":
        search= request.POST.get('search')
        search_model=Movie.objects.filter(moviename__icontains=search)   
    return render(request,'htmlfiles/search_movie.html',{'search':search ,'search_model':search_model} )




def stored_movies(request):
    model = Movie.objects.all().order_by('-rating')
    return render(request, 'htmlfiles/stored_movies.html', {'model': model})



from django.shortcuts import render, redirect
from .forms import MovieForm

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MovieForm()
    return render(request, 'htmlfiles/add_movie.html', {'form': form})



def view_movie_details(request,pk):
    model2=Movie.objects.get(pk=pk)
    return render(request,'htmlfiles/details.html',{'model2':model2})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm

def update_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form2 = MovieForm(request.POST, request.FILES, instance=movie)
        if form2.is_valid():
            form2.save()
            return redirect('/')
    else:
        form2 = MovieForm(instance=movie)
    return render(request, 'htmlfiles/update.html', {'form2': form2})



def delete_movie(request,pk):
    model3=Movie.objects.get(pk=pk)
    model3.delete()
    return redirect('/')




from django.contrib import messages
def register_user(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'username is alredy exists...')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.error(request,'email alredy exists....')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,'register successfully...')
                return redirect('login_user')
        else:
            messages.error(request,'invalid password...')
            return redirect('register')
    else:
        return render(request,'htmlfiles/register.html')
    



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  
            print("Login Successfully...!")
            return redirect('home')
        else:
            print("Invalid Credentials....!")
            return redirect('user_login')
    else:
        return render(request, 'htmlfiles/login.html')









def logout_user(request):
    if request.method == 'POST':
        logout(request)
        print("logout succesfully....")
    return redirect("home")










