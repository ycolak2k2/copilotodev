# Mystery Module

This module provides a function to solve quadratic equations of the form: 
ax^2 + bx + c = 0

## Function

### `fn_x(a, b, c)`

Calculates the real roots of a quadratic equation.

**Parameters:**
- `a` (float): Coefficient of x²
- `b` (float): Coefficient of x
- `c` (float): Constant term

**Returns:**
- Tuple `(root1, root2)` if real roots exist
- `None` if the equation has no real roots

**Example Usage:**
```python
from mystery_module import fn_x

roots = fn_x(1, -3, 2)  # Solves x² - 3x + 2 = 0
print(roots)  # Output: (2.0, 1.0)

Notes:

Only real roots are returned.
If discriminant (b² - 4ac) < 0, function returns None.
This module is part of the CENG302 Copilot project.