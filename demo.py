import logging
import math

logging.basicConfig(
    filename="quadratic.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)


def solve_quadratic(a, b, c):
    logging.info(f"Start solving: {a}x^2 + {b}x + {c} = 0")

    for param, val in zip(["a", "b", "c"], [a, b, c]):
        if not isinstance(val, (int, float)):
            logging.critical(f"Bad type for '{param}': {type(val)}")
            raise TypeError(f"Coefficient {param} must be int or float")

    if a == 0:
        logging.error("a equals zero - not a quadratic equation")
        raise ValueError("Parameter a cannot be zero")

    discriminant = b ** 2 - 4 * a * c
    logging.debug(f"D = {discriminant}")

    if discriminant < 0:
        logging.warning("No real roots (D < 0)")
        return None

    if discriminant == 0:
        root = -b / (2 * a)
        logging.info("Single root found")
        return (root,)

    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    logging.info("Two roots found")
    return x1, x2


if __name__ == "__main__":
    print("=== Тестирование solve_quadratic ===\n")

    print("Два корня:", solve_quadratic(1, -5, 6))
    print("Один корень:", solve_quadratic(1, -4, 4))
    print("Нет корней:", solve_quadratic(1, 0, 1))

    try:
        solve_quadratic(0, 2, 3)
    except ValueError as err:
        print("Ошибка a=0:", err)

    try:
        solve_quadratic("x", 1, 2)
    except TypeError as err:
        print("Ошибка типа:", err)