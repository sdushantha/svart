#!/usr/bin/env python3
#
# by Siddharth Dushantha
#
import subprocess
import sys
import argparse
import signal
from time import sleep
import als

__version__ = "1.0.0"


def run_command(command: str) -> str:
    """
    Runs a given command using subprocess module
    """
    output, _ = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True).communicate()
    return output.decode("utf-8").rstrip("\r\n")


def set_mode_to(value: str) -> None:
    """
    Set the mode to dark or light mode
    """
    if value == "dark":
        set_darkmode_to = True
    else:
        set_darkmode_to = False
    run_command(f"osascript -e 'tell application \"System Events\" to tell appearance preferences to set dark mode to {set_darkmode_to}'")


def get_current_mode() -> str:
    """
    Get current mode that is set on the system
    """
    current_mode = run_command("defaults read -g AppleInterfaceStyle")

    if current_mode == "Dark":
        return "dark"

    return "light"


def debug_print(text: str, **kwargs) -> None:
    """
    Print debugging information only when verbose mode is set
    """
    if verbose:
        # Erase current line and move the cursor to the start of the line
        print("\033[2K", end="\r", flush=True)
        print(text, **kwargs)


def exit_gracefully(signum: int, frame) -> None:
    """
    Clean exit when user does CTRL-C
    """
    print("\rGot interrupted by CTRL-C")
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(usage="%(prog)s [options]")
    parser.add_argument("ambient",
                        nargs="?",
                        default="1,100,000",
                        help="Dark mode when ambient light reaches this level (default: 1,100,000) (commas are not needed)")

    parser.add_argument("--verbose", "-v", "--debug", "-d",
                        action="store_true",
                        help="Show some information that might be useful during debugging")

    parser.add_argument("--timeout", "-t",
                        default=0,
                        help="Seconds between each check of the ambient level (default: 0)")

    parser.add_argument("--version",
                        action="store_true",
                        help="Show version number")

    args = parser.parse_args()

    global verbose
    verbose = args.verbose
    timeout = int(args.timeout)
    ambient_level_for_darkmode = int(args.ambient.replace(",", ""))

    signal.signal(signal.SIGINT, exit_gracefully)

    if args.version:
        print(__version__)
        sys.exit()

    if sys.platform != "darwin":
        print("Sorry buddy, this program only works on macOS")
        sys.exit(1)

    print("svart is now running...")

    # The commas were added to the string for better legibility
    current_mode = get_current_mode()
    debug_print(f"System mode at start: {current_mode}")

    while True:
        current_ambient_level = als.getSensorReadings()[0]

        if current_ambient_level <= ambient_level_for_darkmode:
            if current_mode != "dark":
                debug_print("Setting mode to dark")
                set_mode_to("dark")
                current_mode = "dark"
        else:
            if current_mode != "light":
                debug_print("Setting mode to light")
                set_mode_to("light")
                current_mode = "light"

        debug_print(f"Ambience level: {current_ambient_level}", end="\r")
        # Since this is running in a while loop, it is very CPU intensive, but
        # it has not caused my Macbook Air to become slow, so I prefer to keep
        # the timeout to 0s has the changing of the mode is more immediate.
        # Use --timeout and alter the seconds for sleeping to your liking.
        sleep(timeout)


if __name__ == "__main__":
    main()

