## EXAMPLE QUEST EVENTS - ADVANCED
##THIS IS HOW DIALOGUE EVENTS ARE CODED IN

##DIALOGUE VARIABLES
#These are True/False variables, False by default, they turn True when the associated snippet has been seen.
default example_quest_ADVANCED_001_event01 = False
default example_quest_ADVANCED_001_event02 = False
default example_quest_ADVANCED_001_event03 = False
default example_quest_ADVANCED_001_event04 = False

##CHARACTER DIALOGUE NAMES
#Characters are defined in the Script file of the original game, and they can automatically apply many things (quote marks, Italics for thoughts...). When writing dialogue, simply refer to the desired character,
#add the emotion and then write the dialogue between "". Follows an example list.
#d (DAVID NORMAL, QUOTES)
#d_i (DAVID THOUGHTS, FULL ITALICS, NO QUOTES)
#d_st (DAVID PHONE, UNDERLINED, QUOTES)
#j (JACK NORMAL, QUOTES)
#j_i (JACK THOUGHTS, FULL ITALICS, NO QUOTES)
#j_st (JACK PHONE, UNDERLINED, QUOTES)
#p (PENNY NORMAL, QUOTES)
#p_i (PENNY THOUGHTS, FULL ITALICS, NO QUOTES)
#p_st (PENNY PHONE, UNDERLINED, QUOTES)
#e (EVELYN NORMAL, QUOTES)
#e_i (EVELYN THOUGHTS, FULL ITALICS, NO QUOTES)
#e_st (EVELYN PHONE, UNDERLINED, QUOTES)
##All characters follow the same naming convention. Check SCRIPT.RPY to see a list of all the characters added so far.
##CHARACTER VARIABLES ARE ALL LOWER CASE, emotions must all be called in lower-case.

##LABELS ARE USED BY CODE TO JUMP BETWEEN SNIPPETS OF DIALOGUE, EACH SNIPPET MUST HAVE A DIFFERENTLY NAMED LABEL
label example_quest_ADVANCED_001_event01:
    d_i neutral "(The window is shattered... And the scratch marks on the frame seem to indicate it was not because of age or weather.)"
    j surprise "They did say the family left when they noticed a pack of Beowolves prowling increasingly closer."
    p surprise "And no Hunter would come take care of them?"
    e sad "Unfortunately, it would've been delaying the inevitable... Place this isolated, you can't defend it properly. Hunters can't be everywhere all the time."
    d frown "They're lucky the Beowolves didn't just attack them outright..."
    p sad "...still, how awful. Having to leave your home behind."
    if example_quest_ADVANCED_001_event01 == False:#This expression checks if the associated Variable is False. If it is...
        $ example_quest_ADVANCED_001_event01 = True#This command turns it True.

label example_quest_ADVANCED_001_event02:
    j surprise "Huh, curious. You see that?"
    e surprise "See what? The hole in the roof?"
    j smile "Yes... And also the lack of tree branches. The structure is otherwise pretty solid, no?"
    j surprise "Wonder how that happened. Termites, maybe?"
    e pain "Oh ewewew I really hope not! Come on, let's find that ring and go!"
    if example_quest_ADVANCED_001_event02 == False:#This expression checks if the associated Variable is False. If it is...
        $ example_quest_ADVANCED_001_event02 = True#This command turns it True.


label example_quest_ADVANCED_001_event03:
    if example_quest_ADVANCED_001_event03 == False:#IF STATEMENTS WITH BRANCHES IN DIALOGUE NEED A : AND EVERYTHING BELOW IN THE BRANCH TO BE TABBED RIGHT
        e sad "Awwww, what a waste... Look at the stitching on this coat. Such a beautiful thing, ruined."
        e surprise "Huh? Something fell out the pocket..."
        p surprise "A keychain... One is clearly for the front door."
        if example_quest_ADVANCED_001_event04:#DEPENDING WHETHER ANOTHER ONE OF THE SNIPPETS HAS BEEN SEEN BY THE PLAYER, THE CODE BRANCHES
            d smile "What do you bet one of the others opens the safe?"
            j smile "No bet. It's either that, or I freeze the metal off."
        else:#SIMPLE IF/ELSE TO CHECK IF ONE VARIABLE IS TRUE IS FINE
            d neutral "Could be useful. If this ring was so precious, I bet they didn't just 	leave it out in the open."
            j neutral "Now we just need to find a hole to use one in..."
    else:
        d_i neutral "(Nothing else of interest that I can see...)"
        d frown "Evelyn, no."
        e sad "Buuuuuut baaaaaaaaaabyyyyyyyyy~"
        d surprise "You're an amazing tailor but not even you can do miracles."
        e frown "Uuuuugh..."
    if example_quest_ADVANCED_001_event03 == False:#This expression checks if the associated Variable is False. If it is...
        $ example_quest_ADVANCED_001_event03 = True#This command turns it True.


label example_quest_ADVANCED_001_event04:
    if example_quest_ADVANCED_001_event03 == False:
        d surprise "So, if I was a Betting Boy..."
        p smile "A safe! Of course, if it was such a prized heirloom..."
        e surprise "I see a keyhole behind this wooden panel... Guess that's how you open it?"
        j surprise "Then we need to find the key. I doubt anything inside the safe would survive a Hunter-grad attempt and breaking into it."
    else:
        j neutral "The moment of truth. So, judging from the size of the hole..."
        j smile "Yes! It opened!"
        p smile "And look! Velvet cloth..."
        e smile "And a pretty little ring in it. Nice bauble, not gonna lie."
        d neutral "Not as nice as I thought it'd be... I guess the value is sentimental. Did the client mention why?"
        j sad "Hmm, from what I gathered this was their grandmother's favourite ring and, well... You saw the tombstone outside?"
        d surprise "...oh."
        p sad "...guess they didn't have the means to relocate the body, or to pay someone to do it. Back then or today."
        e smile "Wanna clean up the tombstone before we go?"
        d smile "My sentiments exactly."
    if example_quest_ADVANCED_001_event04 == False:#This expression checks if the associated Variable is False. If it is...
        $ example_quest_ADVANCED_001_event04 = True#This command turns it True.