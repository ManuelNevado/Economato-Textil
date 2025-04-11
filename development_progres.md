# Implementación del Sistema de Menú y Funcionalidades

## 🎮 Sistema de Menú Principal

He implementado un sistema de menú completo con las siguientes características:

### 📋 Items del Menú

- "Start Game"
- "Options"
- "Settings"

### 🕹️ Navegación

- Teclas **UP/DOWN** para navegar entre items
- **ENTER** para seleccionar un item
- **ESC** para volver al menú desde otros estados

### 👁️ Feedback Visual

- Título en la parte superior
- Item seleccionado resaltado en amarillo
- Otros items en blanco

### 🏗️ Arquitectura (Patrón MVC)

| Componente | Responsabilidad |
|------------|----------------|
| **Model**  | Estado del menú, item seleccionado y estado del juego |
| **View**   | Renderiza el menú con formato y resaltados |
| **Controller** | Maneja inputs del teclado para navegación |

## 🖼️ Mejoras Visuales (GameView)

```python
# Cambios implementados:
import os  # Para manejo de rutas de archivos

# En el constructor:
self.background = load_image("assets/background.png")
self.background = scale_to_fit(screen_size)

# En _render_menu():
draw_background()
draw_semi_transparent_overlay(alpha=128)  # Mejora legibilidad
draw_menu_text()  # Sobre el fondo
```

### 🔧 Ajustes Disponibles

#### 1. Transparencia del Overlay

```python
# En game_view.py
OVERLAY_ALPHA = 128  # Valor actual (0-255)
```

#### 2. Escalado de Imagen de Fondo

```python
# Ejemplo de código ajustable
def resize_background():
    screen_size = (1920, 1080)  # Valores modificables
    return pygame.transform.scale(original_image, screen_size)
```

#### 3. Posición de Elementos del Menú

| Elemento | Variable | Valor por defecto |
| --- | --- | --- |
| Título | `TITLE_POS` | `(100, 50)` |
| Primer ítem | `FIRST_ITEM_Y` | `200` |
| Espaciado | `ITEM_SPACING` | `60` |

#### 🔄 Cómo Modificar

##### Overlay:

```
# Para mayor transparencia:
- OVERLAY_ALPHA = 128
+ OVERLAY_ALPHA = 80  # Más transparente
```

##### Escalado (Relación de aspecto):

```python
# Mantener aspect ratio:
scaled_width = screen_width * 0.8  # 80% del ancho
scaled_height = original_height * (scaled_width / original_width)
```

##### Posiciones (Coordenadas personalizadas):

```python
# Sistema de coordenadas relativas:
def calculate_y_position(index):
    return FIRST_ITEM_Y + (index * ITEM_SPACING)
```

#### 📊 Valores Recomendados

| Ajuste | Mínimo | Recomendado | Máximo |
| --- | --- | --- | --- |
| Transparencia | 50  | 120-150 | 255 |
| Escala (porcentaje) | 50% | 75%-90% | 100% |
| Espaciado vertical | 30  | 50-70 | 100 |


La documentacion esta en la siguiente [ubicacion](https://roguebasin.com/index.php/Basic_BSP_Dungeon_generation)

## 📚 Recursos para Desarrollo de Roguelikes en Python

### 🧩 Algoritmos de Generación Procedural

#### Binary Space Partitioning (BSP)

- [RogueBasin: Basic BSP Dungeon Generation](https://roguebasin.com/index.php/Basic_BSP_Dungeon_generation) - Tutorial detallado sobre implementación de BSP
- [Red Blob Games: Procedural Generation](https://www.redblobgames.com/maps/terrain-from-noise/) - Excelentes tutoriales visuales sobre generación procedural
- [PCG Wiki: Dungeon Generation](http://pcg.wikidot.com/pcg-algorithm:dungeon-generation) - Colección de algoritmos para generación de mazmorras

#### Otros Algoritmos

- [Cellular Automata Tutorial](https://gamedevelopment.tutsplus.com/tutorials/generate-random-cave-levels-using-cellular-automata--gamedev-9664) - Generación de cuevas con autómatas celulares
- [Drunkard's Walk Algorithm](https://www.roguebasin.com/index.php/Random_Walk_Cave_Generation) - Implementación del algoritmo de caminata aleatoria

### 🐍 Frameworks y Tutoriales para Roguelikes en Python

- [libtcod/python-tcod](https://github.com/libtcod/python-tcod) - Biblioteca popular para desarrollo de roguelikes
- [RoguelikeDev Tutorial Series](https://www.reddit.com/r/roguelikedev/wiki/python_tutorial_series) - Tutorial completo paso a paso
- [TStand90's Roguelike Tutorial](https://github.com/TStand90/tcod_tutorial_v2) - Tutorial moderno con Python 3 y tcod

### 🎮 Implementaciones con Pygame

- [PyGame Dungeon Generator](https://github.com/AtTheMatinee/dungeon-generation) - Generador de mazmorras específico para Pygame
- [Roguelike Development with Pygame](https://www.youtube.com/watch?v=Fdbe2PuAjAQ) - Tutorial en video sobre desarrollo con Pygame

### 📺 Videos Explicativos

- [Procedural Generation: Programming The Universe](https://www.youtube.com/watch?v=ZZY9YE7rZJw) - Por Sebastian Lague
- [Procedural Dungeon Generation](https://www.youtube.com/watch?v=v7yyZZjF1z4) - Por The Coding Train

### 📖 Artículos y Guías

- [The Procedural Content Generation Wiki](http://pcg.wikidot.com/) - Recurso completo sobre generación procedural
- [Roguelike Development Subreddit](https://www.reddit.com/r/roguelikedev/) - Comunidad activa con recursos y discusiones
- [How to Make a Roguelike](https://www.gamasutra.com/blogs/JoshGe/20181029/329512/How_to_Make_a_Roguelike.php) - Guía completa sobre diseño de roguelikes