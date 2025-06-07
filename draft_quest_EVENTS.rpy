## EXAMPLE QUEST EVENTS

##LABELS ARE USED BY CODE TO JUMP BETWEEN SNIPPETS OF DIALOGUE, EACH SNIPPET MUST HAVE A DIFFERENTLY NAMED LABEL
label example_quest_001_event01:
    David (thought) Neutral: "(The window is shattered... And the scratch marks on the frame seem to indicate it was not because of age or weather.)"
    Jack Surprise: "They did say the family left when they noticed a pack of Beowolves prowling increasingly closer."
    Penny Surprise: "And no Hunter would come take care of them?"
    Evelyn Sad: "Unfortunately, it would've been delaying the inevitable... Place this isolated, you can't defend it properly. Hunters can't be everywhere all the time."
    David Frown: "They're lucky the Beowolves didn't just attack them outright..."
    Penny Sad: "...still, how awful. Having to leave your home behind."

label example_quest_001_event02:
    Jack Surprise: "Huh, curious. You see that?"
    Evelyn Surprise: "See what? The hole in the roof?"
    Jack Smile: "Yes... And also the lack of tree branches. The structure is otherwise pretty solid, no?"
    Jack Surprise: "Wonder how that happened. Termites, maybe?"
    Evelyn Pain: "Oh ewewew I really hope not! Come on, let's find that ring and go!"


label example_quest_001_event03:
    If the coat-hangers have not been inspected:#IF STATEMENTS WITH BRANCHES IN DIALOGUE NEED A : AND EVERYTHING BELOW IN THE BRANCH TO BE TABBED RIGHT
        Evelyn Sad: "Awwww, what a waste... Look at the stitching on this coat. Such a beautiful thing, ruined."
        Evelyn Surprise: "Huh? Something fell out the pocket..."
        Penny Surprise: "A keychain... One is clearly for the front door."
        If the safe has been inspected:
            David Smile: "What do you bet one of the others opens the safe?"
            Jack Smile: "No bet. It's either that, or I freeze the metal off."
        If the safe has not been inspected:
            David Neutral: "Could be useful. If this ring was so precious, I bet they didn't just 	leave it out in the open."
            Jack Neutral: "Now we just need to find a hole to use one in..."
    If the coat-hangers have been inspected:
        David (thought) Neutral: "(Nothing else of interest that I can see...)"
        David Frown: "Evelyn, no."
        Evelyn Sad: "Buuuuuut baaaaaaaaaabyyyyyyyyy~"
        David Surprise: "You're an amazing tailor but not even you can do miracles."
        Evelyn Frown: "Uuuuugh..."


label example_quest_001_event04:
    If the coat-hangers have not been inspected:
        David Surprise: "So, if I was a Betting Boy..."
        Penny Smile: "A safe! Of course, if it was such a prized heirloom..."
        Evelyn Surprise: "I see a keyhole behind this wooden panel... Guess that's how you open it?"
        Jack Surprise: "Then we need to find the key. I doubt anything inside the safe would survive a Hunter-grad attempt and breaking into it."
    If the coat-hangers have been inspected:
        Jack Neutral: "The moment of truth. So, judging from the size of the hole..."
        Jack Smile: "Yes! It opened!"
        Penny Smile: "And look! Velvet cloth..."
        Evelyn Smile: "And a pretty little ring in it. Nice bauble, not gonna lie."
        David Neutral: "Not as nice as I thought it'd be... I guess the value is sentimental. Did the client mention why?"
        Jack Sad: "Hmm, from what I gathered this was their grandmother's favourite ring and, well... You saw the tombstone outside?"
        David Surprise: "...oh."
        Penny Sad: "...guess they didn't have the means to relocate the body, or to pay someone to do it. Back then or today."
        Evelyn Smile: "Wanna clean up the tombstone before we go?"
        David Smile: "My sentiments exactly."
