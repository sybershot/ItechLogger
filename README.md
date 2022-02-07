# ItechLogger
Simple logger using Singleton pattern.
This project was written using Python 3.9.3.

## Main features
Three types of logging:
- INFO level is used to log call of a function. Logs function's name and returned value.
- WARN level is used to log a function, which returned `None`. Logs function's name.
- ERROR level is used to log exceptions during runtime. Logs function's name and caught exception.

Creation of a logfile of the last session in `/logs` directory.

Log is duplicated in console during runtime.

# Usage
Launch is done by loading `tests.py` from `/tests` folder to an interpreter.
