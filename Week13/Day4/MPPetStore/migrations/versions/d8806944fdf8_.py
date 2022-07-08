"""empty message

Revision ID: d8806944fdf8
Revises: c71b16164981
Create Date: 2022-04-09 23:31:06.300527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8806944fdf8'
down_revision = 'c71b16164981'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'cart', ['pet_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cart', type_='unique')
    # ### end Alembic commands ###