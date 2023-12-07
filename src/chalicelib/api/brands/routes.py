from chalice import Blueprint, Chalice, Response
from pydantic import ValidationError
from chalice import Response

from chalicelib.dddpy.shared.schemas.response_schema import ResponseErrorSchema


from chalicelib.dddpy.brands.usecase.brands_cmd_schema import CreateBrandSchema, UpdateBrandSchema
from chalicelib.dddpy.brands.usecase.brands_usecase import BrandUsecase







PREFIX="/brands"

atalaya_brands = Blueprint(__name__)

@atalaya_brands.route(f'{PREFIX}/status', methods=['GET'])
def home():
    return {"message": "Hello fields types!"}

@atalaya_brands.route(f'{PREFIX}/find_by_code/{{code}}', methods=['GET'])
def find_by_code(code: str):
    try:
        response=BrandUsecase().find_by_code(code)
        return response.dict()
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)

@atalaya_brands.route(f'{PREFIX}/create', methods=['POST'])
def create():
    request=atalaya_brands.current_request
    #return request.json_body
    try:
        data=CreateBrandSchema.parse_obj(request.json_body)
        
        response=BrandUsecase().create(data)
        print(type(response))
        return response.dict()
    
        
    except ValidationError as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)
    except Exception as e:
        error_response = ResponseErrorSchema(success=False, message=str(e))
        return Response(body=error_response.dict(), status_code=500)