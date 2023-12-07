from chalice import Blueprint, Chalice, Response
from pydantic import ValidationError

#from chalicelib.dddpy.brands.usecase.brands_cmd_schema import CreateBrandSchema, UpdateBrandSchema
#from chalicelib.dddpy.brands.usecase.brands_usecase import BrandUsecase

from chalicelib.dddpy.routings_multis.usecase.routings_multis_cmd_schema import CreateRoutingMultiSchema, UpdateRoutingMultiSchema
from chalicelib.dddpy.routings_multis.usecase.routings_multis_usecase import RoutingMultiUsecase

from chalicelib.dddpy.shared.schemas.response_schema import ResponseErrorSchema

from chalice import Response




PREFIX="/multi-routing"

routing_multis = Blueprint(__name__)

@routing_multis.route(f'{PREFIX}/status', methods=['GET'])
def home():
    return {"message": "Hello multi routing configuration!"}

@routing_multis.route(f'{PREFIX}/create', methods=['POST'])
def create():
    request=routing_multis.current_request
    #return request.json_body
    try:
        data=CreateRoutingMultiSchema.parse_obj(request.json_body)
        #print(data)
        response=RoutingMultiUsecase().create(data)

        return response.dict()
        #return "ok"
    
    except ValidationError as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)