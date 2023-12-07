
"""
This module provides factories for creating instances of BrandCmdUsecase and BrandQueryUsecase.

The factories create instances of the use cases by initializing the required repositories.

Functions:
- brand_cmd_usecase_factory: Creates an instance of BrandCmdUsecase with BrandCmdRepositoryImpl.
- brand_query_usecase_factory: Creates an instance of BrandQueryUsecase with BrandQueryRepositoryImpl.
"""

from chalicelib.dddpy.brands.usecase.brands_cmd_usecase import BrandCmdUsecase
from chalicelib.dddpy.brands.infrastructure.brands_cmd_repository import BrandCmdRepositoryImpl
from chalicelib.dddpy.brands.usecase.brands_query_usecase import BrandQueryUsecase
from chalicelib.dddpy.brands.infrastructure.brands_query_repository import BrandQueryRepositoryImpl

def brand_cmd_usecase_factory():
    """
    Creates an instance of BrandCmdUsecase with BrandCmdRepositoryImpl.

    Returns:
    BrandCmdUsecase: An instance of BrandCmdUsecase.
    """
    brand_cmd_repository = BrandCmdRepositoryImpl()
    return BrandCmdUsecase(brand_cmd_repository)

def brand_query_usecase_factory():
    """
    Creates an instance of BrandQueryUsecase with BrandQueryRepositoryImpl.

    Returns:
    BrandQueryUsecase: An instance of BrandQueryUsecase.
    """
    brand_query_repository = BrandQueryRepositoryImpl()
    return BrandQueryUsecase(brand_query_repository)


