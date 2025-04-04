# Castlevania Roguelike

A roguelike game inspired by Castlevania, developed in Python using Pygame and following the Model-View-Controller (MVC) architectural pattern.

## Project Overview

This game combines the classic Castlevania atmosphere with roguelike elements, featuring procedurally generated levels, permadeath, and challenging combat mechanics.

## Architecture

The project follows the MVC pattern:

- **Model**: Handles game logic, entity states, and data management
- **View**: Manages all rendering and visual aspects using Pygame
- **Controller**: Processes user input and coordinates between Model and View

## Dependencies

- Python 3.x
- Pygame

## Project Structure

```plaintext
.
├── main.py           # Game entry point
├── model/           # Game logic and data
├── view/            # Rendering and display
├── controller/      # Input handling and game flow
├── assets/         # Game resources (sprites, sounds)
└── README.md       # This file
```

## Setup and Installation

1. Ensure Python 3.x is installed

2. Install dependencies:

   ```bash
   pip install pygame
   ```

3. Run the game:

   ```bash
   python main.py
   ```

## Features (Planned)

- Procedurally generated castle layouts
- Character progression system
- Multiple character classes
- Various weapons and abilities
- Boss battles
- Permadeath mechanics
- Pixel art graphics

## Development Status

🚧 Under Development