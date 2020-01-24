from django.shortcuts import render


# Create your views here.

# No file views.py da app aperitivos  criar uma função chamada video que vai receber
# o request que vai rendenrizar  a pagina do meu video.

def video(request, slug):
    return render(request, 'aperitivos/video.html')
