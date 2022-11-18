# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from typing import List
from typing import Dict
from typing import Tuple
from collections import defaultdict

def main(keyValue: List[Tuple[str, int]]) -> List[Tuple[str, List[int]]]:

    result=defaultdict(list)
    for tup in keyValue:
        result[tup[0]].append(tup[1])
    return list(result.items())
