from chalice import Blueprint, Chalice, Response
from pydantic import ValidationError
from chalice import Response

from chalicelib.dddpy.shared.schemas.response_schema import ResponseErrorSchema

from chalicelib.dddpy.logs.usecase.logs_cmd_schema import CreateLogSchema
from chalicelib.dddpy.logs.usecase.logs_usecase import LogUsecase

import boto3
import os
import logging
import json

name_app_sqs = os.environ.get("SQS_NAME")
sqs = boto3.client("sqs", region_name=os.environ.get("SQS_REGION"))
queue_url = (
    os.environ.get("SQS_URL")
)


PREFIX="/logs"

atalaya_logs = Blueprint(__name__)

@atalaya_logs.route(f'{PREFIX}/status', methods=['GET'])
def home():
    return {"message": "Hello logs!"}

@atalaya_logs.route(f'{PREFIX}/all', methods=['GET'])
def all():
    try:
        response=LogUsecase().all()
        return response.dict()
    
    except ValidationError as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)
    
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)

@atalaya_logs.route(f'{PREFIX}/create', methods=['POST'])
def create():
    request=atalaya_logs.current_request
    #return request.json_body
    try:
        data=CreateLogSchema.parse_obj(request.json_body)
        
        response=LogUsecase().create(data)
        print(type(response))
        return response.dict()
    
    except ValidationError as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)
    
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)
    


@atalaya_logs.on_sqs_message(queue=name_app_sqs)
def sqs_save_log(event):
    try:
        for record in event:
            body = record.body
            print(body)
            data=CreateLogSchema.parse_raw(body)
            response=LogUsecase().create(data)
            print(response)
            sqs.delete_message(
                QueueUrl=queue_url,  # Reemplaza con la URL de tu cola
                ReceiptHandle=record.receipt_handle
            )
            
    except Exception as e:
        print(e)
        raise e
    return True

@atalaya_logs.route(f'{PREFIX}/read-sqs', methods=['GET'])
def read_sqs():
    messages=sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        VisibilityTimeout=30,
        WaitTimeSeconds=0
    )
    if 'Messages' in messages:
        logging.info("Messages in queue")
        for message in messages['Messages']:
            data=message['Body']
            try: 
                data=CreateLogSchema.parse_raw(data)
                response=LogUsecase().create(data)
                
            except json.JSONDecodeError as e:
                logging.info("JSONDecodeError")
                logging.info(e)
                logging.info(type(e))

                
            #response=LogUsecase().create(data)
            #logging.info(data)
            sqs.delete_message(
                QueueUrl=queue_url,  # Reemplaza con la URL de tu cola
                ReceiptHandle=message['ReceiptHandle']
            )