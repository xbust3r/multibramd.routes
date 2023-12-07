
from chalicelib.dddpy.generator.domain.mediacode_repository import MediacodeRepository
from chalicelib.dddpy.generator.usecase.mediacode_schema import (
    MediacodeSchema,
    UrlReplaceSchema,
)


class MediacodeQueryUsecase:
    """
    This class represents a use case for querying mediacodes and generating redirect URLs.
    """

    def __init__(self, mediacode_repository: MediacodeRepository):
        """
        Initializes a new instance of the MediacodeQueryUsecase class.

        Args:
            mediacode_repository (MediacodeRepository): The repository for mediacodes.
        """
        self.mediacode_repository = mediacode_repository

    def get_mediacode(self, mediacode: str):
        """
        Retrieves a mediacode from the repository.

        Args:
            mediacode (str): The mediacode to retrieve.

        Returns:
            The retrieved mediacode.
        """
        return self.mediacode_repository.get_mediacode(mediacode)

    def get_redirect_url(self, replace: UrlReplaceSchema):
        """
        Generates a redirect URL based on the provided replacement data.

        Args:
            replace (UrlReplaceSchema): The replacement data for generating the URL.

        Returns:
            The generated redirect URL.
        """
        if replace.system == "rater":
            url = f"{replace.url}?media_code={replace.mediacode}&phone={replace.phone}&zip_code={replace.zip_code}&city={replace.city}&state={replace.state}&system=atalaya"
        elif replace.system == "webform":
            url = f"{replace.url}?media_code={replace.mediacode}&phone={replace.phone}&zipcode={replace.zip_code}&city={replace.city}&state={replace.state}&system=atalaya"
        elif replace.system == "nsd":
            url = f"{replace.url}?media_code={replace.mediacode}&phone={replace.phone}&zip_code={replace.zip_code}&city={replace.city}&state={replace.state}&system=atalaya"
        else:
            url = f"{replace.url}"

        return url
