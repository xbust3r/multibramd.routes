
"""
This module contains the implementation of the GeneratorUsecase class, which is responsible for generating configurations and processing URLs.

Classes:
- GeneratorUsecase: Handles the creation of configurations and processing of URLs.

"""

from chalicelib.dddpy.generator.usecase.generator_cmd_schema import CreateGeneatorSchema
from chalicelib.dddpy.generator.usecase.generator_query_schema import GetUrlSchema
from chalicelib.dddpy.generator.domain.generator_exception import (
    InvalidUrlException,
    TypeNotSupportedException,
    GeneratorRoutesNotConfigured,
)

from chalicelib.dddpy.generator.usecase.generator_factory import (
    zipcode_query_usecase_factory,
    mediacode_query_usecase_factory,
)
from chalicelib.dddpy.configurations.usecase.configurations_factory import (
    configuration_query_usecase_factory,
)

from chalicelib.dddpy.configurations.usecase.configurations_usecase import (
    ConfigurationUsecase,
)
from chalicelib.dddpy.configurations.usecase.configurations_query_usecase import (
    CheckDuplicatedConfigurationSchema,
)
from chalicelib.dddpy.configurations.domain.configurations_exception import (
    ConfigurationAlreadyExistsError,
    ConfigurationsNotFoundError,
)
from chalicelib.dddpy.configurations.usecase.configurations_query_schema import (
    FindConfigurationSchema,
)

from chalicelib.dddpy.routings_singles.usecase.routings_singles_cmd_schema import (
    CreateSingleRoutingSchema,
)
from chalicelib.dddpy.routings_singles.usecase.routings_singles_usecase import (
    RoutingSingleUsecase,
)

from chalicelib.dddpy.routings_multis.usecase.routings_multis_cmd_schema import (
    CreateRoutingMultiSchema,
)
from chalicelib.dddpy.routings_multis.usecase.routings_multis_usecase import (
    RoutingMultiUsecase,
)

from chalicelib.dddpy.routings_multis_urls.usecase.routings_multis_urls_cmd_schema import (
    CreateRoutingMultiUrlSchema,
)
from chalicelib.dddpy.routings_multis_urls.usecase.routings_multis_urls_usecase import (
    RoutingMultiUrlUsecase,
)

from chalicelib.dddpy.shared.schemas.response_schema import (
    ResponseErrorSchema,
    ResponseSuccessSchema,
)

from chalicelib.dddpy.generator.usecase.mediacode_schema import MediacodeSchema, UrlReplaceSchema

from chalicelib.dddpy.shared.utils.urls import URL

from chalicelib.dddpy.brands.usecase.brands_usecase import BrandUsecase

import logging
import json

from chalicelib.dddpy.logs.usecase.logs_usecase import LogUsecase

from chalicelib.dddpy.logs.usecase.logs_cmd_schema import CreateLogSchema


