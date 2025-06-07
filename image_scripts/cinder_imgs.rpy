
image cinder_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/body_base.png"
)
image cinder_body_base_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/body_base_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/body_base_full.png"
)
image cinder_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/clothes_full.png"
)
image cinder_clothes_half = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/clothes_half.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/clothes_half.png"
)
image cinder_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_neutral.png"
)
image cinder_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_smile.png"
)
image cinder_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_amused.png"
)
image cinder_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_laugh.png"
)
image cinder_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_surprise.png"
)
image cinder_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_shock.png"
)
image cinder_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_angry.png"
)
image cinder_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_frown.png"
)
image cinder_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_sad.png"
)
image cinder_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_pain.png"
)
image cinder_exp_cry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_cry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_cry.png"
)
image cinder_exp_fear = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_fear.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_fear.png"
)
image cinder_exp_sigh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/exp_sigh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/exp_sigh.png"
)
image cinder_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/acc_sweat.png"
)
image cinder_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/acc_blush.png"
)
image cinder_acc_eye = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/acc_eye.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/acc_eye.png"
)
image cinder_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/cinder/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/cinder/acc_sweatdrop.png"
)
layeredimage Cinder:
    group body:
        attribute base:
            "cinder_body_base"
        attribute full default:
            "cinder_body_base_full"
    group accessories_2:
        attribute blush:
            "cinder_acc_blush"
    group face:
        attribute neutral default:
            "cinder_exp_neutral"#
        attribute amused:
            "cinder_exp_amused"#
        attribute laugh:
            "cinder_exp_laugh"#
        attribute smile:
            "cinder_exp_smile"#
        attribute surprise:
            "cinder_exp_surprise"#
        attribute shock:
            "cinder_exp_shock"#
        attribute angry:
            "cinder_exp_angry"#
        attribute frown:
            "cinder_exp_frown"#
        attribute sad:
            "cinder_exp_sad"#
        attribute pain:
            "cinder_exp_pain"#
        attribute cry:
            "cinder_exp_cry"#
        attribute fear:
            "cinder_exp_fear"#
        attribute sigh:
            "cinder_exp_sigh"#
    group accessories_3:
        attribute eye:
            "cinder_acc_eye"
    group clothes:
        attribute c_full:
            "cinder_clothes_full"
        attribute c_half:
            "cinder_clothes_half"
    group accessories:
        attribute sweat:
            "cinder_acc_sweat"
        attribute sweatdrop:
            "cinder_acc_sweatdrop"
    at character_sprites_cinder