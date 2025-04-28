"""Create daily_wod and wod tables

Revision ID: a620edda5351
Revises: 
Create Date: 2025-04-28 09:11:41.428355

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM

# revision identifiers, used by Alembic.
revision: str = 'a620edda5351'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    """Upgrade schema."""
    wod_type = ENUM('FOR_TIME', 'EMOM', 'TABATA', 'AMRAP', name='wod_type_enum')

    op.create_table(
        'wod',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('type', wod_type, nullable=False),
        sa.Column('time_cap', sa.Integer(), nullable=False),
        sa.Column('description', sa.String(), nullable=False)
    )

    op.create_table(
        'daily_wod',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('warm_up', sa.String(), nullable=False),
        sa.Column('skill', sa.String(), nullable=False),
        sa.Column('data', sa.Date(), nullable=False),
        sa.Column('wod_id', sa.Integer(), sa.ForeignKey('wod.id', ondelete='CASCADE'), nullable=False)
    )

def downgrade():
    """Downgrade schema."""
    op.drop_table('daily_wod')
    op.drop_table('wod')
