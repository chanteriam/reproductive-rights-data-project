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
base_data_dir = "reproductive_rights_data_project/data/"
FILE_NAME_STATE_NAMES = base_data_dir + "states.txt"
FILE_NAME_ABORTION_POLICY_API_GESTATION = (
    base_data_dir + "abortion_policy_api_gestational.json"
)
FILE_NAME_ABORTION_POLICY_API_INSURANCE = (
    base_data_dir + "abortion_policy_api_insurance.json"
)
FILE_NAME_ABORTION_POLICY_API_MINORS = (
    base_data_dir + "abortion_policy_api_minors.json"
)
FILE_NAME_ABORTION_POLICY_API_WAITING_PERIOD = (
    base_data_dir + "abortion_policy_api_waiting.json"
)
FILE_NAME_ANSIRH_CLEAN_DATA = base_data_dir + "clean_ansirh.json"

FILE_NAME_STATE_ABBREVIATIONS = base_data_dir + "state_abbreviations.csv"

# API Variables
# Author(s): Michael Plunkett
REQUEST_TIMEOUT = 10
