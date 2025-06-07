image jack_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/body_base.png"
)
image jack_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/exp_neutral.png"
)
image jack_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/exp_smile.png"
)
image jack_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/exp_amused.png"
)
image jack_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/exp_laugh.png"
)
image jack_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/exp_surprise.png"
)
image jack_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/exp_shock.png"
)
image jack_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/exp_angry.png"
)
image jack_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/exp_frown.png"
)
image jack_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/exp_sad.png"
)
image jack_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/exp_pain.png"
)
image jack_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/acc_sweat.png"
)
image jack_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/acc_blush.png"
)
image jack_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/jack/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/jack/acc_sweatdrop.png"
)
layeredimage Jack:
    group body:
        attribute base default:
            "jack_body_base"
    group accessories_2:
        attribute blush:
            "jack_acc_blush"
    group face:
        attribute neutral default:
            "jack_exp_neutral"#
        attribute amused:
            "jack_exp_amused"#
        attribute laugh:
            "jack_exp_laugh"#
        attribute smile:
            "jack_exp_smile"#
        attribute surprise:
            "jack_exp_surprise"#
        attribute shock:
            "jack_exp_shock"#
        attribute angry:
            "jack_exp_angry"#
        attribute frown:
            "jack_exp_frown"#
        attribute sad:
            "jack_exp_sad"#
        attribute pain:
            "jack_exp_pain"#
    group accessories:
        attribute sweat:
            "jack_acc_sweat"
        attribute sweatdrop:
            "jack_acc_sweatdrop"
    at character_sprites_jack

image Jack_bub = LayeredImageProxy("Jack", Transform(crop=(140, 0, 244, 238), zoom=0.9, xpos=1748, ypos=85, anchor=((0.5,0))))#TOP RIGHT