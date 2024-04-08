import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    #načtení povolených klíčů (field) ze souboru
    with open("sequential.json", "r") as f:
        allowed_key = json.load(f)
    #ověření, zda je klíč v množině povolených klíčů
    if field not in allowed_key:
        return None
    with open(file_name, "r") as f:
        data = json.load(f)
    #vrácení hodnot
    return data.get(field)

def linear_search(prohledavana_data, hledane_cislo):
    pozice = []
    for idx, i in enumerate(prohledavana_data):
        if i == hledane_cislo:
            pozice.append(idx)

    pocet = prohledavana_data.count(hledane_cislo)
    slovnik = {"pozice" : pozice, "pocet": pocet}
    return slovnik
def pattern_search(proh_sek, hledany_vzor):
    lis = []
    for j in range(len(proh_sek)-len(hledany_vzor)+1):
        k = proh_sek[j:j+len(hledany_vzor)]
        if k == hledany_vzor:
            lis.append(j)
        else:
            continue

    mnozina = set(lis)
    return mnozina

def main():
    #pass
    #zavolat funkci read_data s pozadovanými vstupy
    sequential_data = read_data("sequential.json", "dna_sequence")
    #vytiskni obsah promenne  sequential_data
    print(sequential_data)
    number = "A"
    slovnik = linear_search(sequential_data, number)
    print(slovnik)
    vzor = "AA"
    mnozina = pattern_search(sequential_data, vzor)
    print(mnozina)



if __name__ == '__main__':
    main()