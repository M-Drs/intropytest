

def inverse(chaine):
    if isinstance(chaine,int):
        raise ValueError("vous devez passer une chaine de caractères")
    

    for element in chaine : 
        if not isinstance(element,str):
            raise ValueError("vous devez passer une chaine de carac")
    
    if len(chaine) == 4 and isinstance(chaine,list):
        chaine.pop()

    chaine = "".join(chaine)

    return chaine [::-1]




if __name__ == "__main__":

    print(inverse("abcd"))
    print(inverse('hello'))
    print(inverse(["a","b","c","d"]))
    print(inverse(["a",8]))

            