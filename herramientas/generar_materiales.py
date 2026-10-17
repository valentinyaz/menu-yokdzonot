"""Genera los materiales impresos y digitales del menú (HTML listo para exportar a PDF/PNG).

  materiales/letrero-entrada.html   45 x 60 cm, para tabla colgante
  materiales/redes-sociales.html    1080 x 1080 px (post Instagram / Facebook)
  materiales/centro-de-mesa.html    hoja carta horizontal, se dobla a la mitad
  materiales/correo.html            600 px de ancho (ancho estándar de correo)
  materiales/whatsapp.html          1080 x 1350 px (vertical)

Uso: python herramientas/generar_materiales.py   (luego herramientas/exportar_materiales.sh)
"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
OUT = RAIZ / "materiales"
OUT.mkdir(exist_ok=True)

URL = "https://valentinyaz.github.io/menu-yokdzonot/"
URL_CORTA = "valentinyaz.github.io/menu-yokdzonot"

svg = (RAIZ / "qr" / "qr-menu-yokdzonot.svg").read_text()
QR = svg[svg.index("<svg"):].replace('width="41mm" height="41mm"', 'class="qr-svg"').replace("<path ", '<path fill="#0b3d4a" ')

PIRAMIDE = "M0 14V12H4V9H8V6H12V3H15V0H21V3H24V6H28V9H32V12H36V14Z"


def piramides(color):
    c = color.replace("#", "%23")
    return (f"url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='36' height='14'%3E"
            f"%3Cpath d='{PIRAMIDE}' fill='{c}'/%3E%3Crect x='16.5' y='3' width='3' height='3' fill='%23d9a441'/%3E%3C/svg%3E\")")


ORNAMENTO = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='34' height='12'%3E"
             "%3Cpath d='M0 6H10M24 6H34' stroke='%23d9a441' stroke-width='1.5'/%3E%3Cpath d='M17 0L23 6L17 12L11 6Z' fill='%23d9a441'/%3E"
             "%3Cpath d='M17 3.5L19.5 6L17 8.5L14.5 6Z' fill='%2314211e'/%3E%3C/svg%3E\")")
GRECA = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='32' height='12'%3E"
         "%3Cpath d='M0 12V8H4V4H8V0H12V4H16V8H20V12' fill='none' stroke='%23d9a441' stroke-width='1.6'/%3E"
         "%3Cpath d='M16 0V4H20V8H24V12H28V8H32V4' fill='none' stroke='%232595b3' stroke-width='1.6'/%3E%3C/svg%3E\")")
TEXTURA = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E"
           "%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/%3E"
           "%3CfeColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .05 0'/%3E%3C/filter%3E"
           "%3Crect width='160' height='160' filter='url(%23n)'/%3E%3C/svg%3E\")")

BASE = f"""
@font-face {{ font-family: "Fraunces"; font-weight: 100 900; src: url(../fuentes/fraunces-latin.woff2) format("woff2"); }}
@font-face {{ font-family: "Outfit"; font-weight: 100 900; src: url(../fuentes/outfit-latin.woff2) format("woff2"); }}
:root {{
  --obsidiana: #14211e; --jade: #0f5a4a; --azul-maya: #2595b3; --azul-claro: #9fe0e6;
  --oro: #d9a441; --oro-claro: #f1d08a; --achiote: #b8432a; --caliza: #ece2cc; --caliza-clara: #f8f2e5;
}}
* {{ box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
html, body {{ margin: 0; padding: 0; background: #fff; }}
body {{ font-family: Outfit, sans-serif; color: #fff; }}
h1, h2, h3, p {{ margin: 0; }}
.pagina {{ position: relative; overflow: hidden; background: var(--obsidiana) {TEXTURA}; }}
.mural {{ display: block; width: 100%; object-fit: cover; }}
.piramides {{ background: {piramides('#14211e')} repeat-x left bottom; position: relative; }}
.piramides.jade {{ background-image: {piramides('#0f5a4a')}; }}
.greca {{ background: {GRECA} repeat-x center; }}
.orn {{ display: flex; align-items: center; justify-content: center; }}
.orn::before, .orn::after {{ content: ""; flex: none; background: {ORNAMENTO} no-repeat center / contain; }}
.oro {{ color: var(--oro-claro); }}
.kicker {{ text-transform: uppercase; color: var(--azul-claro); font-weight: 600; }}
.serif {{ font-family: Fraunces, Georgia, serif; }}
.qr {{ background: #fff; display: inline-block; line-height: 0; }}
.qr-svg {{ width: 100%; height: 100%; display: block; }}
.foto {{ object-fit: cover; display: block; }}
"""


def pagina(nombre, titulo, ancho, alto, css, cuerpo):
    html = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>{titulo} · Cenote Yokdzonot</title>
<style>
@page {{ size: {ancho} {alto}; margin: 0; }}
{BASE}
.pagina {{ width: {ancho}; height: {alto}; }}
{css}
</style></head><body>
{cuerpo}
</body></html>"""
    (OUT / nombre).write_text(html)
    print("listo", nombre)


# ---------------------------------------------------------------- letrero de entrada 45 x 60 cm
pagina("letrero-entrada.html", "Letrero de entrada", "450mm", "600mm", """
.cab { height: 92mm; display: flex; flex-direction: column; align-items: center; justify-content: center; padding-top: 14mm; }
.cab .kicker { font-size: 9mm; letter-spacing: .35em; }
.cab h1 { font-size: 30mm; font-weight: 800; line-height: 1; margin-top: 3mm; letter-spacing: .02em; }
.cab h1.orn { gap: 9mm; }
.cab h1.orn::before, .cab h1.orn::after { width: 34mm; height: 12mm; }
.argolla { position: absolute; top: 14mm; width: 16mm; height: 16mm; border-radius: 50%;
  border: 2.2mm solid var(--oro); background: var(--obsidiana); box-shadow: 0 0 0 1mm rgba(0,0,0,.4); }
.argolla.izq { left: 22mm; } .argolla.der { right: 22mm; }
.mural { height: 230mm; }
.piramides { height: 16mm; margin-top: -16mm; background-size: 41mm 16mm; }
.cuerpo { text-align: center; padding: 12mm 30mm 0; }
.cuerpo .lema { font-size: 11mm; color: #d5ddd8; }
.cuerpo h2 { font-size: 21mm; font-weight: 800; margin-top: 8mm; }
.cuerpo .en { font-size: 9mm; color: var(--azul-claro); margin-top: 2mm; }
.marco { margin: 9mm auto 0; width: 150mm; padding: 5mm; border-radius: 9mm; background: var(--oro); }
.marco .qr { width: 140mm; height: 140mm; padding: 9mm; border-radius: 6mm; }
.url { font-size: 7.4mm; color: var(--oro-claro); margin-top: 6mm; letter-spacing: .02em; }
.pie { position: absolute; left: 0; right: 0; bottom: 0; height: 14mm; }
""", f"""
<div class="pagina">
  <span class="argolla izq"></span><span class="argolla der"></span>
  <div class="cab">
    <span class="kicker">Yokdzonot · Yucatán</span>
    <h1 class="serif oro orn">Restaurante</h1>
  </div>
  <img class="mural" src="mural-169.jpg" alt="">
  <div class="piramides"></div>
  <div class="cuerpo">
    <p class="lema">Cocina yucateca a la orilla del cenote</p>
    <h2 class="serif oro">Escanea nuestro menú</h2>
    <p class="en">Scan for our menu · Español / English</p>
    <div class="marco"><div class="qr">{QR}</div></div>
    <p class="url">{URL_CORTA}</p>
  </div>
  <div class="pie greca" style="background-size: 32mm 12mm"></div>
</div>
""")

# ---------------------------------------------------------------- redes sociales 1080 x 1080
FOTOS = [("poc-chuc", "Poc Chuc"), ("panuchos", "Panuchos"), ("guacamole", "Guacamole")]
circulos = "".join(f'<figure><img class="foto" src="../fotos/{f}.jpg" alt=""><figcaption class="serif">{n}</figcaption></figure>' for f, n in FOTOS)

pagina("redes-sociales.html", "Post redes sociales", "1080px", "1080px", """
.mural { height: 400px; }
.piramides { height: 26px; margin-top: -26px; background-size: 67px 26px; }
.cuerpo { text-align: center; padding: 30px 60px 0; }
.cuerpo .kicker { font-size: 20px; letter-spacing: .32em; }
.cuerpo h1 { font-size: 66px; font-weight: 800; line-height: 1.05; margin-top: 10px; }
.platos { display: flex; justify-content: center; gap: 46px; margin-top: 30px; }
figure { margin: 0; }
figure img { width: 170px; height: 170px; border-radius: 50%; border: 6px solid var(--oro); }
figcaption { margin-top: 10px; font-size: 26px; font-weight: 700; color: #fff; }
.abajo { position: absolute; left: 0; right: 0; bottom: 0; height: 190px; background: var(--jade);
  display: flex; align-items: center; justify-content: center; gap: 36px; padding: 0 60px; }
.abajo .qr { width: 150px; height: 150px; padding: 10px; border-radius: 14px; border: 4px solid var(--oro); }
.abajo .txt { text-align: left; }
.abajo .txt b { display: block; font: 800 38px Fraunces, serif; color: var(--oro-claro); }
.abajo .txt span { display: block; font-size: 25px; color: #e6f1ec; margin-top: 6px; }
.techo { position: absolute; left: 0; right: 0; bottom: 190px; height: 26px; background-size: 67px 26px; }
""", f"""
<div class="pagina">
  <img class="mural" src="mural-ancho.jpg" alt="">
  <div class="piramides"></div>
  <div class="cuerpo">
    <span class="kicker">Restaurante · Yokdzonot, Yucatán</span>
    <h1 class="serif oro">Nuestro menú<br>ahora es digital</h1>
    <div class="platos">{circulos}</div>
  </div>
  <div class="techo piramides jade"></div>
  <div class="abajo">
    <div class="qr">{QR}</div>
    <div class="txt"><b>Escanea o visita</b><span>{URL_CORTA}</span></div>
  </div>
</div>
""")

# ---------------------------------------------------------------- centro de mesa (carta horizontal, se dobla)
cara = f"""
<div class="cara {{pos}}">
  <img class="mural" src="mural-ancho.jpg" alt="">
  <div class="lado">
    <span class="kicker">Yokdzonot · Yucatán</span>
    <h2 class="serif oro">Escanea el menú</h2>
    <p class="en">Scan for our menu · ES / EN</p>
    <div class="qr">{QR}</div>
    <p class="url">{URL_CORTA}</p>
  </div>
</div>"""
pagina("centro-de-mesa.html", "Centro de mesa", "279.4mm", "215.9mm", """
.pagina { background: #fff; }
.cara { position: absolute; left: 0; right: 0; height: 107.95mm; display: flex; overflow: hidden;
  background: var(--obsidiana) """ + TEXTURA + """; }
.cara.arriba { top: 0; transform: rotate(180deg); }
.cara.abajo { bottom: 0; }
.cara .mural { width: 150mm; height: 100%; object-fit: cover; object-position: 45% 50%; }
.lado { flex: 1; text-align: center; padding: 7mm 6mm 0; position: relative; }
.lado { border-left: 1.6mm solid var(--oro); }
.lado .kicker { font-size: 2.8mm; letter-spacing: .3em; }
.lado h2 { font-size: 8.4mm; font-weight: 800; margin-top: 1.5mm; }
.lado .en { font-size: 3.2mm; color: var(--azul-claro); margin-top: .5mm; }
.lado .qr { width: 52mm; height: 52mm; padding: 3mm; border-radius: 3mm; margin-top: 4mm; box-shadow: 0 0 0 1.4mm var(--oro); }
.lado .url { font-size: 2.6mm; color: var(--oro-claro); margin-top: 3mm; }
.doblez { position: absolute; left: 0; right: 0; top: 107.95mm; border-top: .3mm dashed #999; z-index: 2; }
.doblez span { position: absolute; right: 4mm; top: -3.6mm; font-size: 2.4mm; color: #999; background: #fff; padding: 0 1mm; }
""", f"""
<div class="pagina">
  {cara.replace("{pos}", "arriba")}
  {cara.replace("{pos}", "abajo")}
  <div class="doblez"><span>doblar aquí</span></div>
</div>
""")

# ---------------------------------------------------------------- correo 600 px
fotos_correo = "".join(f'<td><img class="foto" src="../fotos/{f}.jpg" alt="{n}"><span class="serif">{n}</span></td>' for f, n in FOTOS)
pagina("correo.html", "Correo", "600px", "1130px", """
.mural { height: 338px; }
.piramides { height: 16px; margin-top: -16px; background-size: 41px 16px; }
.cuerpo { text-align: center; padding: 26px 40px 0; }
.cuerpo .kicker { font-size: 12px; letter-spacing: .3em; }
.cuerpo h1 { font-size: 36px; font-weight: 800; line-height: 1.1; margin-top: 8px; }
.cuerpo .orn { gap: 12px; margin-top: 14px; }
.cuerpo .orn::before { width: 60px; height: 14px; }
.cuerpo .orn::after { display: none; }
.cuerpo p { font-size: 16px; line-height: 1.5; color: #d5ddd8; margin-top: 10px; }
.boton { display: inline-block; margin-top: 22px; background: var(--oro); color: var(--obsidiana); text-decoration: none;
  font: 700 18px Outfit, sans-serif; padding: 15px 34px; border-radius: 12px; }
table { width: 100%; table-layout: fixed; border-spacing: 12px 0; margin-top: 26px; }
td { text-align: center; vertical-align: top; }
td img { width: 150px; height: 150px; margin: 0 auto; border-radius: 12px; border: 3px solid var(--oro); }
td span { display: block; font-size: 15px; font-weight: 700; margin-top: 6px; }
.qrfila { display: flex; align-items: center; justify-content: center; gap: 18px; margin-top: 26px; }
.qrfila .qr { width: 104px; height: 104px; padding: 7px; border-radius: 10px; }
.qrfila span { text-align: left; font-size: 14px; color: #d5ddd8; }
.pie { position: absolute; left: 0; right: 0; bottom: 0; height: 64px; background: var(--jade);
  display: flex; align-items: center; justify-content: center; font-size: 13px; color: var(--azul-claro); }
.pie i { font-family: Fraunces, serif; color: #fff; margin-right: 6px; }
.techo { position: absolute; left: 0; right: 0; bottom: 64px; height: 16px; background-size: 41px 16px; }
""", f"""
<div class="pagina">
  <img class="mural" src="mural-169.jpg" alt="Cenote Yokdzonot">
  <div class="piramides"></div>
  <div class="cuerpo">
    <span class="kicker">Restaurante · Yokdzonot, Yucatán</span>
    <h1 class="serif oro">Nuestro menú ya está<br>en tu celular</h1>
    <div class="orn"></div>
    <p>Poc chuc, panuchos, salbutes, sopa de lima y aguas frescas de chaya.<br>Consulta platillos, fotos y precios en español o inglés.</p>
    <a class="boton" href="{URL}">Ver el menú →</a>
    <table><tr>{fotos_correo}</tr></table>
    <div class="qrfila"><div class="qr">{QR}</div><span>¿Estás en la computadora?<br>Escanea con tu celular.</span></div>
  </div>
  <div class="techo piramides jade"></div>
  <div class="pie"><i>Yok'ts'ono'ot</i> «sobre el cenote» en lengua maya</div>
</div>
""")

# ---------------------------------------------------------------- whatsapp 1080 x 1350
pagina("whatsapp.html", "WhatsApp", "1080px", "1350px", """
.mural { height: 607px; }
.piramides { height: 26px; margin-top: -26px; background-size: 67px 26px; }
.cuerpo { text-align: center; padding: 34px 60px 0; }
.cuerpo .kicker { font-size: 21px; letter-spacing: .32em; }
.cuerpo h1 { font-size: 74px; font-weight: 800; line-height: 1.04; margin-top: 12px; }
.platos { display: flex; justify-content: center; gap: 50px; margin-top: 34px; }
figure { margin: 0; }
figure img { width: 180px; height: 180px; border-radius: 50%; border: 6px solid var(--oro); }
figcaption { margin-top: 10px; font-size: 27px; font-weight: 700; color: #fff; }
.abajo { position: absolute; left: 0; right: 0; bottom: 0; height: 200px; background: var(--jade);
  display: flex; align-items: center; justify-content: center; gap: 36px; padding: 0 60px; }
.abajo .qr { width: 150px; height: 150px; padding: 10px; border-radius: 14px; border: 4px solid var(--oro); }
.abajo .txt { text-align: left; }
.abajo .txt b { display: block; font: 800 40px Fraunces, serif; color: var(--oro-claro); }
.abajo .txt span { display: block; font-size: 27px; color: #e6f1ec; margin-top: 6px; }
.techo { position: absolute; left: 0; right: 0; bottom: 200px; height: 26px; background-size: 67px 26px; }
""", f"""
<div class="pagina">
  <img class="mural" src="mural-169.jpg" alt="">
  <div class="piramides"></div>
  <div class="cuerpo">
    <span class="kicker">Restaurante · Yokdzonot, Yucatán</span>
    <h1 class="serif oro">Mira nuestro menú<br>desde tu celular</h1>
    <div class="platos">{circulos}</div>
  </div>
  <div class="techo piramides jade"></div>
  <div class="abajo">
    <div class="qr">{QR}</div>
    <div class="txt"><b>Toca el enlace del mensaje</b><span>{URL_CORTA}</span></div>
  </div>
</div>
""")
