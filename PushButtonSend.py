import pymsteams
from gpiozero import Button

message = pymsteams.connectorcard("https://masseyuni.webhook.office.com/webhookb2/5dffb57a-7a47-45aa-b35c-875ffc8c995c@388728e1-bbd0-4378-98dc-f8682e644300/IncomingWebhook/d47efa67ed8c4be983309ad3ce297fea/5f90cd43-6bdb-4cc2-a793-fce40b8bb5e1")

message.text("Someone has pressed the button and requires your attention!!!")

button = Button(3)
button.wait_for_press()
print("pressed!")
message.send()

