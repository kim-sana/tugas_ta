from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import TugasAkhir
from .forms import LoginForm
from .forms import CustomUserCreationForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home') 

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def tentang(request):
    return render(request, 'tentang.html')

@login_required
def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)  
    return redirect('login') 

def lihat_data(request):
    data = TugasAkhir.objects.all()
    return render(request, 'lihat_data.html', {'data': data})

def pencarian(request):
    query = request.GET.get('query', '')
    kategori = request.GET.get('kategori', 'nama')
    if query:
        if kategori == 'nama':
            hasil = TugasAkhir.objects.filter(nama__icontains=query)
        elif kategori == 'judul':
            hasil = TugasAkhir.objects.filter(judul__icontains=query)
        else:
            hasil = TugasAkhir.objects.all()
    else:
        hasil = []

    return render(request, 'pencarian.html', {'hasil': hasil, 'query': query})