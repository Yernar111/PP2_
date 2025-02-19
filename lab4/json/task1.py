import json

print("Interface status")
print("="*80)
print("DN", " "*48, "Description", " "*8, "Speed"," "*3, "MTU")
print("-"*50, "-"*20, "-"*8, "-"*8)

with open("sample-data.json", "r") as abcd:
    u=json.load(abcd)
    a=u["imdata"]
    for i in range(len(a)):
        b=a[i]["l1PhysIf"]["attributes"]["dn"]
        c=a[i]["l1PhysIf"]["attributes"]["descr"]
        d=a[i]["l1PhysIf"]["attributes"]["speed"]
        e=a[i]["l1PhysIf"]["attributes"]["mtu"]
        print(f"{b:<50}", f"{c}", " "*20, f"{d}", "\t" f"{e}")


