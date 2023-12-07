
from chalicelib.dddpy.generator.domain.zipcode_repository import ZipcodeRepository
import requests

import logging

import os

class ZipcodeQueryRepositoryImpl(ZipcodeRepository):
    def get_info_by_zipcode(self, code: int):
        """
        Retrieves information about a zipcode from an external API.

        Args:
            code (int): The zipcode code.

        Returns:
            dict: A dictionary containing the following information:
                - state: The state code of the zipcode.
                - city: The city name of the zipcode.
                - zip: The zipcode code.
                - address: The address associated with the zipcode.

            None: If the data retrieval fails.
        """
        api_zip = os.environ.get("ZIPCODE_API_URL")
        url = f"{api_zip}/{code}.json"
        data = requests.get(url)

        if data.status_code != 200:
            logging.error(f"Failed to retrieve data: {data.status_code}")
            return None

        json_data = data.json()
        data_field = json_data.get("data")
        if data_field is not None:
            zip_data = {
                "state": data_field.get("StateCode"),
                "city": data_field.get("City"),
                "zip": data_field.get("Zipcode"),
                "address": data_field.get("Address"),
            }

        return zip_data
