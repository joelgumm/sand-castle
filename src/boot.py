# Import the main module to start your application
import main


# boot.py

selected_app = 'moisture_indicator'

try:
    # Import the selected controller
    app_module = __import__('apps.' + selected_app, None, None, [selected_app])

except ImportError:
    print(f"App '{selected_app}' not found.")
    app_module = None


# Call the main function to execute the controller
main.main(app_module)
