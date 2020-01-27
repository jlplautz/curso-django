from django.shortcuts import render


# Create your views here.

# No file views.py da app aperitivos  criar uma função chamada video que vai receber
# o request que vai rendenrizar  a pagina do meu video.


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', 386792293),
    Video('instalacao-windows', 'Instalação Wndows', 387145176),
]


videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
