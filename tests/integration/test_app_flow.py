from src.app import QuickCalcApp
from src.calculator import Calculator


def test_full_user_interaction_addition():
    """
    Simulate: 5 + 3 = 8
    """
    app = QuickCalcApp(calc=Calculator())
    result = app.compute(5, "+", 3)

    assert result == "8"
    assert app.display == "8"


def test_clear_resets_display_to_zero():
    app = QuickCalcApp(calc=Calculator())

    app.compute(10, "*", 2)
    assert app.display == "20"

    app.clear()
    assert app.display == "0"