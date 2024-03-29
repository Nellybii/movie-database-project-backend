"""create movies table

Revision ID: 7acc5b70a3d8
Revises: 
Create Date: 2023-12-17 04:12:44.100973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7acc5b70a3d8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.VARCHAR(), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('genre', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('runtime', sa.VARCHAR(), nullable=False),
    sa.Column('production_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###
