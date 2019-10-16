from dialog_bot_sdk.bot import DialogBot
from dialog_bot_sdk import interactive_media
from dialog_api import messaging_pb2
import time
import grpc


class LocalMessage:
    def __init__(self, mid, date):
        self.mid = mid
        self.date = date


def on_msg(*params):
    print(params)
    msg_text = params[0].message.textMessage.text
    if (msg_text == 'Хочу вопрос'):
        bot.messaging.send_message(
            params[0].peer,
            "Артем гей?",
            [interactive_media.InteractiveMediaGroup(
                [
                    interactive_media.InteractiveMedia(
                        1,
                        interactive_media.InteractiveMediaButton("True", "Да!")
                    ),
                    interactive_media.InteractiveMedia(
                        1,
                        interactive_media.InteractiveMediaButton("Flase", "Нет!")
                    )
                ]
            )]
        )
    elif (msg_text == 'Хочу другой вопрос'):
        bot.messaging.send_message(
            params[0].peer,
            "Темир гей?",
            [interactive_media.InteractiveMediaGroup(
                [
                    interactive_media.InteractiveMedia(
                        2,
                        interactive_media.InteractiveMediaButton("Flase", "Нет!")
                    ),
                    interactive_media.InteractiveMedia(
                        2,
                        interactive_media.InteractiveMediaButton("True", "Да!")
                    )
                ]
            )]
        )
    else:
        bot.messaging.send_message(
            params[0].peer, 'Reply to : ' + str(msg_text)
        )


def on_click(*params):
    # print(int(time.time()))
    qId = params[0].id
    qA = params[0].value
    message = LocalMessage(params[0].mid, int(time.time() * 1000))
    if (qId == '1'):
        if (qA == 'True'):
            answer = 'Все верно, Артем гей!'
        else:
            answer = 'Увы, но Артем гей!'
        bot.messaging.update_message(
            message,
            answer
        )
    elif (qId == '2'):
        if (qA == 'True'):
            answer = 'Все верно, Темир гей!'
        else:
            answer = 'Увы, но Темир гей!'
        bot.messaging.update_message(
            message,
            answer
        )
    


if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        'hackathon-mob.transmit.im',
        grpc.ssl_channel_credentials(),
        '75ea3221b62c6770adc2ff903ae90f4c9817f33c',
        verbose=True
    )

    bot.messaging.on_message(on_msg, on_click)