import os
from pathlib import Path

# ==========================
# CONFIG GITHUB
# ==========================
USUARIO_GITHUB = "xcapitann"
REPO_NAME = "OPL-Unified-Assets"
BRANCH = "main"

# ==========================
# ESCANEAR CARPETAS (PS1/PS2)
# ==========================
def get_unique_games(directory):
    """
    Cada carpeta = 1 juego (ID PS2/PS1)
    """
    path = Path(directory)

    if not path.exists():
        return []

    juegos = set()

    for folder in path.iterdir():
        if folder.is_dir():
            juegos.add(folder.name)

    return sorted(list(juegos))

# ==========================
# ACTUALIZAR README + XML
# ==========================
def update_readme_and_xml(ps1_games, ps2_games):
    base_path = Path(__file__).parent.resolve()
    readme_path = base_path / "README.md"
    xml_path = base_path / "database.xml"

    raw_url = f"https://raw.githubusercontent.com/{USUARIO_GITHUB}/{REPO_NAME}/{BRANCH}"

    # ==========================
    # 1. README.md
    # ==========================
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

    # ==========================
    # 2. DATABASE.XML
    # ==========================
    with open(xml_path, "w", encoding="utf-8") as x:
        x.write('<?xml version="1.0" encoding="utf-8"?>\n')
        x.write('<UnifiedDatabase>\n')

        # ================= PS1 =================
        for g_id in ps1_games:
            folder = "covers/DSPS1_2D"

            x.write(f'   <Game id="{g_id}" platform="PS1">\n')
            x.write(f'      <Front>{raw_url}/{folder}/{g_id}_COV.jpg</Front>\n')
            x.write(f'      <Back>{raw_url}/{folder}/{g_id}_BACK.jpg</Back>\n')
            x.write(f'   </Game>\n')

        # ================= PS2 =================
        for g_id in ps2_games:
            folder = "covers/OPL_PS2"

            x.write(f'   <Game id="{g_id}" platform="PS2">\n')
            x.write(f'      <Front>{raw_url}/{folder}/{g_id}_COV.png</Front>\n')
            x.write(f'      <Back>{raw_url}/{folder}/{g_id}_BACK.png</Back>\n')
            x.write(f'      <Disc>{raw_url}/{folder}/{g_id}_ICO.png</Disc>\n')
            x.write(f'   </Game>\n')

        x.write('</UnifiedDatabase>')

    print(f"✅ database.xml generado con {len(ps1_games) + len(ps2_games)} juegos.")

# ==========================
# MAIN
# ==========================
def main():
    base_path = Path(__file__).parent.resolve()

    # rutas corregidas (CARPETAS)
    ps1_path = base_path / "covers" / "DSPS1_2D"
    ps2_path = base_path / "covers" / "OPL_PS2"

    ps1_ids = get_unique_games(ps1_path)
    ps2_ids = get_unique_games(ps2_path)

    print("📊 RESUMEN:")
    print(f"PS1: {len(ps1_ids)} juegos")
    print(f"PS2: {len(ps2_ids)} juegos")

    update_readme_and_xml(ps1_ids, ps2_ids)

# ==========================
# RUN
# ==========================
if __name__ == "__main__":
    main()