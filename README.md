# Portafolio — página única

Página estática que enlaza los tres demos funcionales de Pablo Cariaga:

- **[camara-a-telegram](../camara-a-telegram)** — evento de cámara → foto en Telegram → registro.
- **[seguimiento-de-precios](../seguimiento-de-precios)** — scraper programado con GitHub Actions y sitio en Pages.
- **[analizador-de-accesos](../analizador-de-accesos)** — análisis de CSV de accesos 100% en el navegador.

Sin backend, sin dependencias de build: es HTML + CSS plano, listo para GitHub Pages.

## Antes de publicar (importante)

Los enlaces usan el placeholder `TU-USUARIO`. Reemplazalo por tu usuario real de
GitHub antes de pushear:

```powershell
# en esta carpeta
(Get-Content index.html) -replace 'TU-USUARIO', '<tu-usuario>' | Set-Content index.html
```

Los enlaces a los "sitios del demo" (`TU-USUARIO.github.io/...`) solo funcionan
una vez que cada repo esté publicado y con GitHub Pages activado (carpeta `docs/`
o raíz según corresponda).

## Qué es real y qué es simulado

| Elemento | Estado |
|---|---|
| Textos y descripciones de los demos | Reales: describen lo que cada repo hace y prueba |
| Resumen de Pablo | Real, provisto por él |
| Enlaces a repos/sitios | Funcionan al publicar; hoy llevan placeholder |
| Capturas de pantalla | No hay (la página se prueba con Playwright, ver `tests/`) |
| Testimonios, números de clientes, logos | No existen y no se inventan |

## Probar en local

```powershell
python -m http.server 8080
# abrir http://localhost:8080
```

## Tests

```powershell
python -m venv .venv
.\.venv\Scripts\pip install -r requirements-dev.txt
.\.venv\Scripts\python -m pytest tests/
```

Los tests usan Chrome instalado vía Playwright (`channel="chrome"`).

## Licencia

MIT — ver [LICENSE](LICENSE).
