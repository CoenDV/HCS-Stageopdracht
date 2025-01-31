"""updated llm logs

Revision ID: 68ef513c8716
Revises: a0285e69206b
Create Date: 2024-12-05 11:10:37.992117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68ef513c8716'
down_revision = 'a0285e69206b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('backend_logs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('prompt', sa.String(length=255), nullable=False))

    with op.batch_alter_table('llm_with_rag_logs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('model', sa.String(length=50), nullable=False))

    with op.batch_alter_table('llm_without_rag_logs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('model', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('llm_without_rag_logs', schema=None) as batch_op:
        batch_op.drop_column('model')

    with op.batch_alter_table('llm_with_rag_logs', schema=None) as batch_op:
        batch_op.drop_column('model')

    with op.batch_alter_table('backend_logs', schema=None) as batch_op:
        batch_op.drop_column('prompt')

    # ### end Alembic commands ###
