class prop_1:

    alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"

    def decimale_base(n, base):
        l = len(prop_1.alphabet)
        if base > l:
            raise RuntimeError(f"La base demandee est trop grande pour ce programe (maximum: {l})")
        if n < 0:
            raise RuntimeError("Le nombre doit etre positif (ou égal a 0)")
        a = prop_1.alphabet[:base]
        if n == 0:
            return a[0]
        quotient = n
        nb = []
        while quotient != 0:
            reste = quotient % base
            quotient = quotient // base
            nb.append(a[reste])
        final = "".join(reversed(nb))
        return final
    
    def decimale_binaire (n):
        return prop_1.decimale_base(n, 2)

    def decimale_exadecimale(n):
        return prop_1.decimale_base(n, 16)

class prop_2:

    def norme_IEEE(n):
        if n >= 0:
            final = "0 "
        else:
            final = "1 "
        n = abs(n)
        n_lst = [int(n), n-int(n)]
        b_entier = prop_1.decimale_binaire(n_lst[0])
        ex = 0
        if len(b_entier) > 23:
            ex = len(b_entier)-1
            b_entier = b_entier[:24]
        n_dec = n_lst[1]
        b_dec = ""
        result = n_dec
        while len(b_entier + b_dec) < 24:
            result = str(result*2).split(".")
            b_dec = b_dec + result[0]
            result = float("0." + result[1])
        if round(result) == 1:
            suf = len(b_dec.split("0")[-1])
            b_dec = b_dec[0:len(b_dec)-suf-1]
            b_dec = b_dec + "1" + "0"*suf
        else:
            b_dec = b_dec
        if ex == 0:
            if b_entier == "0":
                ex = -(b_dec.split("1")[0].count("0") + 1)
            else:
                ex = len(b_entier)-1
        ex = prop_1.decimale_binaire(ex+127)
        ex = "0"*(8-len(ex)) + ex
        b = (b_entier+b_dec)[1:]
        final = final + ex + " " + b
        return final
    
    def somme(n, m):
        r = float(str(n + m)[0 : max(len(str(n)), len(str(m)))+1])
        return r, prop_2.norme_IEEE(r)



print("""Bienvenue, veuillez choisir une des deux proposition:
(1): Convertion d'entiers positifs
(2): Norme IEEE 754""") 
proposition = input()

if proposition == "1":
    print("Quelle partie de l'exercice voulez-vous executer?")
    ex = input()
    if ex == "1":
        n = int(input("Nombre a convertir (entier et en base décimale): "))
        print(prop_1.decimale_base(n, 2) + " (base 2)")
    elif ex == "2":
        n = int(input("Nombre a convertir (entier et en base décimale): "))
        print(prop_1.decimale_base(n, 16) + " (base 16)")
    elif ex == "3":
        n = int(input("Nombre a convertir (entier et en base décimale): "))
        base = int(input("Base demandée (entier et en base décimale): "))
        print(prop_1.decimale_base(n, base) + " (base " + str(base) + ")")
    else:
        print("ERREUR: Il n'y a pas d'éxercice à ce numérot")

elif proposition == "2":
    print("Quelle partie de l'exercice voulez-vous executer?")
    ex = input()
    if ex == "1":
        print("La norme IEE-754 est un moyen d'écrir des nombres flotants en binaire très précisément dans un ordinateur.")
        print("Ces nombres peuvent s'écrir, par convention, avec 32 ou 64 bits. Plus le nombre de bits est ellevé,")
        print("plus le nombre écris sera précis. Dans cette norme, les bits sont répartis en trois valeures: 1 bit")
        print("pour le signe du nombre (0 si positif et 1 si négatif), 8 bits pour l'exposant, et le reste des bits")
        print("disponibles sont réservés à la mantisse, c'est à dire tous les chifres de ce nombre en binaire, sauf")
        print("le premier (celui le plus a gauche) depuis la gauche.")
    elif ex == "2":
        print(prop_2.norme_IEEE(float(input("Nombre a convertir (base décimale): "))))
    elif ex == "3":
        n = float(input("Nombre no 1: "))
        m = float(input("Nombre no 2: "))
        print(str(prop_2.somme(n, m)))
    else:
        raise RuntimeError("ERREUR: Il n'y a pas d'éxercice à ce numérot")