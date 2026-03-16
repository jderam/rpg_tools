from fastapi import FastAPI, Query
from rpg_tools.tiny_dungeon.char import PlayerCharacter as TinyDungeonPlayerCharacter

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "rpg_tools"}


@app.get("/tiny_dungeon")
async def tiny_dungeon_char(
    race: str | None = Query(None),
) -> dict[str, any]:
    pc: TinyDungeonPlayerCharacter = TinyDungeonPlayerCharacter(race)
    pc_dict: dict[str, any] = pc.to_dict()
    return pc_dict
