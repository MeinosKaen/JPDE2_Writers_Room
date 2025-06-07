image philo_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/body_base.png"
)
image philo_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/clothes_full.png"
)
image philo_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/exp_neutral.png"
)
image philo_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/exp_smile.png"
)
image philo_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/exp_amused.png"
)
image philo_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/exp_laugh.png"
)
image philo_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/exp_surprise.png"
)
image philo_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/exp_shock.png"
)
image philo_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/exp_angry.png"
)
image philo_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/exp_frown.png"
)
image philo_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/exp_sad.png"
)
image philo_exp_bored = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/exp_bored.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/exp_bored.png"
)
image philo_exp_sigh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/exp_sigh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/exp_sigh.png"
)
image philo_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/exp_pain.png"
)
image philo_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/acc_sweat.png"
)
image philo_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/acc_blush.png"
)
image philo_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/philo/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/philo/acc_sweatdrop.png"
)
layeredimage Philo:
    group body:
        attribute base default:
            "philo_body_base"
    group clothes:
        attribute c_full default:
            "philo_clothes_full"
    group accessories_2:
        attribute blush:
            "philo_acc_blush"
    group face:
        attribute neutral default:
            "philo_exp_neutral"#
        attribute amused:
            "philo_exp_amused"#
        attribute laugh:
            "philo_exp_laugh"#
        attribute smile:
            "philo_exp_smile"#
        attribute surprise:
            "philo_exp_surprise"#
        attribute shock:
            "philo_exp_shock"#
        attribute angry:
            "philo_exp_angry"#
        attribute frown:
            "philo_exp_frown"#
        attribute sad:
            "philo_exp_sad"#
        attribute pain:
            "philo_exp_pain"#
        attribute bored:
            "philo_exp_bored"#
        attribute sigh:
            "philo_exp_sigh"#
    group accessories:
        attribute sweat:
            "philo_acc_sweat"
        attribute sweatdrop:
            "philo_acc_sweatdrop"
    at character_sprites_philo