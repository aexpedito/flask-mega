"""Post table

Revision ID: e1f804c4282b
Revises: c6142b0e38d2
Create Date: 2019-05-09 22:20:05.689799

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import CreateSequence, Sequence, DropSequence


# revision identifiers, used by Alembic.
revision = 'e1f804c4282b'
down_revision = 'c6142b0e38d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(CreateSequence(Sequence('post_seq_id')))
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_email', sa.String(length=140), nullable=True),
    sa.ForeignKeyConstraint(['user_email'], ['tb_user.user_email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.execute(DropSequence(Sequence('post_seq_id')))
    # ### end Alembic commands ###
