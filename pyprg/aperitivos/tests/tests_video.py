import pytest
from django.urls import reverse
from pyprg.django_assertions import assert_contains


# chamar esta fixture resp => porque vai ser gerada uma resposta http.
# def resp(client): => recebemos o client como dependencia
# utilizando o client vamos fazer uma chamada pra get vamos utilizar a função reverse do Django para calcular
# a URL reversa da minha api aperitivos/video. Esta app será diferente porque vou colocar no path dela um
# identificador unico para cada video  neste momente será somente 1,
# args indica os paramentos que vamos passar para esta url vamos definir a slug => com o nome do video
# este args é uma tupla e vamos finalizar com virgula esta resp vamos retornar como resultado da criação da fixture
# para todos os testes que utilizarem  a emulação da chamada get


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    '''
    teste code da aplicação que vai receber o resp como dependencia do meu teste e vamos no certificar
    que esta resposta retorna com status_code com valor 200 (status code de sucesso)
    '''
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1 class="mt-4 mb-3">Video Aperitivo: Motivação</h1>')


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/386792293"')
