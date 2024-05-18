import json
from uuid import UUID, uuid4

from app.models.comment import Comment

from app.rabbitmq import send_comment_created, send_comment_rating_changed


class CommentsRepo:

    async def create_comment(self, comment: Comment):
        await send_comment_created(comment.model_dump_json())

    async def up_comment(self, comment_id: UUID):
        data = {
            'comment_id': str(comment_id),
            'delta': 1
        }

        await send_comment_rating_changed(json.dumps(data))

    async def down_comment(self, comment_id: UUID):
        data = {
            'comment_id': str(comment_id),
            'delta': -1
        }

        await send_comment_rating_changed(json.dumps(data))