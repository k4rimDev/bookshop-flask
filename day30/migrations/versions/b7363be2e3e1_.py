"""empty message

Revision ID: b7363be2e3e1
Revises: 
Create Date: 2022-05-30 19:56:06.699635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7363be2e3e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('author', sa.String(length=20), nullable=False),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('discount_price', sa.Float(), nullable=True),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('image_url', sa.String(length=200), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('publisher', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('language',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('language', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=20), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('created_at', sa.String(length=20), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('genre__book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('language__book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('language_id', sa.Integer(), nullable=True),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['language_id'], ['language.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('language__book')
    op.drop_table('genre__book')
    op.drop_table('comments')
    op.drop_table('language')
    op.drop_table('genre')
    op.drop_table('book')
    # ### end Alembic commands ###
