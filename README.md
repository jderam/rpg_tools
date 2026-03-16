# rpg_tools

A collection of tools for use with tabletop RPGs for generating characters, equipment, spells, etc.

## Supported Systems

| System | Module | Features |
|--------|--------|----------|
| Astonishing Swordsmen & Sorcerers of Hyperborea | `rpg_tools.assh` | Character generation |
| D666 | `rpg_tools.d666` | Character generation |
| Gamma Five | `rpg_tools.gamma5` | Character generation |
| Maze Rats | `rpg_tools.maze_rats` | Character & spell generation |
| Tiny Dungeon | `rpg_tools.tiny_dungeon` | Character generation |
| Frostgrave | `rpg_tools.frostgrave` | Spell data |
| Misc Data | `rpg_tools.misc_data` | DCC occupations, Knave spells, Dying Earth spells, Zothique names |

## Installation

```bash
pip install rpg_tools
```

### Development Setup

```bash
# Clone the repo
git clone https://github.com/jderam/rpg_tools.git
cd rpg_tools

# Install with all development dependencies
uv sync --frozen --all-extras

# Install pre-commit hooks
uv run pre-commit install
```

## Usage

```python
# Generate an ASSH character
from rpg_tools.assh.char import PlayerCharacter
pc = PlayerCharacter()
print(pc.to_dict())

# Generate a Maze Rats spell
from rpg_tools.maze_rats.magic import generate_spell
print(generate_spell())

# Generate a D666 character at level 3
from rpg_tools.d666.char import D666Character
c = D666Character(level=3)
print(c.to_dict())
```

## Development

```bash
make format    # Format code with ruff
make lint      # Lint code with ruff
make test      # Run tests with pytest
make test-cov  # Run tests with coverage report
make check     # Run format check + lint
make help      # Show all available targets
```

## License

MIT
