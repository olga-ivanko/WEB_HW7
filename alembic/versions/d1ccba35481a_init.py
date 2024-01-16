"""Init

Revision ID: d1ccba35481a
Revises: 
Create Date: 2024-01-16 17:04:46.999687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1ccba35481a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('10', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('group_id')
    )
    op.create_table('professors',
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('50', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('professor_id')
    )
    op.create_table('students',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('50', sa.String(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.group_id'], ),
    sa.PrimaryKeyConstraint('student_id')
    )
    op.create_table('subjects',
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('25', sa.String(), nullable=False),
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['professor_id'], ['professors.professor_id'], ),
    sa.PrimaryKeyConstraint('subject_id'),
    sa.UniqueConstraint('25')
    )
    op.create_table('grades',
    sa.Column('grade_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.Column('date_recieved', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.student_id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.subject_id'], ),
    sa.PrimaryKeyConstraint('grade_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grades')
    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('professors')
    op.drop_table('groups')
    # ### end Alembic commands ###
