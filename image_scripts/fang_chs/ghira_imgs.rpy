
image ghira_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/body_base.png"
)
image ghira_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/clothes_full.png"
)
image ghira_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/exp_neutral.png"
)
image ghira_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/exp_smile.png"
)
image ghira_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/exp_amused.png"
)
image ghira_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/exp_laugh.png"
)
image ghira_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/exp_surprise.png"
)
image ghira_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/exp_shock.png"
)
image ghira_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/exp_angry.png"
)
image ghira_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/exp_frown.png"
)
image ghira_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/exp_sad.png"
)
image ghira_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/exp_pain.png"
)
image ghira_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/acc_sweat.png"
)
image ghira_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/acc_blush.png"
)
image ghira_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/ghira/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/ghira/acc_sweatdrop.png"
)
layeredimage Ghira:
    group body:
        attribute base default:
            "ghira_body_base"
    group clothes:
        attribute c_full default:
            "ghira_clothes_full"
    group accessories_2:
        attribute blush:
            "ghira_acc_blush"
    group face:
        attribute neutral default:
            "ghira_exp_neutral"#
        attribute amused:
            "ghira_exp_amused"#
        attribute laugh:
            "ghira_exp_laugh"#
        attribute smile:
            "ghira_exp_smile"#
        attribute surprise:
            "ghira_exp_surprise"#
        attribute shock:
            "ghira_exp_shock"#
        attribute angry:
            "ghira_exp_angry"#
        attribute frown:
            "ghira_exp_frown"#
        attribute sad:
            "ghira_exp_sad"#
        attribute pain:
            "ghira_exp_pain"#
    group accessories:
        attribute sweat:
            "ghira_acc_sweat"
        attribute sweatdrop:
            "ghira_acc_sweatdrop"
    at character_sprites_ghira