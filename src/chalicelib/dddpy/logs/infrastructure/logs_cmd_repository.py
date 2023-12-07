
from chalicelib.dddpy.logs.usecase.logs_cmd_schema import CreateLogSchema
from chalicelib.dddpy.logs.domain.logs_repository import LogRepository
from chalicelib.dddpy.logs.domain.logs import Log
from chalicelib.dddpy.logs.infrastructure.logs import DBLogs

from chalicelib.dddpy.shared.timezone import Timezone
from chalicelib.dddpy.shared.mysql.base import SessionLocal
from contextlib import contextmanager
import logging
from chalicelib.dddpy.shared.mysql.session_manager import session_scope


class LogCmdRepositoryImpl(DBLogs):
    """
    Implementation of the command repository for logs.

    This class provides methods to create log entries in the database.

    Attributes:
        None
    """

    def create(self, data: CreateLogSchema):
        """
        Creates a log entry.

        Args:
            data (CreateLogSchema): The data to use for the log entry.

        Returns:
            Log: The created log entry.
        """

        logging.info("create LOG DEBUG")
        logging.info(data)
        #check if data is a dict, if not is a dict covert to dict
        logging.info(type(data))
        #if not isinstance(data, dict):
        #    data=data.__dict__
        with session_scope() as session:
            today=Timezone.get_datetime()
            log = Log(
                response=data.response,
                status=data.status,
                ip=data.ip,
                brand_id=data.brand_id,
                language=data.language,
                created_at=today,
                updated_at=today,
            )
            new_log=Log.to_db(log)
            session.add(new_log)
            session.commit()
            session.refresh(new_log)
            return Log.from_db(new_log)
    