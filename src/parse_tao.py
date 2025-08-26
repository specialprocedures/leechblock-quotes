# %%
import json
import re

with open("TAO.txt", "r") as f:
    tao = f.read()


parts = [i.strip() for i in tao.split("---") if len(i) > 100]

all_chapters = []

for p in parts:
    # split on new line if begins with numeric
    chapters = re.split(r"\n(?=\d)", p)

    for c in chapters:
        if len(c) > 10:
            chapter_number, text = c.split("\n", 1)
            all_chapters.append(
                {
                    "author": f"Tao Te Ching, Ron Hogan Translation, {chapter_number}",
                    "text": text.strip(),
                }
            )

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(all_chapters, f, ensure_ascii=False, indent=4)
