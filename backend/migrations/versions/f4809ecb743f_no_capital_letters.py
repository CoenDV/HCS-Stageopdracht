"""no capital letters

Revision ID: f4809ecb743f
Revises: 80df22119dfc
Create Date: 2024-11-20 09:30:26.489115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4809ecb743f'
down_revision = '80df22119dfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('current_value', sa.Float(), nullable=False))
        batch_op.drop_column('currentValue')

    with op.batch_alter_table('customer_policy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_start', sa.Date(), nullable=False))
        batch_op.add_column(sa.Column('price_per_month', sa.Float(), nullable=False))
        batch_op.drop_column('pricePerMonth')
        batch_op.drop_column('dateStart')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customer_policy', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dateStart', sa.DATE(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('pricePerMonth', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
        batch_op.drop_column('price_per_month')
        batch_op.drop_column('date_start')

    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('currentValue', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
        batch_op.drop_column('current_value')

    # ### end Alembic commands ###
