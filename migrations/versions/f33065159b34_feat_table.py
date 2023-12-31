"""Feat: (Table)

Revision ID: f33065159b34
Revises: 6b3931a39620
Create Date: 2023-11-24 23:07:16.136140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f33065159b34'
down_revision = '6b3931a39620'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sells', schema=None) as batch_op:
        batch_op.add_column(sa.Column('brand', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('model', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('year', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('price', sa.Float(), nullable=True))
        batch_op.drop_column('is_vehicle')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sells', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_vehicle', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_column('price')
        batch_op.drop_column('year')
        batch_op.drop_column('model')
        batch_op.drop_column('brand')

    # ### end Alembic commands ###
