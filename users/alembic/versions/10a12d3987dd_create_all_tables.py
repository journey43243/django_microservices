"""create all tables

Revision ID: 10a12d3987dd
Revises: 
Create Date: 2024-09-16 18:12:41.509211

"""
from typing import Sequence, Union
from ...database.orm import create_tables, drop_tables

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10a12d3987dd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    create_tables()


def downgrade() -> None:
    drop_tables()
