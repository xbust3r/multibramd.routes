import pytest

from chalicelib.dddpy.fields_types.usecase.fields_types_usecase import FieldTypeUsecase
from chalicelib.dddpy.fields_types.usecase.fields_types_cmd_schema import CreateFieldTypeSchema

from marshmallow.exceptions import ValidationError

def test_create_ok():
    field_type=FieldTypeUsecase()
    new_field_type=field_type.create(CreateFieldTypeSchema(field_type="test", length=10, description="test"))