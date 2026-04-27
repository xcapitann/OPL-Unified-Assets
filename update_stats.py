import os
from pathlib import Path

# --- CONFIGURACIÓN DE GITHUB ---
USUARIO_GITHUB = "xcapitann"  # Reemplaza con tu nombre de usuario real
REPO_NAME = "OPL-Unified-Assets"
BRANCH = "main"

def get_unique_games(directory):
    """Cuenta IDs únicos basados en el sufijo _COV para no contar archivos repetidos"""
    path = Path(directory)
    if not path.exists():
        return []
    # Solo tomamos los que terminan en _COV.jpg para identificar el juego
    return sorted([f.stem.replace("_COV", "") for f in path.iterdir() if f.name.endswith("_COV.jpg")])
    return sorted([f.stem.replace("_COV", "") for f in path.iterdir() if f.name.endswith("_COV.png")])

def update_readme_and_xml(ps1_games, ps2_games):
    base_path = Path(__file__).parent.resolve()
    readme_path = base_path / "README.md"
    xml_path = base_path / "database.xml"
    
    # URL base para los enlaces RAW de GitHub
    raw_url = f"https://raw.githubusercontent.com/{USUARIO_GITHUB}/{REPO_NAME}/{BRANCH}"

    # 1. ACTUALIZAR README.MD
    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        skip = False
        for line in lines:
            if "## 📊 Estadísticas" in line:
                new_lines.append(line)
                new_lines.append(f"\n* **PlayStation 1 (DuckStation):** `{len(ps1_games)}` Juegos únicos\n")
                new_lines.append(f"* **PlayStation 2 (OPL):** `{len(ps2_games)}` Juegos únicos\n")
                new_lines.append(f"* **Total de Títulos:** `{len(ps1_games) + len(ps2_games)}` en la colección\n")
                skip = True
            elif skip and line.startswith("##"):
                new_lines.append("\n" + line)
                skip = False
            elif not skip:
                new_lines.append(line)

        with open(readme_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("✅ README.md actualizado.")

    # 2. GENERAR DATABASE.XML (NUEVO)
    with open(xml_path, "w", encoding="utf-8") as x:
        x.write('<?xml version="1.0" encoding="utf-8"?>\n')
        x.write('<UnifiedDatabase>\n')
        
        # Procesar PS1
        x.write('   \n')
        for g_id in ps1_games:
            folder = "covers/DSPS1_2D"
            x.write(f'   <Game id="{g_id}" platform="PS1">\n')
            x.write(f'      <Front>{raw_url}/{folder}/{g_id}_COV.jpg</Front>\n')
            x.write(f'      <Back>{raw_url}/{folder}/{g_id}_BACK.jpg</Back>\n')
            x.write(f'   </Game>\n')

        # Procesar PS2
        x.write('   \n')
        for g_id in ps2_games:
            folder = "covers/OPL_PS2"
            x.write(f'   <Game id="{g_id}" platform="PS2">\n')
            x.write(f'      <Front>{raw_url}/{folder}/{g_id}_COV.png</Front>\n')
            x.write(f'      <Back>{raw_url}/{folder}/{g_id}_BACK.png</Back>\n')
            x.write(f'      <Disc>{raw_url}/{folder}/{g_id}_ICO.png</Disc>\n')
            x.write(f'   </Game>\n')
            
        x.write('</UnifiedDatabase>')
    print(f"✅ database.xml generado con {len(ps1_games) + len(ps2_games)} entradas.")

def main():
    base_path = Path(__file__).parent.resolve()
    
    # Obtenemos las listas de juegos reales
    ps1_ids = get_unique_games(base_path / "covers" / "DSPS1_2D")
    ps2_ids = get_unique_games(base_path / "covers" / "OPL_PS2")
    
    print(f"Resumen: PS1: {len(ps1_ids)} juegos | PS2: {len(ps2_ids)} juegos")
    
    update_readme_and_xml(ps1_ids, ps2_ids)

if __name__ == "__main__":
    main()