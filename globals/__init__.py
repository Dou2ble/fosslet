from os import name as os_name

STUDY_TYPES = [
    "write",
    "listen",
    "listen slow"
]

YES_NO = [
    "yes",
    "no"
]

if os_name == "nt":
    CLEAR = "clr"
else:
    CLEAR = "clear"
