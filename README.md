# 🎮 OPL Unified Assets Cloud

## 📊 Estadísticas

* **PlayStation 1:** 50 Total de portadas
* **PlayStation 2:** 16 Total de portadas
* **Total:** 66 archivos

## 📁 Estructura del Repositorio

* `/covers`: Contiene todas las portadas de los juegos.
* `/database`: Contiene el archivo `database_ps1.json` con los nombres reales de los juegos.

---

## 🛠️ Estándar de Contribución (LEER ANTES DE SUBIR)

Para que la aplicación pueda reconocer tus aportaciones, es **obligatorio** seguir estas reglas de nomenclatura:

### 1. Nomenclatura de Portadas
Las imágenes deben guardarse en la carpeta `/covers` con el siguiente formato:
`[ID_DEL_JUEGO]_COV.[extensión]`

* **PS1/PS2 con punto decimal:** El ID debe llevar un punto antes de los últimos dos dígitos.
* **Ejemplo:** `SCUS_944.91_COV.jpg`
* **Formatos aceptados:** `.jpg`, `.png`

### 2. Formato del ID en la Base de Datos
Si vas a agregar un nombre al archivo `/database/database_ps1.json`, usa el ID **sin puntos**:
`"ID_LIMPIO": "Nombre Real del Juego"`

* **Ejemplo:** `"SCUS_94491": "Crash Bandicoot 3: Warped"`

---

## 🤝 Cómo colaborar

¡Tu ayuda es fundamental para completar la colección! Sigue estos pasos:

1.  **Fork:** Haz un fork de este repositorio en tu cuenta.
2.  **Subir archivos:** Sube tus portadas a la carpeta `/covers` de tu fork.
3.  **Pull Request:** Envía un Pull Request (PR) hacia la rama principal de este repositorio.
4.  **Revisión:** Una vez verificado que los nombres cumplen el estándar, se aceptará el cambio y estará disponible para todos los usuarios de la App.

---

## 🛡️ Calidad de Imagen Recomendada
* **Dimensiones:** 600x900 píxeles (proporción 2:3).
* **Fondo:** Preferiblemente sin transparencias (a menos que sea arte 3D).
* **Peso:** Intentar que cada imagen no supere los 300KB para una carga rápida en la App.

---
*Mantenido con ❤️ por la comunidad de Retro Gaming.*

