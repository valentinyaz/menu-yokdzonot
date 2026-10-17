"""Genera las fotos ligeras del menú a partir de fotos/originales/.

  fotos/<nombre>.jpg       800 px, para la vista ampliada (se baja solo al tocar)
  fotos/mini/<nombre>.jpg  200x200 recortada, la que se ve en la lista

  originales/cenote.jpg es especial (mural panorámico de la portada):
  fotos/portada.jpg (1800 px, computadora) y fotos/portada-celular.jpg (recorte central)

Uso: python herramientas/optimizar_fotos.py   (requiere Pillow)
"""
from pathlib import Path
from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent.parent / "fotos"
ORIG = RAIZ / "originales"
MINI = RAIZ / "mini"
MINI.mkdir(exist_ok=True)

for src in sorted(ORIG.glob("*.jp*g")):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    nombre = src.stem + ".jpg"

    if src.stem == "cenote":
        W, H = im.size
        ancho = round(H * 1.78)  # recorte central para celular
        x = max(0, min(W - ancho, round(W * 0.43) - ancho // 2))
        cel = im.crop((x, 0, x + ancho, H)).resize((900, round(900 * H / ancho)), Image.LANCZOS)
        cel.save(RAIZ / "portada-celular.jpg", "JPEG", quality=66, optimize=True, progressive=True)
        pc = im.resize((1800, round(1800 * H / W)), Image.LANCZOS)
        pc.save(RAIZ / "portada.jpg", "JPEG", quality=66, optimize=True, progressive=True)
        print("portada.jpg / portada-celular.jpg listas")
        continue

    grande = im.copy()
    grande.thumbnail((800, 800), Image.LANCZOS)
    grande.save(RAIZ / nombre, "JPEG", quality=68, optimize=True, progressive=True)

    mini = ImageOps.fit(im, (200, 200), Image.LANCZOS)
    mini.save(MINI / nombre, "JPEG", quality=62, optimize=True, progressive=True)

    print(f"{nombre:28} grande {(RAIZ / nombre).stat().st_size // 1024:4} KB   mini {(MINI / nombre).stat().st_size // 1024:3} KB")
