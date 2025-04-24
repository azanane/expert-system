
import re

class RuleNode:

    def __init__(self, rule: str, facts = []):
        self.rule: str = rule
        self.left = self.__get_left_part()
        self.right = self.__get_right_part()
        self.expr = self.__get_expr()

        self.left_facts = {fact.literal: fact for fact in facts if fact.literal in self.left}
        self.right_facts = {fact.literal: fact for fact in facts if fact.literal in self.right}

    def __get_left_part(self):
        index = self.rule.find(">")
        return self.__side_to_expr(self.rule[:index - 1])

    def __get_right_part(self):
        index = self.rule.find(">")
        return self.__side_to_expr(self.rule[index + 1:])

    def __get_expr(self):
        left_for_expr = self.__side_to_expr(self.left)
        right_for_expr = self.__side_to_expr(self.right)
        return f'(not ({left_for_expr})) or ({right_for_expr})'

    def __side_to_expr(self, side: str):
        side = side.replace("+", " & ")
        side = side.replace("!", " not ")
        side = re.sub(r'not\s+([A-Z-(-)]+)', r'(not \1)', side)
        side = side.replace("^", " ^ ")
        side = side.replace("|", " | ")
        return side

    def print(self):
        print(f'------ Rule {self.rule} ------')
        print(f'left: {self.left}, right: {self.right}, expr: {self.expr}')
        print(f'left facts {self.left_facts}')
        print(f'right facts {self.right_facts}')

    def eval_left(self):
        assignment = {literal: fact.value for literal, fact in self.left_facts.items()}
        return eval(self.left, {}, assignment)

    def eval_expr(self):
        assignment = {literal: fact.value for literal, fact in self.left_facts.items()}
        assignment.update({literal: fact.value for literal, fact in self.right_facts.items()})
        return eval(self.expr, {}, assignment)

    def set_right_side(self):
        facts_changed = []
        for literal, fact in self.left_facts.items():
            fact.final = True
        for literal, fact in self.right_facts.items():
            if fact.final == True and fact.value != self.get_value_to_assign(literal, self.right):
                raise Exception(f"Might have a contradiction {self.rule}")
            fact.value = self.get_value_to_assign(literal, self.right)
            fact.default = False
            fact.final = True
            facts_changed.append(fact)

        for fact in facts_changed:
            fact.define_valid_rules(self)

    def get_value_to_assign(self, literal: str, expr: str):
        if expr.find(f'(not {literal})') != -1:
            return False
        return True