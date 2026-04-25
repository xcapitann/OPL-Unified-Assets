from pathlib import Path
from PIL import Image, ImageOps

# --- CONFIGURACIÓN PARA TU REPO ---
TARGET_SIZE = (512, 736)  # Tamaño estándar de OPL Manager
# Carpetas que quieres procesar
SUB_FOLDERS = ["DSPS1_2D", "ARTOPL_PS2"] 
IGNORE_LOWER_RESOLUTION = False # Si es True, no agranda imágenes pequeñas (evita pixelado)

def procesar_directorio(covers_dir: Path):
    if not covers_dir.exists():
        print(f"⚠️ Saltando: {covers_dir.name} (No existe)")
        return

    print(f"🔍 Escaneando {covers_dir.name}...")
    
    # Buscamos imágenes con tamaño incorrecto
    invalid_list = []
    for p in covers_dir.iterdir():
        if p.suffix.lower() in (".jpg", ".jpeg", ".png"):
            try:
                with Image.open(p) as img:
                    if img.size != TARGET_SIZE:
                        invalid_list.append(p)
            except:
                continue

    if not invalid_list:
        print(f"✅ Todas las imágenes en {covers_dir.name} están perfectas.")
        return

    print(f"📍 Se encontraron {len(invalid_list)} imágenes para ajustar en {covers_dir.name}.")
    confirmar = input("¿Deseas procesarlas ahora? (s/n): ")
    
    if confirmar.lower() == 's':
        for p in invalid_list:
            try:
                with Image.open(p) as img:
                    img = ImageOps.exif_transpose(img)
                    # El método .fit recorta y ajusta sin estirar la imagen
                    new = ImageOps.fit(img, TARGET_SIZE, centering=(0.5, 0.5))
                    
                    # Convertir a RGB si es JPG (evita errores con transparencias)
                    if p.suffix.lower() in (".jpg", ".jpeg"):
                        new = new.convert("RGB")
                    
                    new.save(p, quality=90, optimize=True)
                    print(f"✔️ Ajustada: {p.name}")
            except Exception as e:
                print(f"❌ Error en {p.name}: {e}")

def main():
    # La ruta base es donde esté este script
    base_path = Path(__file__).parent.resolve()
    
    for folder in SUB_FOLDERS:
        ruta_completa = base_path / "covers" / folder
        procesar_directorio(ruta_completa)

if __name__ == "__main__":
    main()