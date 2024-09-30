import json
import random

f1 = open("psalmResults/psalmResults.json")
psalm = json.load(f1)
f1.close()
f2 = open("semgrepResults/semgrepResults.json")
sem = json.load(f2)
f2.close()
num = 53
category = "Detected tainted text"

psarray = list()
resarray = list()
for psele in psalm:
    if category == psele["message"]:
        psarray.append(psele["snippet"])
if num < len(psarray):
    selection = random.sample(psarray, num)
else:
    selection = set(psarray)
for sel in selection:
    print("hello")
    for semele in sem["results"]:
        if semele["extra"]["lines"] in sel:
            resarray.append(semele["extra"]["lines"])
            break
# Output
with open("compare1.txt", "a") as f:
    f.write(f"{category}:\n",)
    for e in resarray:
        f.write(f'\t{repr(e)}\n')

