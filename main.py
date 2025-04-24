
from Parsing import Parser
import re
from RuleNode import RuleNode
from Node import FactNode

if __name__ == "__main__":
    try:
        parser = Parser()

        print(f'Parser exprs {parser.exprs}')
        print(f'Parser literals {parser.all_literals}')

        facts, rules = parser.init_facts_and_rules_node()

        if parser.initial_facts != []:
            for fact in facts:
                if fact.literal in parser.initial_facts:
                    fact.define_valid_rules(None)
        else:
            for rule in rules:
                if rule.eval_left():
                    rule.set_right_side()

        for fact in facts:
            if fact.literal in parser.querries:
                print(f'{fact.literal}: {fact.value}')

    except Exception as e:
        print(f'{str(e)}')
        exit(1)