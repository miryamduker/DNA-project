from dnaSequence import DnaSequence

data = []


def insert_data(new_name, new_dna):
    new_id = len(data) + 1
    dna = DnaSequence()
    result = dna.insert_values(new_id, new_name, new_dna)
    if not result:
        return False
    data.append(dna)
    return True


def get_dna_by_id(id):
    for dna in data:
        if dna.get_id() == id:
            return dna
    return "Id not found"


def get_dna_by_name(name):
    for dna in data:
        if dna.get_name() == name:
            return dna
    return "Name not found"
