from models import User, Message


if __name__ == "__main__":
    gab = User.get(User.name == "gab")
    # gab.delete_instance()
    # gab = User.create_user(name="gab", email="gab@gmail.com", password="Test250")
    
    # Message.create(title="Test Message", message="This is a test message", user=gab, test="Test field")
    # messages = gab.messages
    # for message in messages:
    #     print(message.title, message.message, message.created_at, message.user.name, message.test)

    # print(gab.login("Test25"))