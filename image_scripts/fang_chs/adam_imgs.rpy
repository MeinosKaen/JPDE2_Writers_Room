#Character Layered Images
#Conditional Adam Images
image adam_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/adam/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/adam/body_base.png"
)
image adam_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/adam/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/adam/exp_neutral.png"
)
image adam_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/adam/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/adam/exp_amused.png"
)
image adam_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/adam/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/adam/exp_surprise.png"
)
image adam_exp_shout = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/adam/exp_shout.png",
    "persistent.PC98_mode == True", "images/PC98/ch/adam/exp_shout.png"
)
image adam_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/adam/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/adam/exp_angry.png"
)
image adam_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/adam/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/adam/exp_frown.png"
)
image adam_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/adam/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/adam/exp_pain.png"
)
image adam_acc_dark = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/adam/acc_dark.png",
    "persistent.PC98_mode == True", "images/PC98/ch/adam/acc_dark.png"
)
image adam_extra_mask = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/adam/extra_mask.png",
    "persistent.PC98_mode == True", "images/PC98/ch/adam/extra_mask.png"
)
layeredimage Adam:
    group body:
        attribute base default:
            "adam_body_base"
    group face:
        attribute neutral default:
            "adam_exp_neutral"#
        attribute amused:
            "adam_exp_amused"#
        attribute angry:
            "adam_exp_angry"#
        attribute smile:
            "adam_exp_pain"#
        attribute surprise:
            "adam_exp_surprise"#
        attribute shout:
            "adam_exp_shout"#
        attribute frown:
            "adam_exp_frown"#
        attribute pain:
            "adam_exp_pain"#
    group accessories:
        attribute dark:
            "adam_acc_dark"
    group mask:
        attribute extra_mask default:
            "adam_extra_mask"
        attribute no_mask:
            Null()
    at character_sprites