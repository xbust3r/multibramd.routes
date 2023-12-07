
from datetime import datetime
from typing import Optional

from chalicelib.dddpy.logs.infrastructure.logs import DBLogs


class Log:
    """
    Represents a log entry.

    Args:
        status (bool): The status of the log.
        response (dict): The response of the log.
        ip (str): The IP address associated with the log.
        brand_id (int): The brand ID associated with the log.
        language (str): The language associated with the log.
        created_at (datetime, optional): The creation timestamp of the log. Defaults to None.
        updated_at (datetime, optional): The update timestamp of the log. Defaults to None.
        id (int, optional): The ID of the log. Defaults to None.
    """

    def __init__(
        self,
        status: bool,
        response: dict,
        ip: str,
        brand_id: int,
        language: str,
        created_at: datetime = None,
        updated_at: datetime = None,
        id: Optional[int] = None,
    ) -> None:
        self.id = id
        self.status = status
        self.response = response
        self.ip = ip
        self.brand_id = brand_id
        self.language = language
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_db(cls, db_logs: DBLogs) -> "Log":
        """
        Creates a Log instance from a DBLogs instance.

        Args:
            db_logs (DBLogs): The DBLogs instance.

        Returns:
            Log: The Log instance.
        """
        return cls(
            id=db_logs.id,
            status=db_logs.status,
            response=db_logs.response,
            ip=db_logs.ip,
            brand_id=db_logs.brand_id,
            language=db_logs.language,
            created_at=db_logs.created_at,
            updated_at=db_logs.updated_at,
        )

    @classmethod
    def to_db(cls, log: "Log") -> DBLogs:
        """
        Converts a Log instance to a DBLogs instance.

        Args:
            log (Log): The Log instance.

        Returns:
            DBLogs: The DBLogs instance.
        """
        return DBLogs(
            id=log.id,
            status=log.status,
            response=log.response,
            ip=log.ip,
            brand_id=log.brand_id,
            language=log.language,
            created_at=log.created_at,
            updated_at=log.updated_at,
        )

    def to_dict(self) -> dict:
        """
        Converts the Log instance to a dictionary.

        Returns:
            dict: The dictionary representation of the Log instance.
        """
        return {
            "id": self.id,
            "status": self.status,
            "response": self.response,
            "brand_id": self.brand_id,
            "language": self.language,
            "ip": self.ip,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
