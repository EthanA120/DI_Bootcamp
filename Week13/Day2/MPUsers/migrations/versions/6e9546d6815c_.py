"""empty message

Revision ID: 6e9546d6815c
Revises: 
Create Date: 2022-04-01 13:27:54.200425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e9546d6815c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=35), nullable=True),
    sa.Column('street', sa.String(length=35), nullable=True),
    sa.Column('city', sa.String(length=35), nullable=True),
    sa.Column('zipcode', sa.String(length=35), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
