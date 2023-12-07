from chalice import Blueprint, Chalice, Response
from pydantic import ValidationError
#import pandas as pd
import logging
import os


# from chalicelib.dddpy.brands.usecase.brands_cmd_schema import CreateBrandSchema, UpdateBrandSchema
# from chalicelib.dddpy.brands.usecase.brands_usecase import BrandUsecase

from chalicelib.dddpy.generator.usecase.generator_query_schema import GetUrlSchema
from chalicelib.dddpy.generator.usecase.generator_cmd_schema import CreateGeneatorSchema
from chalicelib.dddpy.generator.usecase.generator_usecase import GeneratorUsecase

from chalicelib.dddpy.shared.schemas.response_schema import (
    ResponseErrorSchema,
    ResponseSuccessSchema,
)

from chalice import Response


PREFIX = "/generator"

routing_generator = Blueprint(__name__)


@routing_generator.route(f"{PREFIX}/status", methods=["GET"])
def home():
    return {"message": "Hello generator configuration!"}


@routing_generator.route(f"{PREFIX}/create", methods=["POST"])
def create():
    request = routing_generator.current_request
    # return request.json_body
    try:
        data = CreateGeneatorSchema.parse_obj(request.json_body)
        # print(data)
        response = GeneratorUsecase().create(data)

        return response.dict()

    except ValidationError as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)


@routing_generator.route(f"{PREFIX}/process", methods=["POST"], cors=True)
def process():
    request = routing_generator.current_request
    try:
        data = GetUrlSchema.parse_obj(request.json_body)
        response = GeneratorUsecase().process(data)
        return response.dict()

    except ValidationError as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)

