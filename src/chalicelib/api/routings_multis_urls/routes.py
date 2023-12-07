from chalice import Blueprint, Chalice, Response
from pydantic import ValidationError

#from chalicelib.dddpy.brands.usecase.brands_cmd_schema import CreateBrandSchema, UpdateBrandSchema
#from chalicelib.dddpy.brands.usecase.brands_usecase import BrandUsecase

from chalicelib.dddpy.routings_multis_urls.usecase.routings_multis_urls_cmd_schema import CreateRoutingMultiUrlSchema, UpdateRoutingMultiUrlSchema
from chalicelib.dddpy.routings_multis_urls.usecase.routings_multis_urls_usecase import RoutingMultiUrlUsecase

from chalicelib.dddpy.shared.schemas.response_schema import ResponseErrorSchema

from chalice import Response




PREFIX="/multi-routing-url"

routing_multis_urls = Blueprint(__name__)

@routing_multis_urls.route(f'{PREFIX}/status', methods=['GET'])
def home():
    return {"message": "Hello multi routing Urls configuration!"}

@routing_multis_urls.route(f'{PREFIX}/create', methods=['POST'])
def create():
    request=routing_multis_urls.current_request
    #return request.json_body
    try:
        data=CreateRoutingMultiUrlSchema.parse_obj(request.json_body)
        #print(data)
        response=RoutingMultiUrlUsecase().create(data)

        return response.dict()
        #return "ok"
    
    except ValidationError as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)
    
