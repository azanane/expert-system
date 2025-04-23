# Propositional logic

Logic is the basis of all mathematical reasoning and all automated reasoning. The rules of logic specify the meaning of mathematical statements.

Let see the different truth table where T = true and F = false

### Negation

The negation "!" operator  
| A | !A |
| - | - |  
| T | F |   
| F | T |  

### Conjunction  

The AND "+" operator  
| A + B | C |  
| ------| - |   
| T + T | T |
| T + F | F |
| F + T | F |
| F + F | F |

### Disjunction
The OR "|" operator  
| A \| B | C |
| ------ | - |
| T \| T | T | 
| T \| F | T |
| F \| T | T |
| F \| F | F |

### XOR
The XOR operator "^"  

| A \^ B | C |  
|   -    | - |
| T \^ T | F |
| T \^ F | T |
| F \^ T | T |
| F \^ F | F |

### Implication
The implies operator

| A | B | A => B |
| - | - | ------ |
| T | T |   T    |
| T | F |   F    |
| F | T |   T    |
| F | F |   T    |

### Double implication
The double implication, if and only if

| A | B | A <=> B |
| - | - | ------- |
| T | T |    T    |
| T | F |    F    |
| F | T |    F    |
| F | F |    T    |
