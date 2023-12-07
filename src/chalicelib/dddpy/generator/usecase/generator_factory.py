
from chalicelib.dddpy.generator.infrastructure.zipcode_query_repository import ZipcodeQueryRepositoryImpl
from chalicelib.dddpy.generator.usecase.zipcode_query_usecase import ZipcodeQueryUsecase

from chalicelib.dddpy.generator.infrastructure.mediacode_query_repository import MediacodeQueryRepositoryImpl
from chalicelib.dddpy.generator.usecase.mediacode_query_usecase import MediacodeQueryUsecase

def zipcode_query_usecase_factory():
    """
    Factory function that creates an instance of ZipcodeQueryUsecase.

    Returns:
        ZipcodeQueryUsecase: An instance of ZipcodeQueryUsecase.
    """
    return ZipcodeQueryUsecase(ZipcodeQueryRepositoryImpl())

def mediacode_query_usecase_factory():
    """
    Factory function that creates an instance of MediacodeQueryUsecase.

    Returns:
        MediacodeQueryUsecase: An instance of MediacodeQueryUsecase.
    """
    return MediacodeQueryUsecase(MediacodeQueryRepositoryImpl())