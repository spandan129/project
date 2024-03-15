from django.db import models

class UserMessage_to_friends(models.Model):
    message_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.message_id)

class friendMessage_to_user(models.Model):
    message_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.message_id)

class Friends(models.Model):
    friend_id = models.IntegerField(primary_key=True)
    friend_name = models.CharField(max_length=30)
    usermessage = models.ManyToManyField(UserMessage_to_friends, blank=True, null=True)
    friendmessage = models.ManyToManyField(friendMessage_to_user, blank=True, null=True)


    def __str__(self):
        return self.friend_name

class UserMessage_to_group(models.Model):
    message_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=1000)
    def __str__(self):
        return self.message_id
    
class othersMessage_to_group(models.Model):
    message_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=1000)
    def __str__(self):
        return self.message_id

class Group_users(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=30)
    usermessage = models.ForeignKey(UserMessage_to_group, on_delete=models.CASCADE, blank=True, null=True)
    othersmessage = models.ForeignKey(othersMessage_to_group, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.user_name
    
class GroupChat(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=255)
    group_users = models.ForeignKey(Group_users, on_delete=models.CASCADE)

    def __str__(self):
        return self.group_name
    
class Users(models.Model):
    user_id = models.AutoField(primary_key = True)
    user_name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    friends = models.ForeignKey(Friends, on_delete=models.CASCADE, blank=True, null=True)
    groupchat = models.ForeignKey(GroupChat, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return str(self.user_name)
    
class Chat(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to='images/')
    product_description = models.CharField(max_length=1000)
    product_category = models.CharField(max_length = 30)

class Post(models.Model):
    post_id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(Users, on_delete = models.CASCADE, blank=False, null=False)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, default="default.jpg")


    def __str__(self):
        return str(self.post_id)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete = models.CASCADE, blank=False, null=False)
    actual_comment = models.TextField(default="")


    def __str__(self):
        return str(self.comment_id)