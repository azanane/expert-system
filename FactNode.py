

class FactNode:

    def __init__(self, literal: str, value = False, final = False, default = True):
        self.literal: str = literal
        self.value: bool = value
        self.default = default
        self.final: bool = final

        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def print(self):
        print(f'------ Fact: {self.literal} ------')
        print(f'value: {self.value}, default: {self.default}, rules: {[rule.rule for rule in self.rules]}')

    def get_next_valid_rule(self):
        for rule in self.rules:
            if rule.eval_left() and not rule.eval_expr():
                return rule
        return None

    def define_valid_rules(self, rule_comming_from):
        for rule in self.rules:
            if rule.eval_left() and not rule.eval_expr() and rule != rule_comming_from:
                rule.set_right_side()

