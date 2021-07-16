counter = 1


class DnaSequence:

    def __init__(self):
        self.__dna_id = None
        self.__dna_name = None
        self.__dna_string = None
        self.counter = 1

    def insert_values(self, dna_id, dna_name, dna_string):
        """
        :param dna_id:
        :param dna_name:
        :param dna_string:
        :return: dna's info if managed, false otherwise
        """
        global counter
        try:
            if self.is_valid_dna(dna_string):
                self.__dna_id = dna_id
                if dna_name is None:
                    dna_name = "seq{}".format(counter)
                    counter += 1
                self.__dna_name = dna_name
                self.__dna_string = dna_string
                if len(self.__dna_string) > 40:
                    sq = self.__dna_string[:40] + "..." + self.__dna_string[-3:]
                else:
                    sq = self.__dna_string
                return "[{}] {}: {}".format(self.__dna_id, self.__dna_name, sq)
            else:
                raise ValueError
        except ValueError:
            return False

    def get_id(self):
        """
        :return: id of dna_item
        """
        return self.__dna_id

    def get_name(self):
        """
        :return: name of dna_item
        """
        return self.__dna_name

    def get_string(self):
        """
        :return: sequence od dna_item
        """
        return self.__dna_string

    def is_valid_dna(self, sequence):
        """
        checks if sequence is a valid dna sequence
        :param sequence: to be checked
        :return: true if sequence is valid, false otherwise
        """
        for char in sequence:
            if char not in 'ACTG':
                return False
        return True

    def insert(self, nucleotide, index):
        """
        inserts a nucleotide to dna sequence and prints the dna's info, if didn't manage it will print a relevant message
        :param nucleotide: to be inserted
        :param index: where the nucleotide should be inserted
        :return: true if manged, false otherwise
        """
        try:
            if nucleotide in 'ACTG':
                if index <= len(self.__dna_string):
                    self.__dna_string = self.__dna_string[:index] + nucleotide + self.__dna_string[index:]
                    if len(self.__dna_string) > 40:
                        sq = self.__dna_string[:40] + "..." + self.__dna_string[-3:]
                    else:
                        sq = self.__dna_string
                    print("[{}] {}: {}".format(self.__dna_id, self.__dna_name, sq))
                    return True
                else:
                    raise IndexError
        except IndexError:
            print("Index out of range")
            return False
        except TypeError:
            print("Nucleotide should be one of the next chars: A,C,T,G")
            return False

    def assignment(self, new_dna):
        """
        changes the dna's data to be the new dna's data
        :param new_dna:
        :return:true if managed, false otherwise and prints a relevant message
        """
        try:
            if type(new_dna) is DnaSequence:
                self.__dna_id = new_dna.__dna_id
                self.__dna_name = new_dna.__dna_name
                self.__dna_string = new_dna.__dna_string
                print("[{}] {}: {}".format(self.__dna_id, self.__dna_name, self.__dna_string))
                return True
            else:
                raise TypeError
        except TypeError:
            print("New DNA must be a valid DNA")
            return False

    def __str__(self):
        """
        :return: dna's info as string
        """
        if len(self.__dna_string) > 40:
            sq = self.__dna_string[:40] + "..." + self.__dna_string[-3:]
        else:
            sq = self.__dna_string
        return "DNA id: {}, name: {}, sequence: {}".format(self.__dna_id, self.__dna_name, sq)

    def __eq__(self, other):
        """
        overrides == operator
        :param other: to be checked
        :return: true if equal, false otherwise
        """
        try:
            return self.__dna_id == other.dna_id and self.__dna_name == other.dna_name and self.__dna_string == other.dna_string
        except TypeError:
            print("Please send a valid DNA")
            return

    def __ne__(self, other):
        """
        overrides != operator
        :param other: to be checked
        :return: true if not equal, false otherwise
        """
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
        """
        overrides len()
        :return: the length of the dna's sequence
        """
        return len(self.__dna_string)
