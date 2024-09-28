import json
import random

f1 = open("16/report.json")
psalm = json.load(f1)
f1.close()
f2 = open("16/semgrep_oss_results.json")
sem = json.load(f2)
f2.close()
num = 53
category = "Detected tainted HTML"

psarray = list()
resarray = list()
for psele in psalm:
    if category in psele["message"]:
        psarray.append(psele["snippet"])
if num < len(psarray):
    selection = random.sample(psarray, num)
else:
    selection = set(psarray)
for sel in selection:
    for semele in sem["results"]:
        if semele["extra"]["lines"] in sel:
            resarray.append(semele["extra"]["lines"])
            break
# Output
with open("compare1.txt", "a") as f:
    f.write(f"{category}:\n",)
    for e in resarray:
        f.write(f'\t{repr(e)}\n')

