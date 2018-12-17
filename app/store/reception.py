from app.async_tasks import tasks
from app.house import services
from app.house.residents import AbstractUser


class Clerk(AbstractUser):

    @classmethod
    def create_user_account(cls, user):
        user['password'] = services.SecurityService.hash(user['password'])
        user['token'] = services.SecurityService.generate_a_token()
        created_user = services.UserService.create_new(user)
        name = created_user.username
        from_address = "antunesleo4@gmail.com"
        to_address = created_user.email
        subject = "Test"
        tasks.start_send_email(name, from_address, to_address, subject)
        return created_user