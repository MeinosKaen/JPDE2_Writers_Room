#Character Layered Images
#Conditional Gemma Images
image gemma_body_base = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/body_base.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/body_base.png"
)
image gemma_clothes_casual = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/clothes_casual.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/clothes_casual.png"
)
image gemma_clothes_mili = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/clothes_mili.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/clothes_mili.png"
)
image gemma_clothes_wait = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/clothes_wait.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/clothes_wait.png"
)
image gemma_clothes_bart = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/clothes_bart.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/clothes_bart.png"
)
image gemma_clothes_nurse = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/clothes_nurse.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/clothes_nurse.png"
)
image gemma_acc_dark = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/acc_dark.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/acc_dark.png"
)
image gemma_exp_neutral = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/exp_neutral.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/exp_neutral.png"
)
image gemma_exp_pout = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/exp_pout.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/exp_pout.png"
)
image gemma_exp_smile = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/exp_smile.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/exp_smile.png"
)
image gemma_exp_surprise = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/exp_surprise.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/exp_surprise.png"
)
image gemma_exp_shock = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/exp_shock.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/exp_shock.png"
)
image gemma_exp_angry = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/exp_angry.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/exp_angry.png"
)
image gemma_exp_laugh = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/exp_laugh.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/exp_laugh.png"
)
image gemma_exp_frown = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/exp_frown.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/exp_frown.png"
)
image gemma_exp_sad = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/exp_sad.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/exp_sad.png"
)
image gemma_exp_pain = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/exp_pain.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/exp_pain.png"
)
image gemma_acc_sweat = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/acc_sweat.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/acc_sweat.png"
)
image gemma_acc_blush = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/acc_blush.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/acc_blush.png"
)
image gemma_acc_glitch = ConditionSwitch(
    "persistent.PC98_mode == False", "images/ch/gemma/acc_glitch.png",
    "persistent.PC98_mode == True", "images/PC98/ch/gemma/acc_glitch.png"
)
layeredimage Gemma:
    group body:
        attribute base default:
            "gemma_body_base"
    group clothes:
        attribute c_casual:
            "gemma_clothes_casual"
        attribute c_mili:
            "gemma_clothes_mili"
        attribute c_bart:
            "gemma_clothes_bart"
        attribute c_wait:
            "gemma_clothes_wait"
        attribute c_nurse:
            "gemma_clothes_nurse"
    group accessories_3:
        attribute blush:
            "gemma_acc_blush"
    group face:
        attribute neutral default:
            "gemma_exp_neutral"#
        attribute smile:
            "gemma_exp_smile"#
        attribute surprise:
            "gemma_exp_surprise"#
        attribute shock:
            "gemma_exp_shock"#
        attribute angry:
            "gemma_exp_angry"#
        attribute frown:
            "gemma_exp_frown"#
        attribute laugh:
            "gemma_exp_laugh"#
        attribute pout:
            "gemma_exp_pout"#
        attribute sad:
            "gemma_exp_sad"#
        attribute pain:
            "gemma_exp_pain"#
    group accessories:
        attribute sweat:
            "gemma_acc_sweat"
        attribute dark:
            "gemma_acc_dark"
    group accessories_2:
        attribute glitch:
            "gemma_acc_glitch"
    at character_sprites_gemma