# RPN Calculator

A stack-based Reverse Polish Notation calculator in Python. Supports basic arithmetic, exponentiation, modulus, and scientific functions (sin, cos, tan, sqrt, log, ln).

## Usage

Interactive mode:

```
$ python rpn.py
RPN calculator  (type 'quit' to exit)
rpn> 3 4 + 2 *
14.0
rpn> 45 sin 2 ^  45 cos 2 ^  +
1.0
rpn> quit
```

Single expression from the command line:

```
$ python rpn.py 5 1 2 + 4 '*' + 3 -
14.0
```

## Supported operations

| Token | Operation |
|-------|-----------|
| `+` `-` `*` `/` | Basic arithmetic |
| `^` | Exponentiation |
| `%` | Modulus |
| `sqrt` | Square root |
| `sin` `cos` `tan` | Trig functions (degrees) |
| `log` | Base-10 logarithm |
| `ln` | Natural logarithm |
| `abs` | Absolute value |
| `neg` | Negate |
| `pi` `e` | Constants |

## Tests

```bash
pip install pytest
pytest test_rpn.py -v
```
