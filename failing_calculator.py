
"""
def average_ratios(numbers):
    total = 0
    for i in range(len(numbers)):
        # BUG: Crashes on zero
        total += 100 / numbers[i] 
    return total / len(numbers)

print(average_ratios([10, 5, 0]))
"""

"""Data processing module with logging functionality."""

import logging
from typing import List

# Configure logging
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(message)s"
)


def apply_multiplier(value: float, multiplier: float = 1.15) -> float:
    """
    Apply multiplier to a single value.
    
    Args:
        value: Input numeric value
        multiplier: Multiplier factor (default: 1.15)
    
    Returns:
        The multiplied value
    """
    return value * multiplier


def format_result(value: float) -> str:
    """
    Format result as string with two decimal places.
    
    Args:
        value: Numeric value to format
    
    Returns:
        Formatted string
    """
    return f"Total: {value:.2f}"


def process_data(data: List[float]) -> List[float]:
    """
    Process data by applying multiplier and logging results.
    
    Args:
        data: List of numeric values to process
    
    Returns:
        List of processed values
    """
    results = []
    
    for value in data:
        processed_value = apply_multiplier(value)
        formatted_output = format_result(processed_value)
        
        print(formatted_output)
        logging.info(formatted_output)
        results.append(processed_value)
    
    return results





""" TEST İÇİN:
def average_ratios(numbers):
    '''
    Calculate average of ratios (100 / number) for each number.
    Args:
        numbers: List of numeric values (must not contain zero)
    Returns:
        Average of ratios
    Raises:
        ValueError: If list is empty or contains zero
    '''
    if not numbers:
        raise ValueError("List cannot be empty")
    
    if 0 in numbers:
        raise ValueError("List cannot contain zero (division by zero)")
    
    total = 0
    for i in range(len(numbers)):
        total += 100 / numbers[i]
    
    return total / len(numbers)
"""