from django.shortcuts import render
from .models import TugasAkhir
from .forms import LoginForm



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home') #Ke halaman utama apabila berhasil login
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') #Ke halaman utama setelah login berhasil
            else:
                form.add_error(None, "Username atau Password salah wok")
    
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def tentang(request):
    return render(request, 'tentang.html')

def home(request):
    return render(request, 'home.html')
    
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