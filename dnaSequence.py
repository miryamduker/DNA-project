# from functions import check_function_name

counter = 1


class DnaSequence:

    def __init__(self):
        self.__dna_id = None
        self.__dna_name = None
        self.__dna_string = None
        self.counter = 0

    def insert_values(self, dna_id, dna_name, dna_string):
        global counter
        try:
            if self.is_valid_dna(dna_string):
                self.__dna_id = dna_id
                if dna_name is None:
                    dna_name = "seq{}".format(counter)
                    # while not check_function_name(dna_name):
                    #     counter += 1
                    #     dna_name = "seq{}".format(counter)
                    counter += 1
                self.__dna_name = dna_name
                self.__dna_string = dna_string
                return "[{}] {}: {}".format(self.__dna_id, self.__dna_name, self.__dna_string)
            else:
                raise ValueError
        except ValueError:
            return False

    def get_id(self):
        return self.__dna_id

    def get_name(self):
        return self.__dna_name

    def get_string(self):
        return self.__dna_string

    def is_valid_dna(self, str):
        for char in str:
            if char not in 'ACTG':
                return False
        return True

    def insert(self, nucleotide, index):
        try:
            if nucleotide in 'ACTG':
                if index <= len(self.__dna_string):
                    self.__dna_string = self.__dna_string[:index] + nucleotide + self.__dna_string[index:]
                    return "[{}] {}: {}".format(self.__dna_id, self.__dna_name, self.__dna_string)
                else:
                    raise IndexError
        except IndexError:
            print("Index out of range")
            return False
        except TypeError:
            print("Nucleotide should be one of the next chars: A,C,T,G")
            return False

    def assignment(self, new_dna):
        try:
            if type(new_dna) is DnaSequence:
                self.__dna_id = new_dna.__dna_id
                self.__dna_name = new_dna.__dna_name
                self.__dna_string = new_dna.__dna_string
                return "[{}] {}: {}".format(self.__dna_id, self.__dna_name, self.__dna_string)
            else:
                raise TypeError
        except TypeError:
            return "New DNA must be a valid DNA"

    def __str__(self):
        return "DNA id: {}, name: {}, sequence: {}".format(self.__dna_id, self.__dna_name, self.__dna_string)

    def __eq__(self, other):
        try:
            return self.__dna_id == other.dna_id and self.__dna_name == other.dna_name and self.__dna_string == other.dna_string
        except TypeError:
            print("Please send a valid DNA")
            return

    def __ne__(self, other):
        try:
            return self.__dna_id != other.dna_id or self.__dna_name == other.dna_name or self.__dna_string != other.dna_string
        except TypeError:
            print("Please send a valid DNA")
            return

    def __getitem__(self, item):
        try:
            return self.__dna_string[item]
        except IndexError:
            print("Index out of range")
            return

    def __len__(self):
        return len(self.__dna_string)
