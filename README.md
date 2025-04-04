# Castlevania Roguelike

A roguelike game inspired by Castlevania, developed in Python using Pygame and following the Model-View-Controller (MVC) architectural pattern.

## Project Overview

This game combines the classic Castlevania atmosphere with roguelike elements, featuring procedurally generated levels, permadeath, and challenging combat mechanics.

## Architecture

The project follows the MVC pattern:

* **Model**: Handles game logic, entity states, and data management
* **View**: Manages all rendering and visual aspects using Pygame
* **Controller**: Processes user input and coordinates between Model and View

## Dependencies

* Python 3.x
* Pygame

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

* Procedurally generated castle layouts
* Character progression system
* Multiple character classes
* Various weapons and abilities
* Boss battles
* Permadeath mechanics
* Pixel art graphics

## Development Status

🚧 Under Development

## Contributing

We welcome contributions to the Economato-Textil project! Please follow these steps to contribute:

1. **Fork the Repository**
   * Click the 'Fork' button at the top right of this repository
   * Clone your fork locally:

     ```bash
     git clone https://github.com/YOUR_USERNAME/Economato-Textil.git
     ```

2. **Create a Feature Branch**
   * Create a branch for your feature:

     ```bash
     git checkout -b feature/your-feature-name
     ```

   * Make your changes in this branch

3. **Coding Guidelines**
   * Follow PEP 8 style guidelines for Python code
   * Add comments for complex logic
   * Keep the MVC architecture in mind when adding features
   * Update tests if applicable

4. **Commit Your Changes**
   * Make meaningful commits with clear messages:

     ```bash
     git commit -m "Add: brief description of your changes"
     ```

   * Push to your fork:

     ```bash
     git push origin feature/your-feature-name
     ```

5. **Submit a Pull Request**
   * Go to the original repository
   * Click 'New Pull Request'
   * Select your feature branch
   * Add a clear description of your changes
   * Link any relevant issues

6. **Code Review**
   * Wait for review from maintainers
   * Make any requested changes
   * Once approved, your code will be merged

7. **Keep Updated**
   * Regularly sync your fork with the main repository:

     ```bash
     git remote add upstream https://github.com/ManuelNevado/Economato-Textil.git
     git fetch upstream
     git checkout main
     git merge upstream/main
     ```

Thank you for contributing to make this awesome project even better!
