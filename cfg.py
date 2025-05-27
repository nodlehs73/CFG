import random


class CFG:
    def __init__(self):
        self.terminals = {"a", "b"}
        self.non_terminals = {"S"}
        self.transitions = {"S": ["aSb", ""]}
        self.start_symbol = "S"
        self.random_strings = []

    def has_non_terminals(self, current_string):
        for symbol in current_string:
            if symbol in self.non_terminals:
                return True

        return False

    def generate_next(self, generated_string):
        next_strings = []

        for symbol in generated_string:
            if symbol in self.non_terminals:
                for transition in self.transitions[symbol]:
                    next_string = generated_string.replace(symbol, transition)
                    next_strings.append(generated_string.replace(symbol, transition))

        return next_strings

    def get_random_strings (self, max_length):
        if len (self.random_strings):
            self.random_strings.clear()

        def generate_random_strings(current_string, max_length):
            if not self.has_non_terminals(current_string) and len (current_string) <= max_length:
                self.random_strings.append(current_string)

            if len(self.random_strings) > 10 or len (current_string) > max_length + 1:
                return

            next_strings = self.generate_next(current_string)

            for next_string in next_strings:
                 generate_random_strings(next_string, max_length)

        generate_random_strings(self.start_symbol, max_length)

        random.shuffle (self.random_strings)

        return self.random_strings

    def get_derivation (self, derivation_string):
        derivation_strings = []

        def search_derivation (current_string):
            if len (current_string) > len (derivation_string) + 1:
                return False

            if current_string == derivation_string:
                derivation_strings.append (current_string)
                return True


            next_strings = self.generate_next (current_string)

            for next_string in next_strings:
                if search_derivation (next_string):
                    derivation_strings.append (current_string)
                    return True

            return False

        search_derivation (self.start_symbol)

        return " -> ".join (derivation_strings[::-1])

    def membership_test (self, testing_string):
       self.get_random_strings(12)

       return testing_string in self.random_strings



if __name__ == "__main__":
    cfg = CFG ()
    print (cfg.get_random_strings(10))

    print (cfg.get_derivation("aaaabbbb"))

    print (cfg.membership_test("ab"))



