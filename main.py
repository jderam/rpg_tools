from typing import Any, Dict, Optional

from fastapi import FastAPI, Query
from rpg_tools.tiny_dungeon.char import PlayerCharacter as TinyDungeonPlayerCharacter

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "rpg_tools"}


@app.get("/tiny_dungeon")
async def tiny_dungeon_char(
    race: Optional[str] = Query(None),
) -> Dict[str, Any]:
    pc: TinyDungeonPlayerCharacter = TinyDungeonPlayerCharacter(race)
    pc_dict: Dict[str, Any] = pc.to_dict()
    return pc_dict
