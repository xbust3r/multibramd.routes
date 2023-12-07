
from chalicelib.dddpy.generator.domain.zipcode_repository import ZipcodeRepository

class ZipcodeQueryUsecase:
    """
    This class represents a use case for querying information by zipcode.
    """

    def __init__(self, zipcode_repository: ZipcodeRepository):
        """
        Initializes a new instance of the ZipcodeQueryUsecase class.

        Args:
            zipcode_repository (ZipcodeRepository): The repository for zipcode information.
        """
        self.zipcode_repository = zipcode_repository
    
    def get_info_by_zipcode(self, code: str):
        """
        Retrieves information by zipcode.

        Args:
            code (str): The zipcode code.

        Returns:
            The information associated with the given zipcode.
        """
        return self.zipcode_repository.get_info_by_zipcode(code)