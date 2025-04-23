from argparse import ArgumentParser

class Parser:

    def __init__(self):
        self.exprs = []
        self.initial_facts = []
        self.querries = []
        
        self.file_path = self.__get_file_path()
        self.__parse_file(self.file_path)

        self.all_literals = self.__get_literals()
        self.__validate_querry()

    def __get_literals(self):
        all_literals = []
        for expr in self.exprs:
            for literal in expr:
                if literal.isalpha() and literal not in all_literals:
                    all_literals.append(literal)
        return all_literals
        
    def __get_file_path(self):
        parser = ArgumentParser()
        parser.add_argument("-f", "--file", dest="data_file", help="Enter file path")

        args = parser.parse_args()
        file_path = args.data_file
        if (file_path is None):
            print("Correct format: python3 main.py -f {file_path}")
            exit(1)
        return file_path

    def __validate_querry(self):
        for querry in self.querries:
            if querry not in self.all_literals:
                raise Exception(f"Querry {querry} not in expressions {self.exprs}")

    def __parse_file(self, file_path):
        get_query = False
        with open(file_path) as input_file:
            for line in input_file:
                hashtag_pos = line.find('#')
                line = line[0:hashtag_pos if hashtag_pos != -1 else len(line)]
                line = line.replace(" ", '')
                line = line.replace("\n", '')
                if line.startswith('#') or len(line) == 0:
                    continue
                if line.startswith('='):
                    self.__check_chars_upper(line[1:])
                    for letter in line[1:]:
                        if letter in self.initial_facts:
                            raise Exception("Letter wrote multiple times.")
                        self.initial_facts.append(letter)
                elif line.startswith('?'):
                    self.__check_chars_upper(line[1:])
                    for letter in line[1:]:
                        if letter in self.querries:
                            raise Exception("Letter wrote multiple times.")
                        self.querries.append(letter)
                    get_query = True
                else:
                    self.__check_sign_between_char(line)
                    self.__check_chars_upper(line, False)
                    self.__check_signs(line)
                    self.__check_implication(line)
                    self.exprs.append(line)

        if len(self.exprs) < 1:
            raise Exception('Please add a logical proposition line. Exemple : A + B => C')
        if not get_query:
            raise Exception('Please add a query line. Exemple : ?ABC')
        return True
                
    def __check_sign_between_char(self, line):
        old_letter = ''
        for letter in line:
            if letter.isalpha() and old_letter.isalpha():
                raise Exception(f'Error in the line {line}')
            old_letter = letter

    def __check_chars_upper(self, line, isalpha=True):
        for letter in line:
            if (letter.isalpha() and not letter.isupper()) or (isalpha and not letter.isalpha()):
                raise Exception(f'Char {letter} in line {line} is not in uppercase')

    def __check_signs(self, line):
        signs_possible = ['+', '|', '^', '!', '=', '>', '(', ')']
        right_side = False
        for letter in line:
            if letter not in signs_possible and not letter.isalpha():
                raise Exception(f'Char {letter} in line {line} is not supported.')
            if right_side and letter in ('|', '^', '=', '>'):
                raise Exception(f'You have either an OR a XOR in conclusion or several implication which are not supported')
            if letter == '>':
                right_side = True
    
    def __check_implication(self, line):
        if "=>" not in line and "<=>" not in line:
            raise Exception(f'Must have an implication at the line : {line}')
                
    