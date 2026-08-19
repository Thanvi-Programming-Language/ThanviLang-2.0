import sys
from web.webapp import start_server


def main():

    if len(sys.argv) < 2:
        print("ThanviLang 2.0")
        print()
        print("Usage:")
        print("  python cli.py run")
        return

    command = sys.argv[1]

    if command == "run":
        start_server()

    elif command == "version":
        print("ThanviLang v2.0.0")

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
