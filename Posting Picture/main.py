from instabot import Bot

bot = Bot()

bot.login(username="User Name", password="User password")

bot.upload_photo("Picture.jpg", caption="Write the caption here")
#This Picture.jpg should be in the same directory which has this code
