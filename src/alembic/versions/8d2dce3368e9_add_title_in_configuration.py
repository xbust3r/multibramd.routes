"""add title in configuration

Revision ID: 8d2dce3368e9
Revises: 33a790aa6970
Create Date: 2023-10-25 14:55:50.847107

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d2dce3368e9'
down_revision: Union[str, None] = '33a790aa6970'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