class GeneratorUsecase:
    """
    The GeneratorUsecase class handles the creation of configurations and processing of URLs.

    Methods:
    - create(generator: CreateGeneatorSchema): Creates a new generator configuration.
    - process(generator: GetUrlSchema): Processes a URL and returns the appropriate response.
    """

    def __init__(self) -> None:
        self.configuration_usecase = ConfigurationUsecase()
        self.routing_single_usecase = RoutingSingleUsecase()
        self.routing_multi_usecase = RoutingMultiUsecase()
        self.routing_multi_url_usecase = RoutingMultiUrlUsecase()
        self.brand_usecase = BrandUsecase()

        self.log_usecase = LogUsecase()

        self.zipcode_query_usecase = zipcode_query_usecase_factory()
        self.configuration_query_usecase = configuration_query_usecase_factory()
        self.mediacode_query_usecase = mediacode_query_usecase_factory()

    def create(self, generator: CreateGeneatorSchema):
        """
        Creates a new generator configuration.

        Args:
        - generator: An instance of CreateGeneatorSchema containing the generator details.

        Returns:
        - An instance of ResponseSuccessSchema with the success message and data.

        Raises:
        - ConfigurationAlreadyExistsError: If a duplicate configuration is found.
        - InvalidUrlException: If an invalid URL is provided.
        - TypeNotSupportedException: If the configuration type is not supported.
        - Exception: If an error occurs during the creation process.
        """
        duplicated = self.configuration_usecase.check_duplicated(
            CheckDuplicatedConfigurationSchema(
                language=generator.language,
                insurance=generator.insurance,
                device=generator.device,
                media=generator.media,
                state=generator.state,
                type=generator.type,
                brand_id=generator.brand_id,
            )
        )

        if duplicated.data is not False:
            raise ConfigurationAlreadyExistsError

        try:
            configuration = self.configuration_usecase.create(generator)

        except Exception as e:
            raise e

        configuration_id = configuration.data["id"]
        brand_id = configuration.data["brand_id"]
        type = configuration.data["type"]
        if type == 1:
            try:
                if not URL(generator.urls[0]).is_valid():
                    raise InvalidUrlException()
                domain = URL(generator.urls[0]).domain
                create_single = CreateSingleRoutingSchema(
                    brand_id=brand_id,
                    configuration_id=configuration_id,
                    url=generator.urls[0],
                    domain=domain,
                    variables={"key": "value"},
                )
                routing_type = "single"
                self.routing_single_usecase.create(create_single)
            except Exception as e:
                raise e
        elif type == 2:
            try:
                for url in generator.urls:
                    if not URL(url).is_valid():
                        raise InvalidUrlException()

                create_multi = CreateRoutingMultiSchema(
                    brand_id=brand_id,
                    configuration_id=configuration_id,
                    total=len(generator.urls),
                    variables={"key": "value"},
                )
                multi = self.routing_multi_usecase.create(create_multi)
                order = 0
                for url in generator.urls:
                    order += 1
                    domain = URL(url).domain
                    create_multi_url = CreateRoutingMultiUrlSchema(
                        routing_multi_id=multi.data["id"],
                        url=url,
                        domain=domain,
                        order=order,
                    )
                    routing_type = "multi"
                    multi_url = self.routing_multi_url_usecase.create(create_multi_url)

            except Exception as e:
                raise e
        else:
            raise TypeNotSupportedException

        data_response = {
            "configuration": configuration.data,
            "routing_type": routing_type,
            "routing_urls": generator.urls,
        }

        return ResponseSuccessSchema(
            success=True, message="Generator created successfully", data=data_response
        )

    def process(self, generator: GetUrlSchema):
        """
        Processes a URL and returns the appropriate response.

        Args:
        - generator: An instance of GetUrlSchema containing the URL details.

        Returns:
        - A dictionary containing the processed URL details.

        Raises:
        - Exception: If an error occurs during the processing.
        """
        try:
            data_return = {}
            brand_code = generator.brand

            brand_response = self.brand_usecase.find_by_code(brand_code)

            zip_data = self.zipcode_query_usecase.get_info_by_zipcode(
                generator.zip_code
            )
            logging.info("zip_data:")
            logging.info(zip_data)
            if zip_data is None:
                raise Exception("Zipcode not found")

            state_code = zip_data["state"]

            state_str = zip_data["state"]
            zipcode_str = zip_data["zip"]
            city_str = zip_data["city"]

            configuration = self.configuration_query_usecase.find_configuration(
                FindConfigurationSchema(
                    language=generator.language,
                    insurance=generator.insurance,
                    device=generator.device,
                    media=generator.media,
                    state=state_code,
                    brand_id=brand_response.data["id"],
                )
            )
            if configuration is None:
                configuration = self.configuration_query_usecase.find_configuration(
                    FindConfigurationSchema(
                        language=generator.language,
                        insurance=generator.insurance,
                        device=generator.device,
                        media=generator.media,
                        state="NA",
                        brand_id=brand_response.data["id"],
                    )
                )
                if configuration is None:
                    logging.info("nada")
                    raise GeneratorRoutesNotConfigured

            data_configuration = configuration.to_dict()
            logging.info(data_configuration["system"])
            if data_configuration["type"] == 1:
                logging.info("single")
                logging.info(data_configuration["id"])
                single = self.routing_single_usecase.find_by_configuration_id(
                    data_configuration["id"]
                )

                data_return = {
                    "url": single.data["url"],
                    "domain": single.data["domain"],
                    "variables": single.data["variables"],
                }
                url_str = single.data["url"]
                domain_str = single.data["domain"]
                variables_str = single.data["variables"]
            elif data_configuration["type"] == 2:
                logging.info("mnulti")
                logging.info(data_configuration["id"])
                multi = self.routing_multi_usecase.find_by_configuration_id(
                    data_configuration["id"]
                )
                logging.info(multi)
                if multi.data["current"] == 0:
                    current = 1
                else:
                    current = multi.data["current"] + 1
                if current > multi.data["total"]:
                    current = 1
                logging.info(current)
                multi_url = (
                    self.routing_multi_url_usecase.find_by_routing_multi_id_and_order(
                        multi.data["id"], current
                    )
                )
                self.routing_multi_usecase.update_current_by_id(
                    multi.data["id"], current
                )
                logging.info(multi_url)
                url_str = multi_url.data["url"]
                domain_str = multi_url.data["domain"]
                variables_str = multi.data["variables"]

            logging.info("media_code")
            media_code = self.mediacode_query_usecase.get_mediacode(
                MediacodeSchema(
                    zip_code=generator.zip_code,
                    device=generator.device,
                    language=generator.language,
                    type_insurance=generator.insurance,
                    media=generator.media,
                    brand=brand_code,
                )
            )
            redirect_url = None
            media_code_str = None
            phone_str = None
            if media_code:
                data_mediacode = media_code.get("data")
                phone_str = data_mediacode["phone"]
                media_code_str = data_mediacode["media_code"]
                logging.info(data_mediacode["media_code"])
                redirect_url = self.mediacode_query_usecase.get_redirect_url(
                    UrlReplaceSchema(
                        url=url_str,
                        mediacode=media_code_str,
                        phone=phone_str,
                        zip_code=zipcode_str,
                        city=city_str,
                        state=state_str,
                        system=data_configuration["system"],
                    )
                )
                logging.info(redirect_url)

            data_return = {
                "domain": domain_str,
                "url": url_str,
                "url_redirect": redirect_url,
                "media_code": media_code_str,
                "phone": phone_str,
                "state": state_str,
                "zip_code": zipcode_str,
                "city": city_str,
                #"variables": multi.data["variables"],
            }

            # logging.info()
            if not generator.ip:
                generator.ip = "0.0.0.0"
            
            sqs_query ={
                "response": data_return,
                "status": 1,
                "brand_id": brand_response.data["id"],
                "language": generator.language,
                "ip":generator.ip,
            }
            logging.info(sqs_query)
            #convert sqs_query to json
            sqs_query = json.dumps(sqs_query)
            self.log_usecase.send_to_sqs(sqs_query)
            logging.info("FINISH sqs")
            data_response = {"index": 0}
            
            return ResponseSuccessSchema(
                success=True,
                message="Generator created successfully",
                data=data_return,
            )
        except Exception as e:
            raise e
