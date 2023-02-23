from random import randint


class Validation:
    @staticmethod
    def validate_try(try_to_validate: str, digits_limit: int) -> bool:
        if try_to_validate.find(' ') != -1:
            try_to_validate = ''.join(try_to_validate.split())
        if len(try_to_validate) != digits_limit:
            return False

        for char in try_to_validate:
            if char.isdigit() is False:
                return False

        return True

    @staticmethod
    def validate_int_num(num_to_validate: str, num_range: range) -> bool:
        try:
            num_to_validate: int = int(num_to_validate)
        except TypeError:
            return False

        if num_to_validate not in num_range:
            return False
        else:
            return True

    @staticmethod
    def validate_y_or_n_char(char: str):
        if type(char) != str:
            return False

        char = char.lower()
        if char != 'y' and char != 'n':
            return False
        else:
            return True


class Game:
    def __init__(self):
        self.__trials_limit: int = 12
        self.__digits_limit: int = 5
        self.__is_difficult: bool = True
        self.__actual_try: int = 1
        self.__welcome()
        self.__code: str = Generator(self.__digits_limit, self.__is_difficult).generate_code()

    def __check_try(self, tried_code: str) -> bool:
        verdict_in_place: int = 0
        verdict_in_code: int = 0
        tmp_code: str = self.__code
        indexes: list[int] = [i for i in range(len(tmp_code))]
        zipped_codes: tuple = tuple(zip(indexes, tmp_code, tried_code))

        for i, code_chr, tried_code_chr in zipped_codes:
            if code_chr == tried_code_chr:
                verdict_in_place += 1
                tmp_code = tmp_code[:i] + '!' + tmp_code[i+1:]
            elif tried_code_chr in tmp_code:
                verdict_in_code += 1
                tmp_index: int = tmp_code.find(tried_code_chr)
                tmp_code = tmp_code[:tmp_index] + '!' + tmp_code[tmp_index+1:]

        if verdict_in_place == self.__digits_limit:
            print("You are the Winner! Good Job!")
            return True
        else:
            print(f"You have {verdict_in_place} digits on the right place{'s' if verdict_in_place > 1 else ''},"
                  f"and {verdict_in_code} digit{'s' if verdict_in_code > 1 else ''} which "
                  f"{'are' if verdict_in_code > 1 else 'is'} in the code but on wrong place")

            return False

    def get_trials_limit(self):
        return self.__trials_limit

    def next_try(self):
        self.__actual_try += 1

    def get_actual_try(self):
        return self.__actual_try

    def get_try(self) -> bool:
        got_try: str = input("Type Your guess: ")
        while Validation.validate_try(got_try, self.__digits_limit) is False:
            got_try = input("Wrong code! Try again: ")

        return self.__check_try(got_try)

    def __welcome(self):
        with open("Welcome_text.txt", 'r') as welcome_text_file:
            text = welcome_text_file.read().rstrip().split('\n\n')

        print(text[0])
        choose: str = input("Do You want to change number of digits in generated code? (y/n): ")
        while Validation.validate_y_or_n_char(choose) is False:
            print("Wrong value!")
            choose = input("Do You want to change number of digits in generated code? (y/n): ")

        choose = choose.lower()
        if choose == 'y':
            new_nuber: str = input("Type number of digits in code (1-20): ")
            while Validation.validate_int_num(new_nuber, range(1, 21)) is False:
                print("Wrong value!")
                new_nuber: str = input("Type number of digits in code (1-20): ")
            self.__digits_limit = int(new_nuber)
            print("Value changed successfully")

        print(text[1])
        choose: str = input("Do You want to change number of trials? (y/n): ")
        while Validation.validate_y_or_n_char(choose) is False:
            print("Wrong Value!")
            choose = input("Do You want to change number of trials? (y/n): ")

        choose = choose.lower()
        if choose == 'y':
            new_number: str = input("Type numer of trials (1-100): ")
            while Validation.validate_int_num(new_number, range(1, 100)) is False:
                print("Wrong Values!")
                new_number = input("Type numer of trials (1-100): ")
            self.__trials_limit = int(new_number)
            print("Value changed successfully")

        print(text[2])
        choose: str = input("Do You want to change difficulty level to easy? (y/n): ")
        while Validation.validate_y_or_n_char(choose) is False:
            print("Wrong number!")
            choose = input("Do You want to change difficulty level to easy? (y/n): ")

        choose = choose.lower()
        if choose == 'y':
            self.__is_difficult = False
            print("Value changed successfully")
        print(text[-1])


class Generator:
    def __init__(self, digits_limit: int, is_difficult: bool):
        self.__digits_limit: int = digits_limit
        self.__is_difficult: int = is_difficult

    def generate_code(self) -> str:
        code: str = ""
        for _ in range(self.__digits_limit):
            rand_num: str = str(randint(0, 9))

            if self.__is_difficult is False:
                while rand_num in code:
                    rand_num = str(randint(0, 9))

            code += rand_num
        print(code)
        return code


if __name__ == '__main__':
    play = Game()

    while play.get_actual_try() <= play.get_trials_limit():
        play.get_try()
        play.next_try()
