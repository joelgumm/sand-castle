# main.py

def main(controller_module):
    if controller_module:
        # Run the controller
        controller_module.run()


if __name__ == "__main__":
    # If you need to execute main.py directly during development/testing
    # without using boot.py, you can still call main() here.
    main()
