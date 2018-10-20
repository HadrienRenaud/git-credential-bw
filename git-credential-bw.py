#!/usr/bin/python3.7

import os
import subprocess

if __name__ == '__main__':
    if "BW_SESSION" not in os.environ or len(os.environ["BW_SESSION"]) == 0:
        raise EnvironmentError("Missiong variable : BW_SESSION. Please unlock your bw session before and export result as BW_SESSION.")

    lines = []

    last_line = "a"
    while len(last_line) != 0:
        last_line = input()
        lines.append(last_line)

    input_data = dict(l.split("=") for l in lines if len(l) > 0)  # type: Dict[str, str]

    if "host" not in input_data:
        raise KeyError("host should be in it")

    username = subprocess.run(
        ["bw", "get", "username", input_data["host"]],
        capture_output=True).stdout.decode().replace('\n', '')
    password = subprocess.run(
        ["bw", "get", "password", input_data["host"]],
        capture_output=True).stdout.decode().replace('\n', '')

    lines.append(f"username={username}")
    lines.append(f"password={password}")

    for l in lines:
        if len(l) > 0:
            print(l)
