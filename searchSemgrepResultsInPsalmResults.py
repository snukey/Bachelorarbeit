import json
import random

f1 = open("16/report.json")
psalm = json.load(f1)
f1.close()
f2 = open("16/semgrep_oss_results.json")
sem = json.load(f2)
f2.close()
num = 60
categories = [
    "echoed-request"
    ,"tainted-sql-string"
    ,"tainted-filename"
    ,"curl-ssl-verifypeer-off"
    ,"tainted-callable"
    ,"tainted-exec"
    ,"tainted-url-host"
    ,"tainted-object-instantiation"
    ,"redirect-to-request-uri"
    ,"phpinfo-use"
    ]

for category in categories:
    semarray = list()
    resarray = list()

    for semele in sem["results"]:
        if category in semele["check_id"]:
            line = semele["extra"]["lines"]
            semarray.append(line)

    if num < len(semarray):
        selection = random.sample(semarray, num)
    else:
        selection = semarray

    for semsnip in selection:
        for psele in psalm:
            if semsnip in psele["snippet"]:
                resarray.append(psele["snippet"])
                break
    # Output
    with open("compareSemInPsalm.txt", "a") as f:
        f.write(f"{category}:\n",)
        for e in resarray:
            f.write(f'\t{repr(e)}\n')

    