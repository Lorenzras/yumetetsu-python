from src.controller.slack.sendToSlack import sendToSlackFormatted
postMessageResult = sendToSlackFormatted(10, "ใในใ", "info@yumetetsu.jp", "test@test.com")

print(postMessageResult)