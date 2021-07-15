from flask import Flask
import assh_char
import td_char
import gamma5_char
import maze_rats_char


app = Flask(__name__)


@app.route("/")
def root_test():
    return "welcome to rpg tools"


@app.route("/assh/json")
def assh_character():
    return assh_char.PlayerCharacter().to_dict()


@app.route("/assh/dying-earth/json")
def assh_de_character():
    return assh_char.PlayerCharacter(magician_spell_src="dying_earth").to_dict()


@app.route("/tiny-dungeon/json")
def tiny_dungeon_character():
    return td_char.PlayerCharacter().to_dict()


@app.route("/gamma5/json")
def gamma5_character():
    return gamma5_char.PlayerCharacter().to_dict()


@app.route("/maze-rats/json")
def maze_rats_character():
    return maze_rats_char.PlayerCharacter().to_dict()


if __name__ == "__main__":
    app.run(debug=True)
