"""Tests E2E del portafolio con Playwright (Chrome real, servidor local)."""

import functools
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def servidor():
    handler = functools.partial(SimpleHTTPRequestHandler, directory=str(RAIZ))
    srv = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    srv.RequestHandlerClass.log_message = lambda *a, **k: None
    hilo = threading.Thread(target=srv.serve_forever, daemon=True)
    hilo.start()
    yield f"http://127.0.0.1:{srv.server_address[1]}"
    srv.shutdown()


@pytest.fixture(scope="session")
def navegador():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        yield browser
        browser.close()


@pytest.fixture
def pagina(navegador, servidor):
    page = navegador.new_page()
    errores = []
    page.on("pageerror", lambda e: errores.append(str(e)))
    page.goto(servidor + "/index.html")
    page.wait_for_load_state("networkidle")
    yield page, errores
    page.close()


def test_carga_sin_errores_de_consola(pagina):
    page, errores = pagina
    assert "Pablo Cariaga" in page.title()
    assert errores == []


def test_los_tres_demos_estan_enlazados(pagina):
    page, _ = pagina
    for repo in ("camara-a-telegram", "seguimiento-de-precios", "analizador-de-accesos"):
        assert page.locator(f'a[href$="{repo}"]').count() >= 1


def test_el_resumen_de_pablo_y_la_honestidad_estan(pagina):
    page, _ = pagina
    texto = page.locator("main").inner_text()
    assert "15 años" in texto
    assert "Axessar" in texto
    assert "Platzi" in texto
    assert "no son sistemas de clientes" in texto
