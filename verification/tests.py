"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ["127.0.0.1"],
            "answer": 2130706433,
        },
        {
            "input": ["192.168.0.1"],
            "answer": 3232235521,
        }
    ],
    "Extra": [
        {
            "input": ["0.0.0.0"],
            "answer": 0,
        },
        {
            "input": ["255.255.255.255"],
            "answer": 4294967295,
        }
    ]
}
