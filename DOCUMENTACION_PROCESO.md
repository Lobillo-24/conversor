# Tarea 1. Documentar una aplicación con MkDocs

**Alumno:** Juan Antonio López Muñoz
**Curso:** 2º DAW — Dual Despliegue (GS) 26-27

## Repositorio

- **Enlace:** https://github.com/Lobillo-24/conversor
- **Ramas:** `main` (versión final) y `feature/documentacion` (donde se hizo el trabajo)

---

## 1. Qué he hecho

He partido de un programa en Python, `conversor.py`, que convierte temperaturas entre grados Celsius y Fahrenheit, y he creado su documentación con **MkDocs**. El proyecto está bajo control de versiones con Git y publicado en GitHub.

## 2. Preparación del entorno

Creé la carpeta del proyecto, inicialicé el repositorio y preparé un entorno virtual para instalar MkDocs sin afectar al resto del sistema:

```powershell
mkdir conversor
cd conversor
git init
py -m venv .venv
.venv\Scripts\activate
py -m pip install mkdocs
```

Uso `py` (el lanzador de Python de Windows) en lugar de `python` porque es el comando que funciona en mi terminal de VS Code.

## 3. El programa: `conversor.py`

Es una aplicación de consola con dos funciones de conversión y un menú:

```python
def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9

def main():
    print("Conversor de temperaturas")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = input("Elige una opción: ")
    valor = float(input("Introduce la temperatura: "))

    if opcion == "1":
        print(f"{valor} °C = {celsius_a_fahrenheit(valor):.2f} °F")
    elif opcion == "2":
        print(f"{valor} °F = {fahrenheit_a_celsius(valor):.2f} °C")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
```

Lo probé con `py conversor.py` antes de documentarlo.

## 4. Documentación con MkDocs

Inicialicé MkDocs en la carpeta del proyecto con `mkdocs new .`, que crea `mkdocs.yml` y `docs/index.md`. Después añadí a mano las otras dos páginas.

### Páginas de `docs/`

| Archivo | Contenido |
|---|---|
| `docs/index.md` | Página de inicio: explica qué hace la aplicación |
| `docs/instalacion.md` | Requisitos (Python 3.8 o superior y Git) y procedimiento para obtener el proyecto con `git clone` |
| `docs/uso.md` | Cómo ejecutar el programa y un ejemplo de ejecución |

### Menú de navegación (`mkdocs.yml`)

```yaml
site_name: Conversor de temperaturas
nav:
  - Inicio: index.md
  - Instalación: instalacion.md
  - Uso: uso.md
```

## 5. `README.md` y `.gitignore`

El `README.md` está en la raíz del proyecto: describe brevemente el programa, cómo ejecutarlo y cómo ver la documentación (`pip install mkdocs` y `mkdocs serve`).

El `.gitignore` excluye lo que no debe subirse al repositorio:

```
site/
__pycache__/
*.pyc
.venv/
```

Los tres primeros son los que pide el enunciado. Añadí `.venv/` porque el entorno virtual pesa mucho y se puede recrear en cualquier equipo.

## 6. Comprobación y generación del sitio

```powershell
mkdocs serve
```

Abrí `http://127.0.0.1:8000` y comprobé que el menú muestra **Inicio**, **Instalación** y **Uso**, y que cada página se ve correctamente (listas, bloques de código y ejemplo de ejecución).

```powershell
mkdocs build
```

Esto generó la carpeta `site/` con el sitio estático final. Con `git status` verifiqué que `site/` no aparece como archivo pendiente, es decir, que el `.gitignore` la excluye correctamente.

## 7. Control de versiones

Para no trabajar directamente sobre `main`, usé una rama de trabajo aparte:

1. Un primer commit en `main` solo con el `.gitignore`.
2. Creé la rama `feature/documentacion` y allí hice un commit por cada parte del trabajo.
3. Volví a `main` e integré la rama con un merge sin *fast-forward* (`--no-ff`), para que el historial refleje que el trabajo se hizo en una rama.

```powershell
git branch -M main
git add .gitignore
git commit -m "Añade .gitignore"

git switch -c feature/documentacion

git add conversor.py
git commit -m "Añade programa conversor"

git add docs mkdocs.yml
git commit -m "Añade documentación con MkDocs"

git add README.md
git commit -m "Añade README"

git switch main
git merge --no-ff feature/documentacion -m "Integra documentación del conversor"
```

### Historial resultante

Obtenido con `git log --oneline --graph --all`:

```
*   0611e92 (HEAD -> main) Integra documentación del conversor
|\
| * 7bbc8d7 (feature/documentacion) Añade README
| * 11a8831 Añade documentación con MkDocs
| * 2919da2 Añade programa conversor
|/
* 91ec43e Añade .gitignore
```

## 8. Publicación en GitHub

Creé en GitHub el repositorio `conversor` **vacío** (sin README, `.gitignore` ni licencia, porque ya existían en local y habrían provocado conflictos) y subí las dos ramas:

```powershell
git remote add origin https://github.com/Lobillo-24/conversor.git
git push -u origin main
git push -u origin feature/documentacion
```

## 9. Estructura final del proyecto

```
conversor/
├── conversor.py
├── README.md
├── .gitignore
├── mkdocs.yml
└── docs/
    ├── index.md
    ├── instalacion.md
    └── uso.md
```

La carpeta `site/` se genera con `mkdocs build`, pero no se versiona.

## 10. Requisitos del enunciado

| Requisito | Cumplido | Dónde |
|---|---|---|
| Página de inicio que explique qué hace la aplicación | Sí | `docs/index.md` |
| Página de instalación con requisitos y procedimiento | Sí | `docs/instalacion.md` |
| Página de uso con un ejemplo de ejecución | Sí | `docs/uso.md` |
| Menú de navegación configurado en `mkdocs.yml` | Sí | `mkdocs.yml` (`nav`) |
| `README.md` en la raíz | Sí | `README.md` |
| `.gitignore` que excluya `site/`, `__pycache__/` y `.pyc` | Sí | `.gitignore` |
| Comprobar con `mkdocs serve` | Sí | Apartado 6 |
| Generar el sitio con `mkdocs build` | Sí | Apartado 6 |
| Control de versiones | Sí | Apartados 7 y 8 |

## 11. Problemas que encontré

- **`python` no se reconocía en la terminal.** Windows redirigía el comando a un atajo de la Microsoft Store. Lo resolví usando `py`, el lanzador de Python, que sí funciona.
- **Pegué el contenido del `.gitignore` en la terminal** en lugar de crear el archivo, y PowerShell intentó ejecutar cada línea como un comando. Lo solucioné creando el archivo desde VS Code.
- **`.gitignore` y `README.md` se crearon fuera de la carpeta del proyecto.** Los arrastré dentro de `conversor/` y lo verifiqué con `git status`.

## 12. Cómo reproducir el proyecto

```powershell
git clone https://github.com/Lobillo-24/conversor.git
cd conversor
py -m venv .venv
.venv\Scripts\activate
py -m pip install mkdocs
mkdocs serve
```

Después se abre `http://127.0.0.1:8000` en el navegador. Para generar el sitio estático:

```powershell
mkdocs build
```

## 13. Otros formatos (opcional)

Como el contenido original está en Markdown, estos mismos archivos se pueden reutilizar para generar otros formatos con herramientas adicionales, por ejemplo con Pandoc, o imprimiendo la web a PDF desde el navegador.
