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
from collections import defaultdict

def main(keyVal: Dict[str, List[int]]) -> Dict[str, int]:
    summ=0
    result=defaultdict(lambda x: 0)

    for k, v in keyVal:
        result[k]+=v
    return result
