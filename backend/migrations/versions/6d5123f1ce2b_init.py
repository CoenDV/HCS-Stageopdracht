"""init

Revision ID: 6d5123f1ce2b
Revises: 
Create Date: 2024-10-23 11:03:02.497340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d5123f1ce2b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('licensePlate', sa.String(length=8), nullable=False),
    sa.Column('brand', sa.String(length=50), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('currentValue', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('licensePlate')
    )
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    op.create_table('insurance_policy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('dateStart', sa.Date(), nullable=False),
    sa.Column('pricePerMonth', sa.Float(), nullable=False),
    sa.Column('insuranceType', sa.Enum('WA', 'WA_PLUS', 'ALL_RISK', name='insurancetype'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('insurance_policy')
    op.drop_table('customer')
    op.drop_table('car')
    # ### end Alembic commands ###
