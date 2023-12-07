
from chalicelib.dddpy.logs.domain.logs_repository import LogRepository
from chalicelib.dddpy.logs.domain.logs import Log
from chalicelib.dddpy.logs.infrastructure.logs import DBLogs
from chalicelib.dddpy.shared.timezone import Timezone
from chalicelib.dddpy.shared.mysql.base import SessionLocal
from chalicelib.dddpy.shared.mysql.session_manager import session_scope

class LogQueryRepositoryImpl:
    """
    This class represents the implementation of a query repository for logs.
    It provides methods to retrieve logs from the database.
    """

    def all(self):
        """
        Retrieves all logs from the database.

        Returns:
            A list of Log objects representing the logs.
        """
        with session_scope() as session:
            logs = session.query(DBLogs).all()
            if logs is None:
                return None
            
            data = [Log.from_db(log) for log in logs]
            
            return data
    
    def find_by_id(self, id):
        """
        Retrieves a log from the database by its ID.

        Args:
            id: The ID of the log to retrieve.

        Returns:
            A Log object representing the log with the specified ID, or None if not found.
        """
        with session_scope() as session:
            log = session.query(DBLogs).filter(DBLogs.id == id).first()
            if log is None:
                return None
            return Log.from_db(log)

