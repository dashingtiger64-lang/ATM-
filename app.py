import streamlit as st


class RationalNumber:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def reduce(self):
        gcd = self.greatest_common_divisor(
            self.numerator,
            self.denominator
        )
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod
    def greatest_common_divisor(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def __eq__(self, other):
        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )

    def __add__(self, other):
        numerator = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )
        denominator = (
            self.denominator * other.denominator
        )
        return RationalNumber(numerator, denominator)

    def __sub__(self, other):
        numerator = (
            self.numerator * other.denominator
            - other.numerator * self.denominator
        )
        denominator = (
            self.denominator * other.denominator
        )
        return RationalNumber(numerator, denominator)

    def __mul__(self, other):
        numerator = (
            self.numerator * other.numerator
        )
        denominator = (
            self.denominator * other.denominator
        )
        return RationalNumber(numerator, denominator)

    def __truediv__(self, other):
        numerator = (
            self.numerator * other.denominator
        )
        denominator = (
            self.denominator * other.numerator
        )
        return RationalNumber(numerator, denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


st.set_page_config(
    page_title="Rational Number Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Rational Number Calculator")

st.subheader("First Rational Number")
num1 = st.number_input(
    "Numerator 1",
    value=1,
    step=1
)
den1 = st.number_input(
    "Denominator 1",
    value=2,
    min_value=1,
    step=1
)

st.subheader("Second Rational Number")
num2 = st.number_input(
    "Numerator 2",
    value=1,
    step=1
)
den2 = st.number_input(
    "Denominator 2",
    value=3,
    min_value=1,
    step=1
)

if st.button("Calculate"):
    r1 = RationalNumber(int(num1), int(den1))
    r2 = RationalNumber(int(num2), int(den2))

    st.success("Results")

    st.write(f"R1 = {r1}")
    st.write(f"R2 = {r2}")

    st.write(f"Addition: {r1 + r2}")
    st.write(f"Subtraction: {r1 - r2}")
    st.write(f"Multiplication: {r1 * r2}")
    st.write(f"Division: {r1 / r2}")
