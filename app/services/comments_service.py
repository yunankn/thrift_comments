from uuid import UUID

from fastapi import Depends
from app.models.comment import Comment

from app.repositories.comments_repo import CommentsRepo


class CommentsService:
    comments_repo: CommentsRepo

    def __init__(self, comments_repo: CommentsRepo = Depends(CommentsRepo)):
        self.comments_repo = comments_repo

    async def create_comment(self, comment: Comment):
        await self.comments_repo.create_comment(comment)

    async def up_comment(self, comment_id: UUID):
        await self.comments_repo.up_comment(comment_id)

    async def down_comment(self, comment_id):
        await self.comments_repo.down_comment(comment_id)
