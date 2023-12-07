'''
This file contains the implementation of the RoutingSingleQueryUsecase class, which is responsible for querying routing singles.

The class has the following methods:
- __init__(self, routing_single_repository: RoutingSingleRepository): Initializes the RoutingSingleQueryUsecase object.
- find_by_id(self, id: int): Finds a routing single by its ID.
- find_by_configuration_id(self, configuration_id: int): Finds routing singles by their configuration ID.
'''

from chalicelib.dddpy.routings_singles.domain.routings_singles_repository import RoutingSingleRepository

class RoutingSingleQueryUsecase:
    
    def __init__(self, routing_single_repository: RoutingSingleRepository) -> None:
        self.routing_single_repository = routing_single_repository
        
    def find_by_id(self, id: int):
        return self.routing_single_repository.find_by_id(id)
    
    def find_by_configuration_id(self, configuration_id: int):
        return self.routing_single_repository.find_by_configuration_id(configuration_id)