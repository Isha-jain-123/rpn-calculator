"""Unit tests for the RPN calculator."""

import math
import pytest
from rpn import evaluate


def test_addition():
    assert evaluate("3 4 +") == 7.0


def test_subtraction():
    assert evaluate("10 3 -") == 7.0


def test_multiplication():
    assert evaluate("6 7 *") == 42.0


def test_division():
    assert evaluate("20 4 /") == 5.0


def test_exponentiation():
    assert evaluate("2 10 ^") == 1024.0


def test_modulus():
    assert evaluate("17 5 %") == 2.0


def test_chained_expression():
    # (3 + 4) * 2 = 14
    assert evaluate("3 4 + 2 *") == 14.0


def test_complex_expression():
    # 5 + ((1 + 2) * 4) - 3 = 14
    assert evaluate("5 1 2 + 4 * + 3 -") == 14.0


def test_sqrt():
    assert evaluate("144 sqrt") == 12.0


def test_sin():
    assert evaluate("30 sin") == pytest.approx(0.5)


def test_cos():
    assert evaluate("60 cos") == pytest.approx(0.5)


def test_log():
    assert evaluate("1000 log") == pytest.approx(3.0)


def test_ln():
    assert evaluate("e ln") == pytest.approx(1.0)


def test_pi_constant():
    assert evaluate("pi") == pytest.approx(math.pi)


def test_neg():
    assert evaluate("5 neg") == -5.0


def test_abs():
    assert evaluate("5 neg abs") == 5.0


def test_sin_cos_identity():
    # sin²(45) + cos²(45) = 1
    assert evaluate("45 sin 2 ^ 45 cos 2 ^ +") == pytest.approx(1.0)


def test_not_enough_operands():
    with pytest.raises(ValueError, match="not enough operands"):
        evaluate("3 +")


def test_unknown_token():
    with pytest.raises(ValueError, match="unknown token"):
        evaluate("3 foo")


def test_too_many_values():
    with pytest.raises(ValueError, match="invalid expression"):
        evaluate("3 4")
