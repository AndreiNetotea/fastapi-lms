"""Add cascade on delete

Revision ID: 9c1c23fbcbe4
Revises: 191852c82ed6
Create Date: 2023-04-10 16:53:29.426172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9c1c23fbcbe4"
down_revision = "191852c82ed6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("courses_user_id_fkey", "courses", type_="foreignkey")
    op.create_foreign_key(
        None, "courses", "users", ["user_id"], ["id"], ondelete="CASCADE"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "courses", type_="foreignkey")
    op.create_foreign_key(
        "courses_user_id_fkey", "courses", "users", ["user_id"], ["id"]
    )
    # ### end Alembic commands ###
