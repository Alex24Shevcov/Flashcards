import argparse


class FlashCards:
    def __init__(self):
        self._count_saved_cards = 0
        self._dictionary = dict()
        with open("tmp_log.txt", "w") as file:
            pass

    def input_or_output_to_tmp_log(self, text: str) -> str:
        with open("tmp_log.txt", "a") as file:
            file.write(text + "\n")
        return text

    def _input_definition(self) -> str:
        while True:
            lol_exist = False
            definition = self.input_or_output_to_tmp_log(input())
            for arr in self._dictionary.values():
                if arr[0] == definition:
                    print(self.input_or_output_to_tmp_log(f'The definition "{definition}" already exists. Try again:'))
                    lol_exist = True
                    break
            if lol_exist:
                continue
            return definition

    def _input_term(self) -> str:
        while True:
            lol_exist = False
            term = self.input_or_output_to_tmp_log(input())
            for key in self._dictionary.keys():
                if key == term:
                    print(self.input_or_output_to_tmp_log(f'The term "{term}" already exists. Try again:'))
                    lol_exist = True
                    break
            if lol_exist:
                continue
            return term

    def _wrong_unswer(self, term, unswer):
        for key, arr in self._dictionary.items():
            if arr[0] == unswer:
                print(self.input_or_output_to_tmp_log(f'Wrong. The right answer is "{self._dictionary[term][0]}",'
                                                      f' but your definition is correct for "{key}".'))
                return 0
        return None

    def add(self):
        term = self.input_or_output_to_tmp_log(self._input_term())
        definition = self.input_or_output_to_tmp_log(self._input_definition())
        self._dictionary[term] = [definition, 0]
        print(self.input_or_output_to_tmp_log(f'The pair ("{term}":"{definition}") has been added.'))

    def remove(self):
        print(self.input_or_output_to_tmp_log("Which card?"))
        term = self.input_or_output_to_tmp_log(input())
        for key in self._dictionary.keys():
            if term == key:
                self._dictionary.pop(key)
                print(self.input_or_output_to_tmp_log("The card has been removed."))
                return

        print(self.input_or_output_to_tmp_log(f'Can\'t remove "{term}": there is no such card.'))

    def inport(self, path=""):
        print(self.input_or_output_to_tmp_log("File name:"))
        if path == "":
            path_to_file = self.input_or_output_to_tmp_log(input())
        else:
            path_to_file = path

        try:
            with open(path_to_file, 'r') as file:
                i = 0
                for line in file:
                    line = line.strip()
                    term, definition, count_errors = line.split()
                    self._dictionary[term] = [definition, int(count_errors)]
                    i += 1
                print(self.input_or_output_to_tmp_log(f'{i} cards have been loaded.'))
        except FileNotFoundError:
            print(self.input_or_output_to_tmp_log("File not found."))

    def export(self, path=""):
        print(self.input_or_output_to_tmp_log("File name:"))
        if path == "":
            path_to_file = self.input_or_output_to_tmp_log(input())
        else:
            path_to_file = path

        with open(path_to_file, 'w') as file:
            i = 0
            for term, arr in self._dictionary.items():
                line = f'{term} {arr[0]} {arr[1]}\n'
                file.write(line)
                i += 1
            print(self.input_or_output_to_tmp_log(f"{i} cards have been saved."))

    def ask(self):
        print(self.input_or_output_to_tmp_log("How many times to ask?"))
        n = int(self.input_or_output_to_tmp_log(input()))
        dict_cards = []
        for i in self._dictionary.items():
            dict_cards.append(i)

        for i in range(n):
            term = dict_cards[i % len(dict_cards)][0]
            arr = dict_cards[i % len(dict_cards)][1]

            print(self.input_or_output_to_tmp_log(f'Print the definition of "{term}":'))
            unswer = self.input_or_output_to_tmp_log(input())
            if arr[0] == unswer:
                print(self.input_or_output_to_tmp_log("Correct!"))
            else:
                if self._wrong_unswer(term, unswer) is None:
                    print(self.input_or_output_to_tmp_log(f'Wrong. The right answer is "{arr[0]}".'))
                self._dictionary[term][1] += 1
            n -= 1

    def exit_program(self, export_to_file=""):
        print(self.input_or_output_to_tmp_log("Bye bye!"))
        if export_to_file != "":
            self.export(export_to_file)
        exit()

    def log(self):
        print(self.input_or_output_to_tmp_log("File name:"))
        path_to_file = self.input_or_output_to_tmp_log(input())
        with open(path_to_file, "a") as log_file, open("tmp_log.txt", "r") as tmp_log_file:
            text_from_tmp_log_file = tmp_log_file.read()
            log_file.write(text_from_tmp_log_file)
        print(self.input_or_output_to_tmp_log("The log has been saved."))


    def hardest_card(self):
        max_errors = 0
        for term, arr in self._dictionary.items():
            if arr[1] > max_errors:
                max_errors = arr[1]

        if max_errors == 0:
            print(self.input_or_output_to_tmp_log("There are no cards with errors."))
            return

        arr_term_max_errors = []
        for term, arr in self._dictionary.items():
            if arr[1] == max_errors:
                arr_term_max_errors.append('"' + term + '"')

        s = ""
        for i in arr_term_max_errors:
            s += i + ", "
        s = s[:len(s) - 2]
        if len(arr_term_max_errors) > 1:
            print(self.input_or_output_to_tmp_log('The hardest cards are ' + s + ". You have "
                                                  + str(max_errors)
                                                  + " errors answering them."))
        else:
            print(self.input_or_output_to_tmp_log('The hardest card is ' + s + ". You have "
                                                  + str(max_errors)
                                                  + " errors answering it."))

    def reset_stats(self):
        for term, arr in self._dictionary.items():
            self._dictionary[term][1] = 0
        print(self.input_or_output_to_tmp_log("Card statistics have been reset."))



parser = argparse.ArgumentParser()
parser.add_argument("--import_from", default="")
parser.add_argument("--export_to", default="")
args = parser.parse_args()


cards = FlashCards()

if args.import_from != "":
    cards.inport(args.import_from)

while True:
    print(cards.input_or_output_to_tmp_log("\nInput the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):"))
    choice = cards.input_or_output_to_tmp_log(input())

    if choice == "add":
        cards.add()

    elif choice == "remove":
        cards.remove()

    elif choice == "import":
        cards.inport()

    elif choice == "export":
        cards.export()

    elif choice == "ask":
        cards.ask()

    elif choice == "exit":
        cards.exit_program(args.export_to)

    elif choice == "log":
        cards.log()

    elif choice == "hardest card":
        cards.hardest_card()

    elif choice == "reset stats":
        cards.reset_stats()

