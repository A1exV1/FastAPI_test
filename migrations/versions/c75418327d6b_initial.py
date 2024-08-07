"""Initial

Revision ID: c75418327d6b
Revises: 
Create Date: 2024-08-04 17:01:43.405054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c75418327d6b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flat', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('breed', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('flat', 'name')
    )
    op.create_table('walkers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dog_walker_id', sa.Integer(), nullable=False),
    sa.Column('dog_id', sa.Integer(), nullable=False),
    sa.Column('walk_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['dog_id'], ['dogs.id'], ),
    sa.ForeignKeyConstraint(['dog_walker_id'], ['walkers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('dog_id', 'walk_at')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('walkers')
    op.drop_table('dogs')
    # ### end Alembic commands ###
