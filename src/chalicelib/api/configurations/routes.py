from chalice import Blueprint, Chalice, Response
from pydantic import ValidationError

#from chalicelib.dddpy.brands.usecase.brands_cmd_schema import CreateBrandSchema, UpdateBrandSchema
#from chalicelib.dddpy.brands.usecase.brands_usecase import BrandUsecase

from chalicelib.dddpy.configurations.usecase.configurations_cmd_schema import CreateConfigurationSchema, UpdateConfigurationSchema
from chalicelib.dddpy.configurations.usecase.configurations_query_schema import CheckDuplicatedConfigurationSchema, FindConfigurationSchema

from chalicelib.dddpy.configurations.usecase.configurations_usecase import ConfigurationUsecase

from chalicelib.dddpy.shared.schemas.response_schema import ResponseErrorSchema

from chalice import Response



PREFIX="/brand-configuration"

atalaya_conf = Blueprint(__name__)

@atalaya_conf.route(f'{PREFIX}/status', methods=['GET'])
def home():
    return {"message": "Hello brand configuration!"}

@atalaya_conf.route(f'{PREFIX}/all', methods=['GET'])
def all():
    try:
        response=ConfigurationUsecase().all()
        return response
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)

@atalaya_conf.route(f'{PREFIX}/check-duplicated', methods=['POST'])
def check_duplicated():
    request=atalaya_conf.current_request
    try:
        data=CreateConfigurationSchema.parse_obj(request.json_body)
        response=ConfigurationUsecase().check_duplicated(data)
        return response.dict()
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)

@atalaya_conf.route(f'{PREFIX}/find', methods=['POST'])
def find_configuration():
    request=atalaya_conf.current_request
    try:
        
        data=FindConfigurationSchema.parse_obj(request.json_body)
        response=ConfigurationUsecase().find_configuration(data)
        return response.dict()
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500 )


@atalaya_conf.route(f'{PREFIX}/create', methods=['POST'])
def create():
    request=atalaya_conf.current_request
    #return request.json_body
    try:
        data=CreateConfigurationSchema.parse_obj(request.json_body)
        #print(data)
        response=ConfigurationUsecase().create(data)

        return response.dict()
    
        
    except ValidationError as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)