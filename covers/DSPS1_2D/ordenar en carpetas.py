import os
import re
import shutil

# ==========================
# CONFIG
# ==========================
CARPETA_ORIGEN = "."
CARPETA_DESTINO = "COVERS_ORDENADOS"

VARIANTES = [
    "_BG",
    "_COV",
    "_COV2",
    "_ICO",
    "_LAB",
    "_LGO",
    "_SCR",
    "_SCR2"
]

# ==========================
# EXTRAER ID BASE
# ==========================
def obtener_id_base(nombre):
    # captura algo tipo SCUS_973.99_BG o SLES_123.45
    match = re.match(r"([A-Z]{4}[_\-]?\d{3}\.\d{2})", nombre)
    if match:
        return match.group(1)
    return None

# ==========================
# CREAR CARPETA DESTINO
# ==========================
os.makedirs(CARPETA_DESTINO, exist_ok=True)

# ==========================
# PROCESO
# ==========================
for archivo in os.listdir(CARPETA_ORIGEN):
    ruta = os.path.join(CARPETA_ORIGEN, archivo)

    if not os.path.isfile(ruta):
        continue

    nombre_sin_ext = os.path.splitext(archivo)[0]

    id_base = obtener_id_base(nombre_sin_ext)

    if not id_base:
        continue

    # verificar si es variante válida o base
    es_valido = False
    for v in VARIANTES:
        if v in nombre_sin_ext or nombre_sin_ext == id_base:
            es_valido = True
            break

    if not es_valido:
        continue

    carpeta_final = os.path.join(CARPETA_DESTINO, id_base)
    os.makedirs(carpeta_final, exist_ok=True)

    destino = os.path.join(carpeta_final, archivo)

    print(f"Moviendo {archivo} → {id_base}")
    shutil.move(ruta, destino)

print("\n✔ Covers organizados estilo OPL real.")