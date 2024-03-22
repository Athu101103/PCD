class PredictiveParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.first = {}
        self.follow = {}
        self.build_first()
        self.build_follow()

    def build_first(self):
        for non_terminal in self.grammar:
            self.first[non_terminal] = set()
            self.calculate_first(non_terminal)

    def calculate_first(self, non_terminal):
        if non_terminal in self.first:
            return self.first[non_terminal]
        for production in self.grammar[non_terminal]:
            for symbol in production:
                if symbol.isupper():
                    self.first[non_terminal] |= self.calculate_first(symbol)
                    if 'ε' not in self.first[symbol]:
                        break
                else:
                    self.first[non_terminal].add(symbol)
                    break
        return self.first[non_terminal]

    def build_follow(self):
        start_symbol = list(self.grammar.keys())[0]
        self.follow[start_symbol] = {'$'}
        for non_terminal in self.grammar:
            self.follow[non_terminal] = set()
        while True:
            updated = False
            for non_terminal in self.grammar:
                for production in self.grammar[non_terminal]:
                    for i, symbol in enumerate(production):
                        if symbol.isupper():
                            first_of_next = self.first[production[i+1]] if i < len(production) - 1 else {'$'}
                            if 'ε' in self.first[symbol]:
                                if i == len(production) - 1:
                                    updated |= self.follow[non_terminal] != self.follow[non_terminal] | self.follow[symbol]
                                    self.follow[non_terminal] |= self.follow[symbol]
                                else:
                                    updated |= self.follow[non_terminal] != self.follow[non_terminal] | (first_of_next - {'ε'})
                                    self.follow[non_terminal] |= first_of_next - {'ε'}
                            else:
                                updated |= self.follow[non_terminal] != self.follow[non_terminal] | first_of_next
                                self.follow[non_terminal] |= first_of_next
            if not updated:
                break

    def parse(self, input_string):
        stack = ['$']
        input_string += '$'
        output = []

        current_symbol = input_string[0]
        input_pointer = 1
        while len(stack) > 0:
            top_of_stack = stack.pop()
            if top_of_stack == current_symbol:
                if current_symbol == '$':
                    break
                output.append(f"Matched {current_symbol}")
                current_symbol = input_string[input_pointer]
                input_pointer += 1
            elif top_of_stack in self.grammar:
                if current_symbol not in self.grammar[top_of_stack]:
                    return "Parsing Error: Unexpected symbol"
                output.append(f"Expanded {top_of_stack} -> {' '.join(self.grammar[top_of_stack][current_symbol])}")
                stack.extend(reversed(self.grammar[top_of_stack][current_symbol]))
            else:
                return "Parsing Error: Unexpected symbol"
        
        return "\n".join(output)


def get_grammar_from_user():
    grammar = {}
    while True:
        non_terminal = input("Enter non-terminal (or press Enter to finish): ").strip()
        if not non_terminal:
            break
        productions = input(f"Enter productions for {non_terminal}: ").strip().split('|')
        grammar[non_terminal] = [p.strip().split() for p in productions]
    return grammar


def main():
    user_grammar = get_grammar_from_user()
    parser = PredictiveParser(user_grammar)
    input_string = input("Enter input string: ")
    print(parser.parse(input_string))


if __name__ == "__main__":
    main()
