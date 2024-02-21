"""empty message

Revision ID: 4c5d2a4e18e8
Revises: 
Create Date: 2024-02-20 17:33:04.796985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c5d2a4e18e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('profile_picture', sa.String(length=500), nullable=True),
    sa.Column('description', sa.String(length=400), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('message_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=500), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('sender_profile_id', sa.Integer(), nullable=False),
    sa.Column('receiver_profile_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['receiver_profile_id'], ['profile_table.id'], ),
    sa.ForeignKeyConstraint(['sender_profile_id'], ['profile_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.String(length=500), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['profile_id'], ['profile_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=500), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post_table.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profile_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment_table')
    op.drop_table('post_table')
    op.drop_table('message_table')
    op.drop_table('profile_table')
    # ### end Alembic commands ###