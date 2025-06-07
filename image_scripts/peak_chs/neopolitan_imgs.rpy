#Character Layered Images
#Conditional Neopolitan Images
image neopolitan_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/body_base.png"
)
image neopolitan_clothes_full = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/clothes_full.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/clothes_full.png"
)
image neopolitan_acc_dark = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/acc_dark.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/acc_dark.png"
)
image neopolitan_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/exp_smile.png"
)
image neopolitan_exp_amused = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/exp_amused.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/exp_amused.png"
)
image neopolitan_exp_crazy = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/exp_crazy.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/exp_crazy.png"
)
image neopolitan_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/exp_laugh.png"
)
image neopolitan_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/exp_surprise.png"
)
image neopolitan_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/exp_shock.png"
)
image neopolitan_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/exp_angry.png"
)
image neopolitan_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/exp_frown.png"
)
image neopolitan_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/exp_sad.png"
)
image neopolitan_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/exp_pain.png"
)
image neopolitan_exp_think = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/exp_think.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/exp_think.png"
)
image neopolitan_exp_think = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/exp_think.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/exp_think.png"
)
image neopolitan_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/acc_sweat.png"
)
image neopolitan_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/acc_blush.png"
)
image neopolitan_acc_sweatdrop = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/acc_sweatdrop.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/acc_sweatdrop.png"
)
image neopolitan_acc_glitch = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/neopolitan/acc_glitch.png",
    "persistent.PC98_mode == True", "images/PC98/ch/neopolitan/acc_glitch.png"
)
layeredimage Neopolitan:
    group body:
        attribute base default:
            "neopolitan_body_base"
    group clothes:
        attribute c_full default:
            "neopolitan_clothes_full"
    group accessories_2:
        attribute dark:
            "neopolitan_acc_dark"
        attribute blush:
            "neopolitan_acc_blush"
    group face:
        attribute amused:
            "neopolitan_exp_amused"#
        attribute laugh:
            "neopolitan_exp_laugh"#
        attribute smile default:
            "neopolitan_exp_smile"#
        attribute crazy:
            "neopolitan_exp_crazy"#
        attribute surprise:
            "neopolitan_exp_surprise"#
        attribute shock:
            "neopolitan_exp_shock"#
        attribute angry:
            "neopolitan_exp_angry"#
        attribute frown:
            "neopolitan_exp_frown"#
        attribute sad:
            "neopolitan_exp_sad"#
        attribute think:
            "neopolitan_exp_think"#
        attribute pain:
            "neopolitan_exp_pain"#
    group accessories:
        attribute sweat:
            "neopolitan_acc_sweat"
        attribute sweatdrop:
            "neopolitan_acc_sweatdrop"
    group accessories_3:
        attribute glitch:
            "neopolitan_acc_glitch"
    at character_sprites_neopolitan