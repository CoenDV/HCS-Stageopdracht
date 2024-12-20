"""empty message

Revision ID: 5bedc4fe9414
Revises: 
Create Date: 2024-11-27 14:25:04.111209

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5bedc4fe9414'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('backend_logs', schema=None) as batch_op:
        batch_op.alter_column('correlation_id',
               existing_type=sa.VARCHAR(length=36),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)

    with op.batch_alter_table('frontend_logs', schema=None) as batch_op:
        batch_op.alter_column('correlation_id',
               existing_type=sa.VARCHAR(length=36),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)

    with op.batch_alter_table('llm_logs', schema=None) as batch_op:
        batch_op.alter_column('correlation_id',
               existing_type=sa.VARCHAR(length=36),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
        batch_op.alter_column('without_rag_answer',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('without_rag_duration',
               existing_type=postgresql.TIME(),
               nullable=True)
        batch_op.alter_column('with_rag_answer',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('with_rag_duration',
               existing_type=postgresql.TIME(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('llm_logs', schema=None) as batch_op:
        batch_op.alter_column('with_rag_duration',
               existing_type=postgresql.TIME(),
               nullable=False)
        batch_op.alter_column('with_rag_answer',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('without_rag_duration',
               existing_type=postgresql.TIME(),
               nullable=False)
        batch_op.alter_column('without_rag_answer',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('correlation_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=36),
               existing_nullable=False,
               autoincrement=True)

    with op.batch_alter_table('frontend_logs', schema=None) as batch_op:
        batch_op.alter_column('correlation_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=36),
               existing_nullable=False,
               autoincrement=True)

    with op.batch_alter_table('backend_logs', schema=None) as batch_op:
        batch_op.alter_column('correlation_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=36),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###
