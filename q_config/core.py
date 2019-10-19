import q_config.q_s as q_s
from dialog_bot_sdk import interactive_media

def get_q(set_id, id):
    return q_s.q_list[set_id][id].get_q()


def get_a(set_id, id, score):
    ret = []
    answ = q_s.q_list[set_id][id].get_a()
    for cur in answ:
        ret.append(
            interactive_media.InteractiveMedia(
                str(set_id) + '.' + str(id) + '.' + str(score),
                interactive_media.InteractiveMediaButton(cur[1], cur[0])
        ))
    return [interactive_media.InteractiveMediaGroup(ret)]


def get_A(set_id, id):
    return q_s.q_list[set_id][id].get_A()


def get_is_final(set_id, id):
    return q_s.q_list[set_id][id].get_is_final()