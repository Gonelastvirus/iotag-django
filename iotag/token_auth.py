'''from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from iotapp.models import Token
@database_sync_to_async
def get_token(request):
    user_id = request.user.id
    token = Token.objects.filter(user_id=user_id).values()
    return (token[0]['token'])
class JWTChannelMiddleware:

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        scope["token"] = await get_token()
        return await self.inner(scope, receive, send)'''
