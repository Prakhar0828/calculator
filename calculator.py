"""
Simple Calculator Module

This module provides basic arithmetic operations including addition, subtraction,
multiplication, division, and other mathematical functions.
"""


def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a (float): First number to add
        b (float): Second number to add
        
    Returns:
        float: Sum of the two numbers
        
    Examples:
        >>> add_numbers(5, 3)
        8.0
        >>> add_numbers(2.5, 1.5)
        4.0
    """
    return first_num + second_num


def subtract_numbers(a: float, b: float) -> float:
    """
    Subtract the second number from the first number.
    
    Args:
        a (float): Number to subtract from
        b (float): Number to subtract
        
    Returns:
        float: Difference between the two numbers
        
    Examples:
        >>> subtract_numbers(10, 4)
        6.0
        >>> subtract_numbers(5.5, 2.3)
        3.2
    """
    return a - b


def multiply_numbers(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    
    Args:
        a (float): First number to multiply
        b (float): Second number to multiply
        
    Returns:
        float: Product of the two numbers
        
    Examples:
        >>> multiply_numbers(6, 7)
        42.0
        >>> multiply_numbers(2.5, 4)
        10.0
    """
    return a * b


def divide_numbers(a: float, b: float) -> float:
    """
    Divide the first number by the second number.
    
    Args:
        a (float): Number to be divided (dividend)
        b (float): Number to divide by (divisor)
        
    Returns:
        float: Quotient of the division
        
    Raises:
        ZeroDivisionError: If the divisor (b) is zero
        
    Examples:
        >>> divide_numbers(15, 3)
        5.0
        >>> divide_numbers(10, 4)
        2.5
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power_numbers(base: float, exponent: float) -> float:
    """
    Raise a number to the power of another number.
    
    Args:
        base (float): The base number
        exponent (float): The exponent to raise the base to
        
    Returns:
        float: The result of base raised to the exponent
        
    Examples:
        >>> power_numbers(2, 3)
        8.0
        >>> power_numbers(5, 2)
        25.0
    """
    return base ** exponent


def square_root(number: float) -> float:
    """
    Calculate the square root of a number.
    
    Args:
        number (float): The number to find the square root of
        
    Returns:
        float: The square root of the input number
        
    Raises:
        ValueError: If the input number is negative
        
    Examples:
        >>> square_root(16)
        4.0
        >>> square_root(2)
        1.4142135623730951
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return number ** 0.5


def modulo_numbers(a: float, b: float) -> float:
    """
    Calculate the remainder when dividing the first number by the second.
    
    Args:
        a (float): The dividend
        b (float): The divisor
        
    Returns:
        float: The remainder of the division
        
    Raises:
        ZeroDivisionError: If the divisor (b) is zero
        
    Examples:
        >>> modulo_numbers(17, 5)
        2.0
        >>> modulo_numbers(10, 3)
        1.0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulo with zero divisor")
    return a % b


def absolute_value(num: float) -> float:
    """
    Calculate the absolute value of a number.
    
    Args:
        number (float): The number to find the absolute value of
        
    Returns:
        float: The absolute value of the input number
        
    Examples:
        >>> absolute_value(-5)
        5.0
        >>> absolute_value(3.14)
        3.14
    """
    return abs(num)


def calculate_percentage(part: float, whole: float) -> float:
    """
    Calculate what percentage one number is of another.
    
    Args:
        part (float): The part of the whole
        whole (float): The total/whole amount
        
    Returns:
        float: The percentage as a decimal (multiply by 100 for percentage)
        
    Raises:
        ZeroDivisionError: If the whole amount is zero
        
    Examples:
        >>> calculate_percentage(25, 100)
        0.25
        >>> calculate_percentage(75, 150)
        0.5
    """
    if whole == 0:
        raise ZeroDivisionError("Cannot calculate percentage with zero whole amount")
    return part / whole


def main():
    """
    Main function to demonstrate calculator functionality.
    
    This function provides an interactive interface to test all calculator functions.
    """
    print("Simple Calculator Demo")
    print("=" * 30)
    
    # Test basic operations
    print(f"Addition: 5 + 3 = {add_numbers(5, 3)}")
    print(f"Subtraction: 10 - 4 = {subtract_numbers(10, 4)}")
    print(f"Multiplication: 6 × 7 = {multiply_numbers(6, 7)}")
    print(f"Division: 15 ÷ 3 = {divide_numbers(15, 3)}")
    print(f"Power: 2³ = {power_numbers(2, 3)}")
    print(f"Square Root: √16 = {square_root(16)}")
    print(f"Modulo: 17 % 5 = {modulo_numbers(17, 5)}")
    print(f"Absolute Value: |-5| = {absolute_value(-5)}")
    print(f"Percentage: 25/100 = {calculate_percentage(25, 100):.2%}")


if __name__ == "__main__":
    main() 
