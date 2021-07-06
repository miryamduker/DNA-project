class DnaSequence:

    def __init__(self, dna_string):
        if self.is_valid_dna(dna_string):
            self.dna_string = dna_string

    def is_valid_dna(self, str):
        for char in str:
            if char not in 'ACTG':
                return False
        return True

    def insert(self, nucleotide, index):
        try:
            if nucleotide in 'ACTG':
                self.dna_string = self.dna_string[:index] + nucleotide + self.dna_string[index:]
            else:
                raise TypeError
        except IndexError:
            return "Index out of range"
        except TypeError:
            return "Nucleotide should be one of the next chars: A,C,T,G"

    def assignment(self, new_dna):
        try:
            if type(new_dna) is str:
                if self.is_valid_dna(new_dna):
                    self.dna_string = new_dna
                else:
                    raise TypeError
            if type(new_dna) is DnaSequence:
                self.dna_string = new_dna.dna_string
        except TypeError:
            return "New DNA must be a valid DNA"

    def __str__(self):
        return "DNA is: {}".format(self.dna_string)

    def __eq__(self, other):
        try:
            return self.dna_string == other
        except TypeError:
            return "Please send a string"

    def __ne__(self, other):
        try:
            return self.dna_string != other
        except TypeError:
            return "Please send a string"

    def __getitem__(self, item):
        try:
            return self.dna_string[item]
        except IndexError:
            return "Index out of range"

    def __len__(self):
        return len(self.dna_string)
