# Fotos del menú

1. Pon la foto original (cualquier tamaño) en `fotos/originales/` con el nombre del
   platillo, ej. `poc-chuc.jpg`. Esa carpeta no se publica.
2. Corre `python herramientas/optimizar_fotos.py` (requiere Pillow). Genera:
   - `fotos/<nombre>.jpg`: 800 px, ~50–80 KB. Solo se baja al tocar la foto.
   - `fotos/mini/<nombre>.jpg`: 200×200, ~7 KB. Es la que se ve en la lista.
3. Agrega `foto: "fotos/<nombre>.jpg"` al platillo en `menu-data.js`.

- `cenote.jpg` → si existe, reemplaza la ilustración de la portada automáticamente.
- Si una foto no existe o falla, se muestra el recuadro "Foto próximamente".
