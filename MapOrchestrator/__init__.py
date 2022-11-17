# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df
import os

def orchestrator_function(context: df.DurableOrchestrationContext):
    
    

    listFiles = [f for f in os.listdir(rootDirectory) if os.path.isfile(os.path.join(rootDirectory, f))]

    mapTask = []
    for file in listFiles:
        with open(file, 'r') as f:
            i=0
            for line in f:
                i+=1
                for word in line.split(" "):
                    mapTask.append(context.call_activity("Mapper", f"{i}_{word}"))
    mapOuts=context.task_all(mapTask)
    shufflerTask=[]

    for mapOut in mapOuts:
        shufflerTask.append(context.call_activity("Shuffler", mapOut))

    shufflerOuts=context.task_all(shufflerTask)
    reducerTask=[]

    for shufflerOut in shufflerOut:
        reducerTask.append(context.call_activity("Reducer", shufflerOut))

    finalResults=context.task_all(reducerTask)
    
    return finalResults

main = df.Orchestrator.create(orchestrator_function)