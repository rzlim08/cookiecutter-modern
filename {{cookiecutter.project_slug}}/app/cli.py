"""Console script for {{cookiecutter.project_slug}}."""
import argparse
import {{cookiecutter.project_slug}}

def main():
    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser(description="Console script for {{cookiecutter.project_slug}}.")
    
    # You can add arguments here as needed
    # parser.add_argument('some_argument', type=str, help='Description of the argument')
    
    args = parser.parse_args()

    # Main logic of the script
    print("Replace this message by putting your code into {{cookiecutter.project_slug}}.cli.main")
    print("See argparse documentation at https://docs.python.org/3/library/argparse.html")

if __name__ == "__main__":
    main()
