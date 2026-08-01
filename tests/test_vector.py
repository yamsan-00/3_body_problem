"""Unit tests for the Vector class in vector.py."""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vector import Vector


def test_add():
    assert (Vector(1, 2) + Vector(3, 4)).tuple() == (4, 6)


def test_sub():
    assert (Vector(5, 6) - Vector(2, 1)).tuple() == (3, 5)


def test_mul_by_scalar():
    assert (Vector(2, 3) * 3).tuple() == (6, 9)


def test_magnitude():
    assert math.isclose(Vector(3, 4).magnitude(), 5.0)


def test_unit_of_nonzero_vector():
    u = Vector(3, 4).unit()
    assert math.isclose(u.magnitude(), 1.0, rel_tol=1e-9)


def test_unit_of_zero_vector_is_zero():
    z = Vector(0, 0).unit()
    assert z.tuple() == (0, 0)


def test_tuple_roundtrip():
    v = Vector(1.5, -2.5)
    assert v.tuple() == (1.5, -2.5)


def test_chained_ops():
    v = (Vector(1, 1) + Vector(2, 3)) - Vector(1, 1)
    assert v.tuple() == (2, 3)
