import pytest
import iguales

@pytest.mark.parametrize("w", [
"a#a",
"aa#aa",
"aaa#aaa",
"aaaa#aaaa"
])
def test_acepta(w):
    assert iguales.evaluar(w)

@pytest.mark.parametrize("w", [
"aa#",
"#aa",
"a#aaaa",
"aaa#a",
"hola"
])
def test_rechaza(w):
    assert not iguales.evaluar(w)