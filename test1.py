import json

with open("sample-data.json", "r") as abcd:
    u=json.load(abcd)
    #print("DN", "\t" "\t" "\t" "\t" "\t" "\t" "\t" "\t" "\t" "Description", "\t" "\t" "Speed", "\t" "MTU")
    #print("DN", "\n",u["imdata"][0]["l1PhysIf"]["attributes"]["dn"], "Speed", "\n", u["imdata"][0]["l1PhysIf"]["attributes"]["speed"])
    #print("DN", " "*40, "Description", " "*8, "Speed", "\t" "\t" "MTU")
    #print(u["imdata"][0]["l1PhysIf"]["attributes"]["dn"], " "*20, u["imdata"][0]["l1PhysIf"]["attributes"]["speed"])
    for i in u["imdata"]:
        for j in i:
            for t in i[j]:
                print(i[j][t]["dn"], i[j][t]["speed"], i[j][t]["mtu"])