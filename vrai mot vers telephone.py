def wordforphone(mot = None):
    if not mot:
        mot = input()
    mot = list(str(mot).lower())
    mot2 = []
    a = 0
    for n in mot:
        a += 1
        if n != " ":
            n = n.replace("a","2").replace("b","22").replace("c","222").replace("d","3").replace("e","33").replace("f","333").replace("g","4").replace("h","44")
            n = n.replace("i","444").replace("j","5").replace("k","55").replace("l","555").replace("m","6").replace("n","66").replace("o","666").replace("p","7")
            n = n.replace("q","77").replace("r","777").replace("s","7777").replace("t","8").replace("u","88").replace("v","888").replace("w","9").replace("x","99")
            n = n.replace("y","999").replace("z","9999")
            mot2.append(n)
            if a < len(mot):
                mot2.append(" - ")
    mot2 = str(mot2).replace("[","").replace("]","").replace("'","").replace(",","").replace("  "," ")
    print(mot2)
    input("PRESS ENTER TO EXIT")

if __name__ == '__main__':
    wordforphone()
