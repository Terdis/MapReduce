# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from typing import List, Tuple, Dict
from collections import defaultdict

def main(keyVal: List[Tuple[str, int]]) -> Dict[str, int]:

    result=(keyVal[0], sum(keyVal[1]))
    return result
