from chalice import Blueprint, Chalice, Response
from pydantic import ValidationError

#from chalicelib.dddpy.brands.usecase.brands_cmd_schema import CreateBrandSchema, UpdateBrandSchema
#from chalicelib.dddpy.brands.usecase.brands_usecase import BrandUsecase

from chalicelib.dddpy.routings_singles.usecase.routings_singles_cmd_schema import CreateSingleRoutingSchema, UpdateSingleRoutingSchema
from chalicelib.dddpy.routings_singles.usecase.routings_singles_usecase import RoutingSingleUsecase

from chalicelib.dddpy.shared.schemas.response_schema import ResponseErrorSchema

from chalice import Response



PREFIX="/single-routing"

single_routing = Blueprint(__name__)

@single_routing.route(f'{PREFIX}/status', methods=['GET'])
def home():
    return {"message": "Hello brand configuration!"}

@single_routing.route(f'{PREFIX}/create', methods=['POST'])
def create():
    request=single_routing.current_request
    #return request.json_body
    try:
        data=CreateSingleRoutingSchema.parse_obj(request.json_body)
        #print(data)
        response=RoutingSingleUsecase().create(data)

        return response.dict()
    
        
    except ValidationError as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)

@single_routing.route(f'{PREFIX}/find-by-id/{{id}}', methods=['GET'])
def find_by_id(id):
    try:
        response=RoutingSingleUsecase().find_by_id(id)
        return response.dict()
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)