"""
Constants to be used in various parts of the application.
"""

# Misc. Variables
# Author(s): Chanteria Milner, Michael Plunkett
FILTERED_CHARACTERS_REGEX = r'[!.,\'"?:<>]'
TYPE_DEFAULTS = {"str": None, "bool": False, "int": 0, "float": 0.0}
STANDARD_ENCODING = "utf-8"

# File Names
# Author(s): Michael Plunkett
BASE_DATA_DIR = "data/"
FILE_NAME_STATE_NAMES = BASE_DATA_DIR + "states.txt"
FILE_NAME_STATE_ABBREVIATIONS = BASE_DATA_DIR + "state_abbreviations.csv"
FILE_NAME_ABORTION_POLICY_API_GESTATION = (
    BASE_DATA_DIR + "abortion_policy_api_gestational.json"
)
FILE_NAME_ABORTION_POLICY_API_INSURANCE = (
    BASE_DATA_DIR + "abortion_policy_api_insurance.json"
)
FILE_NAME_ABORTION_POLICY_API_MINORS = (
    BASE_DATA_DIR + "abortion_policy_api_minors.json"
)
FILE_NAME_ABORTION_POLICY_API_WAITING_PERIOD = (
    BASE_DATA_DIR + "abortion_policy_api_waiting.json"
)
FILE_NAME_ANSIRH_CLEAN_DATA = BASE_DATA_DIR + "clean_ansirh.json"

FILE_NAME_STATE_ABBREVIATIONS = BASE_DATA_DIR + "state_abbreviations.csv"

# API Variables
# Author(s): Michael Plunkett
REQUEST_TIMEOUT = 10
