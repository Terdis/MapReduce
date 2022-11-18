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
    
    

    inputBlob = yield context.call_activity('GetInputDataFn', 'filesinput')

    mapTask = []
    for pair in inputBlob:
        mapTask.append(context.call_activity('Mapper', pair))

    mapOuts=yield context.task_all(mapTask)
    
    mapOuts=sum(mapOuts, [])

    shufflerOuts = yield context.call_activity("Shuffler", mapOuts)
    reducerTask=[]

    for shufflerOut in shufflerOuts:
        reducerTask.append(context.call_activity("Reducer", shufflerOut))

    finalResults=yield context.task_all(reducerTask)
    
    return finalResults

main = df.Orchestrator.create(orchestrator_function)