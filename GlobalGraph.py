from Parsing import Parser

class GlobalGraph:
    def __init__(self, parser: Parser):
        self.initial_facts = parser.initial_facts
        self.querries = parser.querries
        self.facts, self.rules = parser.init_facts_and_rules_node()

        self.runned = False

    def run(self):
        # If we have inital facts we start our inference algorithm by these nodes
        if self.initial_facts != []:
            for literal, fact in self.facts.items():
                if literal in self.initial_facts:
                    fact.define_valid_rules(None)

        # If it is not satified after inital fact assignment we go throughout the rules to define them
        if not self.satified():
            for rule in self.rules:
                if rule.eval_left():
                    rule.set_right_side()

        self.runned = True
    
    def satified(self):
        for rule in self.rules:
            if not rule.eval_expr():
                return False
        return True

    def print_result(self):
        if self.runned:
            for querry in self.querries:
                print(f'{querry}: {self.facts[querry].value}')
        else:
            print(f'You must run the algorithm in order to print the result.')