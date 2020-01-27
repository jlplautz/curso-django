from django.shortcuts import render


# Create your views here.

# No file views.py da app aperitivos  criar uma função chamada video que vai receber
# o request que vai rendenrizar  a pagina do meu video.

videos = [
    {'slug': 'motivacao', 'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 386792293},
    {'slug': 'instalacao-windows', 'titulo': 'Instalação Wndows', 'vimeo_id': 387145176},
]


videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
