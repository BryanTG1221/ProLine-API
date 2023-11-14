"""Added Employe table

Revision ID: 8130eae1d0bb
Revises: e50d2e0432d6
Create Date: 2023-11-13 22:25:08.444741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8130eae1d0bb'
down_revision = 'e50d2e0432d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('position', sa.String(length=50), nullable=False),
    sa.Column('department', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    # ### end Alembic commands ###
