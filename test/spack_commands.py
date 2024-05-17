import os
import subprocess
import time
from pathlib import Path

repo_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def time_format(seconds) -> str:
    "Returns a string formatted as 'XXh YYm ZZ.ZZs'."

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    parts = []
    if h:
        parts.append(f"{h:.0f}h")
    if m:
        parts.append(f"{m:.0f}m")
    if s:
        parts.append(f"{s:.2f}s")
    return " ".join(parts)


def log_file(command: str) -> str:
    # Filter out flags
    # and join by underscore, because spaces cause problems in bash.
    command = "_".join([x for x in command.split() if not x.startswith("-")])

    # Remove % because they cause problems in web browsers
    command = command.replace("%", "")

    return Path(repo_dir) / "log" / (command + ".log")


def run_with_spack(command: str, log: str) -> None:
    with log.open("a") as f:
        f.write(command)
        f.write("\n\n")

    start = time.time()
    sysconf = os.environ["SPACK_SYSTEM_CONFIG_PATH"]
    ret = subprocess.run(
        f". {repo_dir}/setup-env.sh {sysconf}; {command} >> {log} 2>&1",
        check=False,
        shell=True,
    )
    end = time.time()

    # Log time and success
    with log.open("a") as f:
        f.write("\n\n")
        f.write(time_format(end - start))
        f.write("\n")
        f.write("OK" if ret.returncode == 0 else "FAILED")
        f.write("\n")

    ret.check_returncode()


def spack_info(spec: str):
    log = log_file(f"info {spec}")
    log.parent.mkdir(exist_ok=True, parents=True)

    run_with_spack(f"spack info {spec}", log)


def spack_spec(spec: str):
    log = log_file(f"spec {spec}")
    log.parent.mkdir(exist_ok=True, parents=True)

    run_with_spack(f"spack spec {spec}", log)


def spack_install(spec: str, test_root: bool = True):
    log = log_file(f"install {spec}")
    log.parent.mkdir(exist_ok=True, parents=True)

    # A spec at the top of a log helps debugging.
    run_with_spack(f"spack spec {spec}", log)

    test_arg = "--test=root" if test_root else ""
    run_with_spack(f"spack install --no-checksum --verbose {test_arg} {spec}")
