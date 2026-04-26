import os
from pathlib import Path

def count_files(directory, extensions=('.jpg', '.jpeg', '.png')):
    path = Path(directory)
    if not path.exists():
        return 0
    return len([f for f in path.iterdir() if f.is_file() and f.suffix.lower() in extensions])

def update_readme(stats):
    readme_path = Path("README.md")
    if not readme_path.exists():
        print("No se encontró README.md")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    skip = False
    
    # Buscamos la sección de estadísticas para actualizarla
    for line in lines:
        if "## 📊 Estadísticas" in line:
            new_lines.append(line)
            new_lines.append(f"\n* **PlayStation 1:** {stats['PS1']} portadas\n")
            new_lines.append(f"* **PlayStation 2:** {stats['PS2']} portadas\n")
            new_lines.append(f"* **Total:** {stats['PS1'] + stats['PS2']} archivos\n")
            skip = True
        elif skip and line.startswith("##"): # Detener el salto cuando llegue a la siguiente sección
            new_lines.append("\n" + line)
            skip = False
        elif not skip:
            new_lines.append(line)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("✅ README.md actualizado con nuevas estadísticas.")

def main():
    # Rutas basadas en tu estructura
    base_path = Path(__file__).parent.resolve()
    
    stats = {
        "PS1": count_files(base_path / "covers" / "DSPS1_2D"),
        "PS2": count_files(base_path / "covers" / "PS2_2D")
    }
    
    print(f"PS1: {stats['PS1']} | PS2: {stats['PS2']}")
    update_readme(stats)

if __name__ == "__main__":
    main()