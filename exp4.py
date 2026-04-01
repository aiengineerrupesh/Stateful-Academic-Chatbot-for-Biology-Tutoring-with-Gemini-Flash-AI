import json
message=[{'role':"user","content":"what is list","role":"assistant","content":"list is a mutable datatype"}]
with open("data.json","w")as file_obj:
    json.dump(message,file_obj)