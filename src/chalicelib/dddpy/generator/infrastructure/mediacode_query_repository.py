
from chalicelib.dddpy.generator.domain.mediacode_repository import MediacodeRepository

import requests
import urllib.parse

from chalicelib.dddpy.generator.usecase.mediacode_schema import MediacodeSchema

import logging
import os

class MediacodeQueryRepositoryImpl(MediacodeRepository):
    """
    This class represents the implementation of the MediacodeQueryRepository interface.
    It provides methods to retrieve media codes from an external API.
    """

    def get_mediacode(self, mediacode: MediacodeSchema):
        """
        Retrieves the media code from the external API based on the provided MediacodeSchema.

        Args:
            mediacode (MediacodeSchema): The MediacodeSchema object containing the media code information.

        Returns:
            dict: The retrieved media code data as a dictionary.
        """
        api_mdc = os.environ.get("MEDIACODE_API_URL")
        url_mdc = f'{api_mdc}?{urllib.parse.urlencode(mediacode.dict())}'

        response = requests.get(url_mdc)
        data_mediacode = response.json()

        return data_mediacode
    
    