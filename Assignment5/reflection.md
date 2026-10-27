# Assignment 5 Reflection

The main challenge in temperature conversion is separating input, validation,
and output without losing track of the selected unit. The program's functions
handle these tasks separately. The unit is passed as a parameter, and the input
functions return validated values to `main()`. Global constants store the two
absolute-zero limits. Temperatures equal to absolute zero are accepted; values
below it are rejected. Conversion results display two decimal places.

The geometry program needs to repeat its menu while keeping each drawing task
separate. Named constants identify the choices, and `main()` calls the requested
drawing function with coordinates, a size, and a color. Positioning the circle
at `y - radius` makes the supplied coordinates its center. Resetting the heading
keeps each new shape oriented correctly after previous drawings.

Techniques applied from Chapter 5:

- Top-down design with a short `main()` and single-purpose helper functions.
- Void functions for displaying output and drawing shapes.
- Value-returning functions for validated input.
- Parameters, positional arguments, local variables, and a default argument.
- Global constants instead of changeable global variables.
- Standard-library imports and turtle drawing functions.
- A menu-driven application with decisions and repetition.
- The `if __name__ == "__main__":` guard.

The assignment also specifically requests the walrus operator (`:=`). Both
programs use it to receive input while testing a loop condition.

Small additions beyond the lecture examples are `try`/`except` for invalid
numeric input and invalid turtle colors, `strip()` for surrounding whitespace,
and `math.isfinite()` to reject infinity and NaN. These prevent invalid input
from crashing the program or reaching the drawing calculations. No classes,
third-party packages, or advanced application structure are used.
