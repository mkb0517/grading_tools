#!/usr/bin/env python

github_usernames = [
    "pbbarnes",
    "muku42",
    "mkb0517",
    "achang6",
    "dchilds7",
    "tedsta",
    "nynhle",
    "klaguana",
    "brennanblue",
    "nagatak",
    "cpearring",
    "joshrobo",
    "RoyGBivDash",
    "jasminks",
    "asttra",
    "cv9828",
    "stphnzilch",
    "joshuacw",
    "shenuhcide"
]

profiles = {
    "bruab": {
        "major": "ICS",
        "boot os": "OSX",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": True,
        "astro": True,
        "game": True,
        "ninja skills": True,
        "web": True,
        "ask me about": "social network analysis"
        },
    "pbbarnes": {
        "major": "Computer Science",
        "boot os": "OSX",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": False,
        "astro": False,
        "game": True,
        "ninja skills": True,
        "web": True,
        "ask me about": "Configuration Management"
        },
    "muku42": {
        "major": "Astronomy",
        "boot os": "OSX",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": True,
        "astro": True,
        "game": True,
        "ninja skills": False,
        "web": True,
        "ask me about": "things you've used your raspberry pi for"
        },
    "mkb0517": {
        "major": "CS",
        "boot os": "Linux Mint",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": False,
        "astro": False,
        "game": True,
        "ninja skills": True,
        "web": True,
        "ask me about": "Magic: the Gathering, sciency things, py-game (in about a month), dual-booting windows and linux, anything really"
        },
    "achang6": {
        "major": "Chemistry",
        "boot os": "Ubuntu",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": False,
        "astro": False,
        "game": True,
        "ninja skills": True,
        "web": True,
        "ask me about": "General Chemistry"
        },
    "dchilds7": {
        "major": "ICS",
        "boot os": "OSX",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": True,
        "astro": True,
        "game": True,
        "ninja skills": True,
        "web": True,
        "ask me about": "social network analysis"
        },
    "tedsta": {
        "major": "CS",
        "boot os": "Ubuntu",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": False,
        "astro": False,
        "game": False,
        "ninja skills": True,
        "web": True,
        "ask me about": "social network analysis"
        },
    "nynhle": {
        "major": "IS",
        "boot os": "OSX",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": False,
        "astro": True,
        "game": True,
        "ninja skills": True,
        "web": True,
        "ask me about": "Ask me, Im a pilot."
        },
    "klaguana": {
        "major": "astronomy",
        "boot os": "OSX",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": False,
        "astro": True,
        "game": False,
        "ninja skills": True,
        "web": True,
        "ask me about": "pop punk"
        },
    "brennanblue": {
        "major": "Econ",
        "boot os": "Windows 10",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": False,
        "astro": False,
        "game": False,
        "ninja skills": True,
        "web": True,
        "ask me about": "Ending the Fed"
        },
    "nagatak": {
        "major": "CS",
        "boot os": "OSX",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": False,
        "astro": False,
        "game": False,
        "ninja skills": True,
        "web": True,
        "ask me about": "iOS app working on"
        },
    "cpearring": {
        "major": "computer science",
        "boot os": "Ubuntu",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": False,
        "astro": False,
        "game": False,
        "ninja skills": True,
        "web": True,
        "ask me about": "The geopolitical instability of the Middle East"
        },
    "joshrobo": {
        "major": "cs",
        "boot os": "windows 10",
        "virtual os": "ubuntu",
        "text editor": "Vim",
        "de-noobification": False,
        "astro": False,
        "game": True,
        "ninja skills": True,
        "web": True,
        "ask me about": "soccer"
        },
    "RoyGBivDash": {
        "major": "Astronomy and Physics",
        "boot os": "Windows",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": False,
        "astro": True,
        "game": False,
        "ninja skills": True,
        "web": False,
        "ask me about": "Do you really have a pet rabbit?"
        },
    "jasminks": {
        "major": "physics and astronomy, minor in math",
        "boot os": "OSX",
        "virtual os": None,
        "text editor": "Emacs",
        "de-noobification": False,
        "astro": True,
        "game": False,
        "ninja skills": True,
        "web": False,
        "ask me about": "Spectroscopy, cute cats and emacs"
        },
    "asttra": {
        "major": "Biology and Astronomy",
        "boot os": "ubuntu",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": True,
        "astro": True,
        "game": False,
        "ninja skills": False,
        "web": False,
        "ask me about": "How did you start working for the USDA?"
        },
    "cv9828": {
        "major": "CS",
        "boot os": "Windows 8.1",
        "virtual os": "Ubuntu",
        "text editor": "Vim",
        "de-noobification": False,
        "astro": False,
        "game": False,
        "ninja skills": True,
        "web": True,
        "ask me about": "CS student"
        },
    "stphnzilch": {
        "major": "Chemistry",
        "boot os": "Ubuntu",
        "virtual os": None,
        "text editor": "Emacs",
        "de-noobification": True,
        "astro": False,
        "game": True,
        "ninja skills": False,
        "web": False,
        "ask me about": "social network analysis"
        },
    "joshuacw": {
        "major": "ICS",
        "boot os": "OSX",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": True,
        "astro": True,
        "game": True,
        "ninja skills": True,
        "web": True,
        "ask me about": "social network analysis"
        },
    "shenuhcide": {
        "major": "ICS",
        "boot os": "OSX",
        "virtual os": None,
        "text editor": "Vim",
        "de-noobification": True,
        "astro": True,
        "game": True,
        "ninja skills": True,
        "web": True,
        "ask me about": "social network analysis"
        }
}
