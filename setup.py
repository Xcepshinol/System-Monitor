# setup.py
from setuptools import setup

setup(
    name="hopmon",
    version="0.1.0",
    py_modules=["systemMonitor"],
    install_requires=["psutil", "keyboard"],
    entry_points={
        "console_scripts": [
            "hopmon = systemMonitor:main",
        ],
    },
    author="Davis Yew",
    description="Real-time terminal system monitor with optional bunny splash",
)
