print("Texte à calculer: ")
whitebox = input()
Octolist = []
for l in whitebox:
    Octolist.append(l)
print("[DEBUG]", Octolist)
for i in Octolist:
    temp = Octolist.count(i)
    print("[DEBUG] Occurence lettre ", i,": ", temp)
