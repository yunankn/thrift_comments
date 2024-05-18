from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Body

from app.models.comment import Comment
from app.services.comments_service import CommentsService

comments_router = APIRouter(prefix='/comments')
CommentsServiceInj = Annotated[CommentsService, Depends(CommentsService)]


@comments_router.post('/create_comment')
async def create_comment(comment: Comment, service: CommentsServiceInj):
    await service.create_comment(comment)


@comments_router.post('/comment/{comment_id}/up')
async def up_comment(comment_id: UUID, service: CommentsServiceInj):
    await service.up_comment(comment_id)


@comments_router.post('/comment/{comment_id}/down')
async def down_comment(comment_id: UUID, service: CommentsServiceInj):
    await service.down_comment(comment_id)
