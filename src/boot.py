# Import the main module to start your application
from main import main

# boot.py

selected_controller = 'dot_matrix.scrolling_text'

try:
    # Import the selected controller
    controller_module = __import__('controllers.' + selected_controller, None, None, [selected_controller])
except ImportError:
    print(f"Controller '{selected_controller}' not found.")
    controller_module = None


# Call the main function to execute the controller
main(controller_module)
