import json

class result_type:
    def __init__(self, res_type) -> None:
        self.res_type = res_type
        self.occurences = 1
        
f = open("psalmResults/psalmResults.json")
data = json.load(f)
result_typesP = list()
for i in data: 
    result = i["message"]
    if existing_type := next((x for x in result_typesP if x.res_type == result), None):
        existing_type.occurences += 1
    else:
        new_type = result_type(result)
        result_typesP.append(new_type)

f = open("semgrepResults/semgrepResults.json")
data = json.load(f)
result_typesS = list()
for preresult in data["results"]:
    result = preresult["check_id"].rsplit(".", 1)[1]
    if existing_type := next((x for x in result_typesS if x.res_type == result), None):
        existing_type.occurences += 1
    else:
        new_type = result_type(result)
        result_typesS.append(new_type)  

sorted_P = sorted(result_typesP, key=lambda x: x.occurences, reverse=True)
sorted_S = sorted(result_typesS, key=lambda x: x.occurences, reverse=True)
for x in sorted_P:
    print(x.res_type + " : " + str(x.occurences))
for x in sorted_S:
    print(x.res_type + " : " + str(x.occurences))

