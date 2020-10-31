from flask import Flask
from game_systems.tiny_dungeon import character as td_char

app = Flask(__name__)

@app.route("/")
def root_test():
    msg = 'welcome to rpg tools'
    return msg

@app.route("/tiny_dungeon")
def tiny_dungeon_char():
    return td_char.PlayerCharacter().to_dict()

if __name__=='__main__':
   app.run(debug=True)
