import pytest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(current_dir, "..")
sys.path.append(module_dir)

from turing_machine import turing_machine as dtm

@pytest.mark.parametrize("data", [
    "ac",
    "bc",
    "aacc",
    "bbcc",
    "abcc",
    "aaaccc",
    "bbbccc",
    "aabccc",
    "aaaacccc",
    "bbbbcccc",
    "aaabcccc",
])
def test_accepts(data):
    assert dtm.accepts_input(data)

@pytest.mark.parametrize("data", [
    "",
    "a",
    "b",
    "c",
    "ab",
    "ba",
    "abc",
    "aac",
    "bcc",
    "bbc",
    "aaccc",
    "bbccc",
    "aabcc",
    "aaacccc",
    "bbbcccc",
    "aaabccc",
    "aabbccc",
    "abbbccc",
    "aaabbcccc",
])
def test_rejects(data):
    assert not dtm.accepts_input(data)
