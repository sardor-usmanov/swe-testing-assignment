from dataclasses import dataclass
from src.calculator import Calculator, DivisionByZeroError


@dataclass
class QuickCalcApp:
    calc: Calculator
    display: str = "0"

    def clear(self) -> None:
        self.display = "0"

    def compute(self, a: float, op: str, b: float) -> str:
        try:
            if op == "+":
                result = self.calc.add(a, b)
            elif op == "-":
                result = self.calc.subtract(a, b)
            elif op == "*":
                result = self.calc.multiply(a, b)
            elif op == "/":
                result = self.calc.divide(a, b)
            else:
                self.display = "Error: Unknown operation"
                return self.display

            # 8.0 ni 8 ko‘rinishda chiqarish
            self.display = str(int(result)) if float(result).is_integer() else str(result)
            return self.display

        except DivisionByZeroError:
            self.display = "Error: Division by zero"
            return self.display


def main():
    import sys

    app = QuickCalcApp(calc=Calculator())

    if len(sys.argv) == 2 and sys.argv[1].lower() == "clear":
        app.clear()
        print(app.display)
        return

    if len(sys.argv) != 4:
        print("Usage: python -m src.app <a> <op> <b> OR python -m src.app clear")
        return

    a = float(sys.argv[1])
    op = sys.argv[2]
    b = float(sys.argv[3])

    print(app.compute(a, op, b))


if __name__ == "__main__":
    main()