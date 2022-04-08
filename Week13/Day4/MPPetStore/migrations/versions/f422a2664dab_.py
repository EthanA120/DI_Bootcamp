"""empty message

Revision ID: f422a2664dab
Revises: 
Create Date: 2022-04-07 19:52:28.172066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f422a2664dab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=35), nullable=True),
    sa.Column('gender', sa.String(length=35), nullable=True),
    sa.Column('breed', sa.String(length=35), nullable=True),
    sa.Column('date_of_birth', sa.DATE(), nullable=True),
    sa.Column('details', sa.TEXT(length=70), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pet')
    # ### end Alembic commands ###
