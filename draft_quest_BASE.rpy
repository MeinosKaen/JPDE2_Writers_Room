## EXAMPLE QUEST

#define NAME OF QUEST OBJECT = Quest("TITLE", "IMAGE", "CLIENT", "CLIENT LOCATION", "REWARD", "SCREEN WITH DESCRIPTION", DURATION IN NUMBER OF DAYS)
define side_quest001_the_grimm_reaper = SideQuest("The Grimm Reaper", "qst/img005_the_grimm_reaper.png", "Glynda Goodwitch", "Island Nation of Menagerie", "100 Hunter Merits", "side_quest001_desc", 3)

#DEFINING TRIGGER VARIABLES FOR DESCRIPTION UPDATES, ALWAYS START AS FALSE

default side_quest001_step1 = False
default side_quest001_step2 = False
default side_quest001_step3 = False

#SCREEN THAT CONTAINS THE QUEST'S DESCRIPTION
#THE PLAYER'S NAME MUST BE REFERRED TO AS [p_n], NOT DAVID, SO THAT IT CHANGES WITH THE VARIABLE.
#THE STRINGS OF TEXTS MUST GO BETWEEN """___""" TRIPLE QUOTES, SO THAT THEY CAN BE LOCALIZED.
#justify True AT THE END MAKES SURE THE TEXT IS ALWAYS JUSTIFIED WHEN DISPLAYED ON SCREEN.

screen side_quest001_desc():
    text """Maria Calavera, the Grimm Reaper. A Hunter of legendary skill, with the most recorded kills of Gargantuan Grimm in recorded history. A loner and wanderer, she has never formally joined any Hunter Organization, and rarely stays long enough in one place to be tracked down.""" justify True
    text """This is the kind of individual that Ruby Rose has chosen as her teacher, behind suggestion from her mother Summer Rose, and is the kind of individual which the Duchy of Peak would love to bring into the fold. As luck would have it, Sienna Khan possessed intelligence that places her on the Island Nation of Menagerie...""" justify True
    if side_quest001_step1:
        text """After a brief roadblack in getting some information from a partly distrustful menagerian populace, [p_n] and his team manage to track down Ruby and Maria to the Menagerian outback. The reunion, with much potential for emotion, turned into a Penny-led farcical moment which left the veteran quite stunned.""" justify True
    if side_quest001_step2:
        text """Maria has revealed herself to not be as resistant to the idea of joining the local hunters as one might have thought... But, unimpressed with the team's showing so far, lays down a challenge: impress her enough with their Skill and she will give the offer serious consideration... Much to Ruby's surprise.""" justify True
    if side_quest001_step3:
        text """After a day of 'testing' Maria Calavera had originally refused the offer of joining the Royal Hunters, while simultaneously graduating Ruby Rose as her apprentice. Overnight, her choice changed, probably due to a private conversation she had with her student...""" justify True