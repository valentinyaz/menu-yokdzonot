#!/bin/zsh
# Exporta materiales/*.html a PDF (y PNG los digitales). Requiere el servidor local en :8765
# (preview "menu") y Google Chrome.
set -e
cd "$(dirname "$0")/.."
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
B="http://localhost:8765/materiales"
for f in letrero-entrada redes-sociales centro-de-mesa correo whatsapp; do
  "$CH" --headless=new --disable-gpu --no-pdf-header-footer --virtual-time-budget=6000 \
    --print-to-pdf="materiales/$f.pdf" "$B/$f.html" 2>/dev/null
done
png() { "$CH" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=6000 \
  --window-size=$2 --force-device-scale-factor=${3:-1} --screenshot="materiales/$1.png" "$B/$1.html" 2>/dev/null; }
png redes-sociales 1080,1080
png whatsapp 1080,1350
png correo 600,1130 2
ls -lh materiales/*.pdf materiales/*.png
