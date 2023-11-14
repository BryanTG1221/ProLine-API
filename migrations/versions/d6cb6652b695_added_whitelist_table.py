"""Added Whitelist Table

Revision ID: d6cb6652b695
Revises: 8130eae1d0bb
Create Date: 2023-11-13 23:29:22.058925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6cb6652b695'
down_revision = '8130eae1d0bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('client', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lastname', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('client', schema=None) as batch_op:
        batch_op.drop_column('lastname')

    # ### end Alembic commands ###