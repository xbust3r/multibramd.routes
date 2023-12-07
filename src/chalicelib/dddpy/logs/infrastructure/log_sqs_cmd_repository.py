
from chalicelib.dddpy.logs.domain.logs_repository import LogRepository
from chalicelib.dddpy.logs.usecase.logs_cmd_schema import CreateLogSchema
import boto3
import os

class LogSqsCmdRepositoryImpl(LogRepository):
    """
    This class is an implementation of the LogRepository interface.
    It uses Amazon SQS (Simple Queue Service) to store logs for later processing.
    """

    def __init__(self):
        """
        The constructor initializes the SQS client with the region specified in the environment variable.
        """
        self.sqs_client = boto3.client("sqs", region_name=os.environ.get("SQS_REGION"))

    def send_to_sqs(self, data: CreateLogSchema):
        """
        This method sends a log to the SQS queue.
        The log is represented by the CreateLogSchema object.
        The method converts the log object to a string and sends it to the SQS queue.
        The URL of the SQS queue is retrieved from an environment variable.
        The method returns the response from the SQS client.

        Args:
            data (CreateLogSchema): The log data to be sent to the SQS queue.

        Returns:
            dict: The response from the SQS client.
        """
        response = self.sqs_client.send_message(
            QueueUrl=os.environ.get("SQS_URL"),
            MessageBody=str(data),
        )
        return response