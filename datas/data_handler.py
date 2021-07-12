from datas.dna_data import data_with_id_key, data_with_name_key
from dnaSequence import DnaSequence


def get_new_id():
    return len(data_with_id_key) + 1


def insert_data(new_name, new_dna):
    dna = DnaSequence()
    result = dna.insert_values(get_new_id(), new_name, new_dna)
    if not result:
        print("DNA not valid")
        return False
    data_with_id_key[dna.get_id()] = dna
    data_with_name_key[dna.get_name()] = dna
    print(result)
    return True


def get_dna_by_id(id):
    return data_with_id_key.get(id)


def get_dna_by_name(name):
    return data_with_name_key.get(name)
