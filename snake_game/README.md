# 🐍 Snake Game

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.5.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub%20Actions-2088FF.svg)

**A classic Snake game implementation with modern features and CI/CD integration**

[Features](#-features) • [Installation](#-installation) • [Gameplay](#-gameplay) • [Development](#-development) • [CI/CD](#-cicd-integration)

</div>

---

## 🎮 Features

### Core Gameplay
- **Classic Snake Mechanics** - Navigate the snake to collect food and grow longer
- **Smooth Controls** - Responsive arrow key controls with collision prevention
- **Score Tracking** - Real-time score display as you collect food
- **Game Over Detection** - Wall and self-collision detection
- **Quick Restart** - Press SPACE to instantly restart after game over

### Technical Highlights
- 🎨 **Clean Graphics** - Built with Pygame for smooth rendering
- 🤖 **Headless Mode** - Supports automated testing in CI/CD environments
- 📦 **Executable Build** - PyInstaller integration for standalone executables
- 🔧 **Configurable** - Easy-to-modify constants for game customization
- 🧪 **Test Mode** - Built-in test mode for automated validation

## 📸 Game Preview

```
┌─────────────────────────────────┐
│  Score: 50                      │
│                                 │
│      ████  🍎                   │
│      ████                       │
│      ████████████               │
│                                 │
│                                 │
│                                 │
└─────────────────────────────────┘

    Arrow Keys: Move Snake
    SPACE: Restart (Game Over)
    ESC: Exit Game
```

## 🚀 Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/zhangjiaran/github_actions_demo.git
   cd github_actions_demo/snake_game
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**
   ```bash
   python main.py
   ```

### Alternative Installation Methods

#### Using Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

#### Using System Python
```bash
# Install dependencies globally
pip install pygame==2.5.2

# Run the game
python main.py
```

## 🎯 Gameplay

### Objective
Control the snake to eat as much food as possible without hitting walls or your own body!

### Controls
| Key | Action |
|-----|--------|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |
| SPACE | Restart (when game over) |
| ESC | Exit Game |

### Rules
1. **Eat Food** - Guide the snake to the red food blocks 🍎
2. **Grow Longer** - Each food item makes the snake grow by one segment
3. **Avoid Collisions** - Don't hit the walls or your own body
4. **Score Points** - Each food item gives you 10 points
5. **Challenge Yourself** - See how high you can score!

### Tips & Tricks
- 💡 Plan your path ahead - don't box yourself in!
- 💡 Stay near the center of the screen for more maneuvering space
- 💡 The snake can't reverse direction - plan accordingly
- 💡 Take your time - there's no time pressure, only collision danger

## 🛠️ Development

### Project Structure
```
snake_game/
├── main.py           # Main game implementation
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

### Code Architecture

#### Classes
- **`Direction`** - Enum for movement directions (UP, DOWN, LEFT, RIGHT)
- **`Snake`** - Snake entity with movement, growth, and collision detection
- **`Food`** - Food entity with random positioning
- **`SnakeGame`** - Main game controller handling events, updates, and rendering

#### Key Constants (Customizable)
```python
WINDOW_WIDTH = 600      # Game window width in pixels
WINDOW_HEIGHT = 600     # Game window height in pixels
GRID_SIZE = 20          # Size of each grid cell
FPS = 10                # Game speed (frames per second)

# Colors (RGB)
BLACK = (0, 0, 0)       # Background
GREEN = (0, 255, 0)     # Snake
RED = (255, 0, 0)       # Food
WHITE = (255, 255, 255) # Text
```

### Running in Test Mode

For automated testing or CI/CD:
```bash
# Explicit test mode
python main.py --test

# CI environment (auto-detected)
CI=true python main.py
```

Test mode runs the game headless for 30 frames and exits automatically.

## 🔄 CI/CD Integration

This project includes a complete GitHub Actions workflow for:

### Automated Testing
- Headless game execution for smoke testing
- Automated dependency installation
- Python 3.11+ environment setup

### Executable Building
- Automatic PyInstaller builds
- Cross-platform executable generation
- Artifact upload for distribution

### Workflow Triggers
- Push to `main` or `master` branches
- Pull requests to `main` or `master` branches
- Manual workflow dispatch

### Download Built Executables
Built executables are available as artifacts in the [Actions tab](../../actions) after each successful build.

## 🧪 Testing

### Manual Testing
```bash
# Run the game normally
python main.py

# Test headless mode
python main.py --test
```

### Automated Testing
The GitHub Actions workflow automatically runs tests on every push and PR.

## 🎨 Customization Ideas

Want to make the game your own? Try these modifications:

1. **Change Colors** - Modify the RGB color constants
2. **Adjust Speed** - Change the `FPS` constant (higher = faster)
3. **Resize Grid** - Modify `GRID_SIZE` for bigger/smaller cells
4. **Add Power-ups** - Implement special food items with different effects
5. **Add Obstacles** - Create walls or barriers on the playing field
6. **High Score System** - Save and display best scores
7. **Sound Effects** - Add audio feedback using pygame.mixer
8. **Multiple Levels** - Increase difficulty as score increases

## 📋 Requirements

- Python 3.11+
- pygame 2.5.2
- pyinstaller 6.3.0 (for building executables)

## 🐛 Troubleshooting

### Game window doesn't appear
- Ensure pygame is installed: `pip install pygame`
- Check display drivers are available
- Try running with `--test` flag to verify code execution

### Installation errors
- Update pip: `pip install --upgrade pip`
- Ensure Python version is 3.11 or higher: `python --version`
- Try installing in a virtual environment

### Performance issues
- Lower the FPS value in the code
- Close other resource-intensive applications
- Check system graphics drivers

## 📝 License

This project is part of the github_actions_demo repository.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

### How to Contribute
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🌟 Acknowledgments

- Built with [Pygame](https://www.pygame.org/) - Python game development library
- Inspired by the classic Nokia Snake game
- CI/CD powered by GitHub Actions

---

<div align="center">

**Enjoy the game! 🐍🎮**

Made with ❤️ and Python

</div>
