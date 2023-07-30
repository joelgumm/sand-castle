# main.py
import sys


def main(app_module):
    if app_module:
        print(app_module)
        print(dir(sys.modules[__name__]))
        # Run the controller
        app_module.run()


if __name__ == "__main__":
    # If you need to execute main.py directly during development/testing
    # without using boot.py, you can still call main() here.
    main()
