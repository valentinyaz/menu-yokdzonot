"""Genera las fotos ligeras del menú a partir de fotos/originales/.

  fotos/<nombre>.jpg       800 px, para la vista ampliada (se baja solo al tocar)
  fotos/mini/<nombre>.jpg  200x200 recortada, la que se ve en la lista

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

    grande = im.copy()
    grande.thumbnail((800, 800), Image.LANCZOS)
    grande.save(RAIZ / nombre, "JPEG", quality=68, optimize=True, progressive=True)

    mini = ImageOps.fit(im, (200, 200), Image.LANCZOS)
    mini.save(MINI / nombre, "JPEG", quality=62, optimize=True, progressive=True)

    print(f"{nombre:28} grande {(RAIZ / nombre).stat().st_size // 1024:4} KB   mini {(MINI / nombre).stat().st_size // 1024:3} KB")
