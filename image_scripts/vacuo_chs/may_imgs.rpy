
image may_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/body_base.png"
)
image may_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/clothes_full.png"
)
image may_shawl = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/shawl.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/shawl.png"
)
image may_hood = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/hood.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/hood.png"
)
image may_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/exp_neutral.png"
)
image may_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/exp_smile.png"
)
image may_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/exp_amused.png"
)
image may_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/exp_laugh.png"
)
image may_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/exp_surprise.png"
)
image may_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/exp_shock.png"
)
image may_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/exp_angry.png"
)
image may_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/exp_frown.png"
)
image may_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/exp_sad.png"
)
image may_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/exp_pain.png"
)
image may_exp_think = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/exp_think.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/exp_think.png"
)
image may_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/acc_sweat.png"
)
image may_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/acc_blush.png"
)
image may_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/may/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/may/acc_sweatdrop.png"
)
layeredimage May:
    group body:
        attribute base default:
            "may_body_base"
    group clothes:
        attribute c_full default:
            "may_clothes_full"
    group accessories_2:
        attribute dark:
            "may_acc_dark"
        attribute blush:
            "may_acc_blush"
    group face:
        attribute neutral default:
            "may_exp_neutral"#
        attribute amused:
            "may_exp_amused"#
        attribute laugh:
            "may_exp_laugh"#
        attribute smile:
            "may_exp_smile"#
        attribute surprise:
            "may_exp_surprise"#
        attribute shock:
            "may_exp_shock"#
        attribute angry:
            "may_exp_angry"#
        attribute frown:
            "may_exp_frown"#
        attribute sad:
            "may_exp_sad"#
        attribute pain:
            "may_exp_pain"#
        attribute think:
            "may_exp_think"#
    group accessories:
        attribute sweat:
            "may_acc_sweat"
        attribute sweatdrop:
            "may_acc_sweatdrop"
    group accessories_3:
        attribute hood:
            "may_hood"
    group accessories_4:
        attribute shawl:
            "may_shawl"
    at character_sprites_may