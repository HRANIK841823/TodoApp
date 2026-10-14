"""phone number column adding for our user table

Revision ID: 2552e0e25748
Revises: 
Create Date: 2026-10-14 22:16:52.364494

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2552e0e25748'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))
    #(table_name,sa.Column(column_name,type,nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
