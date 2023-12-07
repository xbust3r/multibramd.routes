"""add logs

Revision ID: ef60f2ee0e93
Revises: 8d2dce3368e9
Create Date: 2023-11-30 15:59:18.295078

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef60f2ee0e93'
down_revision: Union[str, None] = '8d2dce3368e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "atalaya_logs",
        sa.Column("id", sa.BigInteger, primary_key=True),
        sa.Column("response", sa.JSON, nullable=False),
        sa.Column("brand_id", sa.BigInteger, sa.ForeignKey("atalaya_brands.id"), nullable=False),
        sa.Column("language", sa.String(5), nullable=False),
        sa.Column("status", sa.Boolean, nullable=False),
        sa.Column("ip", sa.String(120), nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
        
    )


def downgrade() -> None:
    op.drop_table("atalaya_logs")
