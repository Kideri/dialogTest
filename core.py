from dialog_bot_sdk.bot import DialogBot
from dialog_bot_sdk import interactive_media
from dialog_api import messaging_pb2
import time
import grpc
import q_config.core as q_config


class LocalMessage:
    def __init__(self, mid, date):
        self.mid = mid
        self.date = date


LocalUser = dict()


def on_msg(*params):
    # print(params)
    msg_text = params[0].message.textMessage.text
    if (msg_text == 'Хочу вопрос'):
        bot.messaging.send_message(
            params[0].peer,
            q_config.get_q(0, 0),
            q_config.get_a(0, 0, 0)
        )
    else:
        bot.messaging.send_message(
            params[0].peer, 'Reply to : ' + str(msg_text)
        )


def on_click(*params):
    # print(int(time.time()))
    qId = params[0].id
    print(qId)
    qA = params[0].value
    message = LocalMessage(params[0].mid, int(time.time() * 1000))
    tmp = qId.split('.')
    qSet = int(tmp[0])
    qId = int(tmp[1])
    uScore = int(tmp[2])
    if qA == q_config.get_A(qSet, qId):
        uScore += 1
    if q_config.get_is_final(qSet, qId):
        bot.messaging.update_message(
            message,
            'Подзравляю, Вы прошли тест!\n' + 
            'Ваш результат: ' + str(uScore) + ' / 4.'
        )
    else:
        bot.messaging.update_message(
            message,
            q_config.get_q(qSet, qId + 1),
            q_config.get_a(qSet, qId + 1, uScore)
        )
        # bot.messaging.update_message(
        #     message,
        #     'Test',
        #     [interactive_media.InteractiveMediaGroup(
        #         [
        #             interactive_media.InteractiveMedia(
        #                 '2',
        #                 interactive_media.InteractiveMediaButton('Test', 'Test')
        #             )
        #         ]
        #     )]
        # )
    


if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        'hackathon-mob.transmit.im',
        grpc.ssl_channel_credentials(),
        '75ea3221b62c6770adc2ff903ae90f4c9817f33c',
        verbose=True
    )

    bot.messaging.on_message(on_msg, on_click)