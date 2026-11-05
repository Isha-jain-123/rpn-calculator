"""
Reverse Polish Notation (RPN) calculator.

Supports the four basic operators (+, -, *, /), exponentiation (^),
modulus (%), and a handful of unary functions (sqrt, sin, cos, tan,
log, ln, abs, neg).  Also recognises the constants 'pi' and 'e'.

Usage
-----
Run the script and type an RPN expression at the prompt, or pipe one in::

    $ python rpn.py
    rpn> 3 4 + 2 *
    14.0
    rpn> 45 sin 2 ^  45 cos 2 ^  +
    1.0
    rpn> quit
"""

import math
import sys

OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "^": lambda a, b: a ** b,
    "%": lambda a, b: a % b,
}

UNARY = {
    "sqrt": math.sqrt,
    "sin":  lambda x: math.sin(math.radians(x)),
    "cos":  lambda x: math.cos(math.radians(x)),
    "tan":  lambda x: math.tan(math.radians(x)),
    "log":  math.log10,
    "ln":   math.log,
    "abs":  abs,
    "neg":  lambda x: -x,
}

CONSTANTS = {
    "pi": math.pi,
    "e":  math.e,
}


def evaluate(expression: str) -> float:
    """Evaluate a single RPN expression and return the result."""
    stack: list[float] = []
    for token in expression.split():
        if token in CONSTANTS:
            stack.append(CONSTANTS[token])
        elif token in OPERATORS:
            if len(stack) < 2:
                raise ValueError(f"not enough operands for '{token}'")
            b, a = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](a, b))
        elif token in UNARY:
            if not stack:
                raise ValueError(f"not enough operands for '{token}'")
            stack.append(UNARY[token](stack.pop()))
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"unknown token: '{token}'")
    if len(stack) != 1:
        raise ValueError(f"invalid expression (stack has {len(stack)} values)")
    return stack[0]


def repl() -> None:
    """Run a read-eval-print loop."""
    print("RPN calculator  (type 'quit' to exit)")
    while True:
        try:
            line = input("rpn> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line or line == "quit":
            break
        try:
            result = evaluate(line)
            print(result)
        except Exception as err:
            print(f"error: {err}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(evaluate(" ".join(sys.argv[1:])))
    else:
        repl()
