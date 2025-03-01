import hypothesis
import hypothesis.strategies as st
import pytest
import warnings

import os
import subprocess


# See the following link for Isaac Orbit environment
# https://isaac-orbit.github.io/orbit/source/setup/installation.html
PYTHON_ENVIRONMENT = "orbit -p"

EXAMPLE_DIR = "isaacorbit"
SCRIPTS = ["ppo_cartpole.py"]
EXAMPLES_DIR = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "source", "examples")
)
COMMANDS = [
    f"{PYTHON_ENVIRONMENT} {os.path.join(EXAMPLES_DIR, EXAMPLE_DIR, script)} --headless --num_envs 64"
    for script in SCRIPTS
]


@pytest.mark.parametrize("command", COMMANDS)
def test_scripts(capsys, command):
    try:
        from omni.isaac.kit import SimulationApp
    except ImportError as e:
        warnings.warn(f"\n\nUnable to import omni.isaac.kit ({e}).\nThis test will be skipped\n")
        return

    subprocess.run(command, shell=True, check=True)
