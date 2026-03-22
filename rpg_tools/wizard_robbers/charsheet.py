"""Generate a Wizard Robbers character sheet as PDF via HTML/CSS + WeasyPrint."""

import random
from pathlib import Path
from string import Template

from weasyprint import HTML

from rpg_tools.wizard_robbers.char import Character


TEMPLATE = Template("""\
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {
    size: letter;
    margin: 0.6in 0.75in;
  }
  body {
    font-family: 'Avenir Next', 'Avenir', 'Gill Sans', sans-serif;
    font-size: 10.5pt;
    color: #1a1a1a;
    line-height: 1.4;
  }
  h1 {
    font-family: 'Pantagruel\u2122', Palatino, serif;
    font-size: 42pt;
    text-align: center;
    margin: 0 0 6pt 0;
    letter-spacing: 2pt;
    font-weight: normal;
  }
  hr {
    border: none;
    border-top: 1.5pt solid #1a1a1a;
    margin: 4pt 0 10pt 0;
  }
  .header-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 2pt;
  }
  .header-field {
    font-size: 10.5pt;
  }
  .label {
    font-weight: bold;
    font-variant: small-caps;
    font-size: 10pt;
    letter-spacing: 0.5pt;
  }
  .section-title {
    font-variant: small-caps;
    font-weight: bold;
    font-size: 12pt;
    letter-spacing: 1pt;
    margin: 14pt 0 4pt 0;
    border-bottom: 1pt solid #1a1a1a;
    padding-bottom: 2pt;
  }
  .item {
    margin: 3pt 0;
    padding-left: 8pt;
  }
  .item-name {
    font-weight: bold;
  }
  .item-desc {
    color: #333;
  }
  .animus-box {
    background: #f5f0e8;
    border: 0.75pt solid #c0b090;
    border-radius: 3pt;
    padding: 8pt 10pt;
    margin: 8pt 0;
  }
  .animus-name {
    font-weight: bold;
    font-style: italic;
  }
  .animus-desc {
    font-size: 9.5pt;
    color: #444;
    margin-top: 2pt;
  }
  .two-col {
    display: flex;
    gap: 24pt;
  }
  .two-col > div {
    flex: 1;
  }
  .equipment-list {
    margin: 0;
    padding-left: 16pt;
  }
  .equipment-list li {
    margin: 1pt 0;
  }
  .spell-item {
    margin: 3pt 0 3pt 8pt;
  }
  .spell-name {
    font-weight: bold;
  }
  .spell-desc {
    font-size: 9.5pt;
    color: #444;
  }
  .checkbox {
    font-size: 12pt;
    letter-spacing: 2pt;
  }
</style>
</head>
<body>

<h1>WIZARD ROBBERS</h1>
<hr>

<div class="header-row">
  <div class="header-field">
    <span class="label">Name:</span> ____________________
  </div>
  <div class="header-field">
    <span class="label">Occupation:</span> $occupation
  </div>
  <div class="header-field">
    <span class="label">Level:</span> $level
  </div>
  <div class="header-field">
    <span class="label">Hit Points:</span> $hit_points_boxes
  </div>
</div>

<div class="animus-box">
  <span class="label">Animus:</span>
  <span class="animus-name">$animus_name</span>
  <div class="animus-desc">$animus_desc</div>
</div>

<div class="two-col">
  <div>
    <div class="section-title">Skills</div>
    $skills_html

    $ea_section

    $spells_section

    <div class="section-title">Weapon</div>
    <div class="item">
      <span class="item-name">$weapon</span>
    </div>

    <div class="section-title">Equipment</div>
    <ul class="equipment-list">
      $equipment_html
    </ul>

    <div class="item" style="margin-top: 10pt;">
      <span class="label">Money:</span> $money terces
    </div>
  </div>
  <div></div>
</div>

</body>
</html>
""")


def _render_skills(skills: list[dict[str, str]]) -> str:
    parts = []
    for skill in skills:
        for name, desc in skill.items():
            parts.append(
                f'<div class="item">'
                f'<span class="item-name">{name}</span> \u2014 '
                f'<span class="item-desc">{desc}</span>'
                f"</div>"
            )
    return "\n".join(parts)


def _render_eas(eas: list[dict[str, str]]) -> str:
    if not eas:
        return ""
    items = []
    for ea in eas:
        for name, desc in ea.items():
            items.append(
                f'<div class="item">'
                f'<span class="item-name">{name}</span> \u2014 '
                f'<span class="item-desc">{desc}</span>'
                f"</div>"
            )
    return '<div class="section-title">Extraordinary Abilities</div>\n' + "\n".join(items)


def _render_spells(spells: list[dict[str, str]]) -> str:
    if not spells:
        return ""
    items = []
    for spell in spells:
        for name, desc in spell.items():
            items.append(
                f'<div class="spell-item">'
                f'<span class="spell-name">{name}</span> \u2014 '
                f'<span class="spell-desc">{desc}</span>'
                f"</div>"
            )
    return '<div class="section-title">Spells</div>\n' + "\n".join(items)


def _render_equipment(equipment: list[str]) -> str:
    return "\n".join(f"<li>{item}</li>" for item in equipment)


def generate_charsheet_html(char: Character) -> str:
    hp_boxes = '<span class="checkbox">' + "\u2610 " * char.hit_points + "</span>"
    return TEMPLATE.substitute(
        level=char.level,
        occupation=char.occupation,
        hit_points_boxes=hp_boxes,
        money=char.money,
        animus_name=char.animus["name"],
        animus_desc=char.animus["description"],
        skills_html=_render_skills(char.skills),
        ea_section=_render_eas(char.extraordinary_abilities),
        spells_section=_render_spells(char.spells),
        weapon=char.weapon,
        equipment_html=_render_equipment(char.equipment),
    )


def generate_charsheet_pdf(char: Character, output_path: str | Path) -> Path:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    html_str = generate_charsheet_html(char)
    HTML(string=html_str).write_pdf(str(output_path))
    return output_path


if __name__ == "__main__":
    random.seed()
    char = Character(level=1)
    out = generate_charsheet_pdf(char, "output/wizard_robbers_char.pdf")
    print(f"Level {char.level} {char.occupation}")
    print(f"HP: {char.hit_points}  Money: {char.money} terces")
    print(f"Animus: {char.animus['name']}")
    print(f"Skills: {[next(iter(s)) for s in char.skills]}")
    print(f"EAs: {[next(iter(ea)) for ea in char.extraordinary_abilities]}")
    if char.spells:
        print(f"Spells: {[next(iter(sp)) for sp in char.spells]}")
    print(f"Weapon: {char.weapon}")
    print(f"Saved to {out}")
