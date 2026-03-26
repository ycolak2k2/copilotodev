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






"""
Yapılan iyileştirmeler:

✅ Type hints eklendi (daha güvenli kod)
✅ Fonksiyonlar ayrıştırıldı (tek sorumluluk prensibi)
✅ Docstring'ler eklendi
✅ Logging modülü kullanıldı (dosya yazısı daha profesyonel)
✅ Değişken adları açıklayıcı hale getirildi
✅ Yapılandırma merkezileştirildi
✅ Yorum satırları düzenli olarak yerleştirildi


"""