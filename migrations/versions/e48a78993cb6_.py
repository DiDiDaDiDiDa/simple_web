"""empty message

Revision ID: e48a78993cb6
Revises: 
Create Date: 2024-04-24 12:16:42.821206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e48a78993cb6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='主键ID'),
    sa.Column('username', sa.String(length=40), nullable=False, comment='用户姓名'),
    sa.Column('pwd', sa.String(length=102), nullable=True, comment='密码'),
    sa.Column('salt', sa.String(length=32), nullable=True, comment='salt'),
    sa.Column('created_at', sa.DateTime(), nullable=False, comment='创建时间'),
    sa.Column('updated_at', sa.DateTime(), nullable=False, comment='更新时间'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
