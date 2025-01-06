# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:21:52 2024

@author: Nathan
"""

import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
#%% Create function

def find_common_words(lyrics: str, num_words: int = 10):
    
    boring_words = ["the", "a", "and", "it", "it's", "to", "that", "lot", "an",
                    "or", "but", "if", "nor", "so", "yet", "for", "in", "on",
                    "at", "to", "by", "with", "from", "of", "about", "as", "like",
                    "that's", "all", "there", "this",
                    
                    #pronouns
                    "i", "you", "he", "she", "it", "we", "they", "me", "him", "her",
                    "us", "them", "my", "your", "his", "her", "our", "their", 
                    "mine", "yours", "ours", "theirs",
                    
                    #common verbs
                    "is", "are", "am", "was", "were", "be", "been", "being",
                    "have", "has", "had", "do", "does", "did", "will", "go",
                    "won't", "don't",
                    
                    #noises
                    "oh", "yeah", "uh", "la", "na", "woah", "ah", "ooh"]
                    
    strip_words = re.findall(r"\b\w+(?:'\w+)?\b", lyrics.lower())
                       
    words = [word for word in strip_words if word not in boring_words]
        
    word_counts = Counter(words)
    
    word_counts = dict(word_counts)
    
    common_words = [(word, count) for word, count in word_counts.items()]
    
    return sorted(common_words, key = lambda x: x[1], reverse = True)[:num_words]



#%% Testing

xmas_lyrics = """
I don't want a lot for Christmas
There is just one thing I need
I don't care about the presents underneath the Christmas tree
I just want you for my own
More than you could ever know
Make my wish come true
All I want for Christmas is you
Yeah
I don't want a lot for Christmas
There is just one thing I need (and I)
Don't care about the presents underneath the Christmas tree
I don't need to hang my stocking there upon the fireplace
Santa Claus won't make me happy with a toy on Christmas Day
I just want you for my own
More than you could ever know
Make my wish come true
All I want for Christmas is you
You, baby
Oh, I won't ask for much this Christmas
I won't even wish for snow (and I)
I'm just gonna keep on waiting underneath the mistletoe
I won't make a list and send it to the North Pole for Saint Nick
I won't even stay awake to hear those magic reindeer click
'Cause I just want you here tonight
Holding on to me so tight
What more can I do?
Oh, baby, all I want for Christmas is you
You, baby
Oh-oh, all the lights are shining so brightly everywhere (so brightly, baby)
And the sound of children's laughter fills the air (oh, oh, yeah)
And everyone is singing (oh, yeah)
I hear those sleigh bells ringing
Santa, won't you bring me the one I really need? (Yeah, oh)
Won't you please bring my baby to me?
Oh, I don't want a lot for Christmas
This is all I'm asking for
I just wanna see my baby standing right outside my door
Oh, I just want you for my own
More than you could ever know
Make my wish come true
Oh, baby, all I want for Christmas is you
You, baby
All I want for Christmas is you, baby
All I want for Christmas is you, baby
All I want for Christmas is you, baby
All I want for Christmas (all I really want) is you, baby
All I want (I want) for Christmas (all I really want) is you, baby
"""


#%% lyrics list

xmas_lyrics_list = ["""I don't want a lot for Christmas
                    There is just one thing I need
                    I don't care about the presents underneath the Christmas tree
                    I just want you for my own
                    More than you could ever know
                    Make my wish come true
                    All I want for Christmas is you
                    Yeah
                    I don't want a lot for Christmas
                    There is just one thing I need (and I)
                    Don't care about the presents underneath the Christmas tree
                    I don't need to hang my stocking there upon the fireplace
                    Santa Claus won't make me happy with a toy on Christmas Day
                    I just want you for my own
                    More than you could ever know
                    Make my wish come true
                    All I want for Christmas is you
                    You, baby
                    Oh, I won't ask for much this Christmas
                    I won't even wish for snow (and I)
                    I'm just gonna keep on waiting underneath the mistletoe
                    I won't make a list and send it to the North Pole for Saint Nick
                    I won't even stay awake to hear those magic reindeer click
                    'Cause I just want you here tonight
                    Holding on to me so tight
                    What more can I do?
                    Oh, baby, all I want for Christmas is you
                    You, baby
                    Oh-oh, all the lights are shining so brightly everywhere (so brightly, baby)
                    And the sound of children's laughter fills the air (oh, oh, yeah)
                    And everyone is singing (oh, yeah)
                    I hear those sleigh bells ringing
                    Santa, won't you bring me the one I really need? (Yeah, oh)
                    Won't you please bring my baby to me?
                    Oh, I don't want a lot for Christmas
                    This is all I'm asking for
                    I just wanna see my baby standing right outside my door
                    Oh, I just want you for my own
                    More than you could ever know
                    Make my wish come true
                    Oh, baby, all I want for Christmas is you
                    You, baby
                    All I want for Christmas is you, baby
                    All I want for Christmas is you, baby
                    All I want for Christmas is you, baby
                    All I want for Christmas (all I really want) is you, baby
                    All I want (I want) for Christmas (all I really want) is you, baby
                    """,
                    """Jingle bell, jingle bell, jingle bell rock
Jingle bells swing and jingle bells ring
Snowin' and blowin' up bushels of fun
Now the jingle hop has begun
Jingle bell, jingle bell, jingle bell rock
Jingle bells chime in jingle bell time
Dancin' and prancin' in Jingle Bell Square
In the frosty air
What a bright time, it's the right time
To rock the night away
Jingle bell time is a swell time
To go glidin' in a one-horse sleigh
Giddy-up jingle horse, pick up your feet
Jingle around the clock
Mix and a-mingle in the jinglin' feet
That's the jingle bell rock
Jingle bell, jingle bell, jingle bell rock
Jingle bells chime in jingle bell time
Dancin' and prancin' in Jingle Bell Square
In the frosty air
What a bright time, it's the right time
To rock the night away
Jingle bell time is a swell time
To go glidin' in a one-horse sleigh
Giddy-up jingle horse, pick up your feet
Jingle around the clock
Mix and a-mingle in the jinglin' feet
That's the jingle bell
That's the jingle bell
That's the jingle bell rock
                    """,
                    """
                    Rockin' around the Christmas tree
At the Christmas party hop
Mistletoe hung where you can see
Every couple tries to stop
Rockin' around the Christmas tree
Let the Christmas spirit ring
Later we'll have some pumpkin pie
And we'll do some caroling
You will get a sentimental feeling when you hear
Voices singing, let's be jolly
Deck the halls with boughs of holly
Rockin' around the Christmas tree
Have a happy holiday
Everyone dancin' merrily
In the new old-fashioned way
You will get a sentimental feeling when you hear
Voices singing, let's be jolly
Deck the halls with boughs of holly
Rockin' around the Christmas tree
Have a happy holiday
Everyone dancin' merrily
In the new old-fashioned way
                    """,
                    """
                    Last Christmas
I gave you my heart
But the very next day you gave it away.
This year
To save me from tears
I'll give it to someone special.

Last Christmas
I gave you my heart
But the very next day you gave it away.
This year
To save me from tears
I'll give it to someone special.

Once bitten and twice shy
I keep my distance
But you still catch my eye.
Tell me, baby,
Do you recognize me?
Well,
It's been a year,
It doesn't surprise me
(Merry Christmas)

I wrapped it up and sent it
With a note saying, "I love you, "
I meant it
Now I know what a fool I've been.
But if you kissed me now
I know you'd fool me again.

Last Christmas
I gave you my heart
But the very next day you gave it away.
This year
To save me from tears
I'll give it to someone special.

Last Christmas
I gave you my heart
But the very next day you gave it away.
This year
To save me from tears
I'll give it to someone special.

Oh, oh, baby.

A crowded room,
Friends with tired eyes.
I'm hiding from you
And your soul of ice.
My god I thought you were someone to rely on.
Me? I guess I was a shoulder to cry on.

A face on a lover with a fire in his heart.
A man under cover but you tore me apart, ooh-hoo.
Now I've found a real love, you'll never fool me again.

Last Christmas
I gave you my heart
But the very next day you gave it away.
This year
To save me from tears
I'll give it to someone special.

Last Christmas
I gave you my heart
But the very next day you gave it away.
This year
To save me from tears
I'll give it to someone special.

A face on a lover with a fire in his heart (I gave you my heart)
A man under cover but you tore him apart
Maybe next year I'll give it to someone
I'll give it to someone special.
                    """,
                    """
                    Santa, tell me if you're really there
Don't make me fall in love again
If he won't be here next year
Santa, tell me if he really cares
'Cause I can't give it all away
If he won't be here next year
Feeling Christmas all around
And I'm trying to play it cool
But it's hard to focus when I see him walkin' 'cross the room
"Let it Snow" is blasting out
But I won't get in the mood
I'm avoiding every mistletoe until I know
It's true love that he thinks of
So next Christmas
I'm not all alone, boy
Santa, tell me if you're really there
Don't make me fall in love again
If he won't be here next year
Santa, tell me if he really cares
'Cause I can't give it all away
If he won't be here next year
I've been down this road before
Fell in love on Christmas night (ooh, babe)
But on New Year's Day, I woke up and he wasn't by my side
Now I need someone to hold
Be my fire in the cold (yeah, yeah)
But it's hard to tell if this is just a fling
Or if it's true love that he thinks of
So next Christmas
I'm not all alone, babe
Santa, tell me if you're really there
Don't make me fall in love again
If he won't be here next year
Santa, tell me if he really cares
'Cause I can't give it all away
If he won't be here next year
Oh, I wanna have him beside me like oh-oh-oh
On the 25th by that fire place, oh-oh-oh
But I don't want a new broken heart
This year I've got to be smart
Ooh, baby
(Santa, tell me, Santa, tell me)
If he will be, if he will be here (Santa, tell me, Santa, tell me)
Oh-oh-oh
Santa, tell me if you're really there (Santa, tell me, 'cause I really care)
Don't make me fall in love again
If he won't be here next year
Santa, tell me if he really cares (tell me, tell me, boy)
'Cause I can't give it all away
If he won't be here next year
Santa, tell me if you're really there (tell me, tell me, baby)
Don't make me fall in love again
If he won't be here next year (if he won't be, if he won't be here)
Santa, tell me if he really cares (tell me, do you care?)
'Cause I can't give it all away
If he won't be here next year
                    """,
                    """
                    It's the most wonderful time of the year
With the kids jingle belling
And everyone telling you be of good cheer
It's the most wonderful time of the year
It's the hap-happiest season of all
With those holiday greetings and gay happy meetings
When friends come to call
It's the hap-happiest season of all
There'll be parties for hosting
Marshmallows for toasting
And caroling out in the snow
There'll be scary ghost stories
And tales of the glories of
Christmases long, long ago
It's the most wonderful time of the year
There'll be much mistltoeing
And hearts will be glowing
When loved ones are near
It's the most wonderful time of the year
There'll be parties for hosting
Marshmallows for toasting
And caroling out in the snow
There'll be scary ghost stories
And tales of the glories of
Christmases long, long ago
It's the most wonderful time of the year
There'll be much mistltoeing
And hearts will be glowing
When loved ones are near
It's the most wonderful time
Yes the most wonderful time
Oh the most wonderful time
Of the year
                    """,
                    """
                    Have a holly jolly Christmas
It's the best time of the year
Now I don't know if there'll be snow
But have a cup of cheer
Have a holly jolly Christmas
And when you walk down the street
Say hello to friends you know
And everyone you meet
Oh-ho, the mistletoe
Is hung where you can see
Somebody waits for you
Kiss her once for me
Have a holly jolly Christmas
And in case you didn't hear
Oh, by golly
Have a holly jolly Christmas this year
Oh-ho, the mistletoe
Is hung where you can see
Somebody waits for you
Kiss her once for me
Have a holly jolly Christmas
And in case you didn't hear
Oh, by golly
Have a holly jolly Christmas this year
                    """,
                    """
                    Oh, the weather outside is frightful
But the fire is so delightful
And since we've no place to go
Let it snow, let it snow, let it snow
It doesn't show signs of stopping
And I've bought some corn for popping
The lights are turned way down low
Let it snow, let it snow, let it snow
When we finally kiss goodnight
How you'll hate going out in the storm
But if you really hold me tight
All the way home you'll be warm
The fire is slowly dying
And, dear, we're still goodbying
But as long as you love me so
Let it snow, let it snow, let it snow
But if you really hold me tight
All the way home you'll be warm
The fire is slowly dying
And, dear, we're still goodbying
But as long as you love me so
Let it snow, let it snow
                    """,
                    """
                    You're here where you should be
Snow is falling as the carolers sing
It just wasn't the same
Alone on Christmas day
Presents, what a beautiful sight
Don't mean a thing if you ain't holding me tight
You're all that I need
Underneath the tree

Tonight, I'm gonna hold you close
Make sure that you know
I was lost before you
Christmas was cold and grey
Another holiday
Alone to celebrate

But then, one day, everything changed
You're all I need
Underneath the tree

You're here where you should be
Snow is falling as the carolers sing
It just wasn't the same
Alone on Christmas day
Presents, what a beautiful sight
Don't mean a thing if you ain't holding me tight
You're all that I need
Underneath the tree

I found what I was looking for
A love that's meant for me
A heart that's mine completely
Knocked me right off my feet
And this year I will fall
With no worries at all

'Cause you are near and everything's clear
You're all I need
Underneath the tree

You're here where you should be
Snow is falling as the carolers sing
It just wasn't the same
Alone on Christmas day
Presents, what a beautiful sight
Don't mean a thing if you ain't holding me tight
You're all that I need
Underneath the tree

And then, one day, everything changed
You're all I need
Underneath the tree, yeah

You're here where you should be
Snow is falling as the carolers sing (Oh, yeah, yeah)
It just wasn't the same (Oh, yeah, yeah, yeah)
Alone on Christmas day
Presents, what a beautiful sight (Oh, you're all I need)
Don't mean a thing if you ain't holding me tight (Underneath my tree)
You're all that I need (Underneath my tree, yeah)
Underneath the tree, tonight

Oh, you're all I need
Underneath, underneath the tree
                    """,
                    """
                    I'm dreaming of a white Christmas
Just like the ones I used to know
Where the tree tops glisten
And children listen
To hear sleigh bells in the snow, oh, the snow
I said, I'm dreaming of a white Christmas
With every Christmas card I write
May your days be merry and bright
And may all your Christmas' be white
(Let's go, sticks, let's go)
I said, I'm dreaming of a white, oh, Christmas
Just like the ones I used to know
Where the tree tops glisten
And the children listen
To hear sleigh bells in the snow
I'm dreaming of a white Christmas
With every Christmas card I write
May your days, may your days, may your days
Be merry and bright
And may all your Christmas' be white
(Come on now, woo)
(J-man, up, up, up)
I'm dreaming of a white Christmas
With every Christmas card I write
May your days be merry and bright
And may all your Christmas' be white
                    """,
                    """
                    It's beginning to look a lot like Christmas
Everywhere you go
Take a look at the five and ten, it's glistening once again
With candy canes and silver lanes that glow
It's beginning to look a lot like Christmas
Toys in every store
But the prettiest sight to see is the holly that will be
On your own front door
A pair of Hopalong boots and a pistol that shoots
Is the wish of Barney and Ben
Dolls that'll talk and will go for a walk
Is the hope of Janice and Jen
And Mom and Dad can hardly wait for school to start again
It's beginning to look a lot like Christmas
Everywhere you go
There's a tree in the Grand Hotel, one in the park as well
It's the sturdy kind that doesn't mind the snow
It's beginning to look a lot like Christmas
Soon the bells will start
And the thing that'll make 'em ring is the carol that you sing
Right within your heart
It's beginning to look a lot like Christmas
Toys in every store
But the prettiest sight to see is the holly that will be
On your own front door
Sure, it's Christmas once more
                    """,
                    """
                    Have yourself a merry little Christmas
Let your heart be light
Next year all our troubles will be out of sight
Have yourself a merry little Christmas
Make the Yuletide gay
Next year all our troubles will be miles away
Once again, as in olden days
Happy golden days of yore
Faithful friends who are dear to us
Will be near to us once more
Someday soon, we all will be together
If the fates allow
Until then, we'll have to muddle through somehow
So have yourself a merry little Christmas now
                    """,
                    """
                    It was Christmas Eve babe
In the drunk tank
An old man said to me, won't see another one
And then he sang a song
The Rare Old Mountain Dew
I turned my face away
And dreamed about you
Got on a lucky one
Came in eighteen to one
I've got a feeling
This year's for me and you
So happy Christmas
I love you baby
I can see a better time
When all our dreams come true
They've got cars big as bars
They've got rivers of gold
But the wind goes right through you
It's no place for the old
When you first took my hand
On a cold Christmas Eve
You promised me
Broadway was waiting for me
You were handsome
You were pretty
Queen of New York City
When the band finished playing
They howled out for more
Sinatra was swinging
All the drunks they were singing
We kissed on a corner
Then danced through the night
The boys of the NYPD choir
Were singing Galway Bay
And the bells were ringing out
For Christmas day
You're a bum
You're a punk
You're an old slut on junk
Lying there almost dead on a drip in that bed
You scumbag, you maggot
You cheap lousy faggot
Happy Christmas your arse
I pray God it's our last
The boys of the NYPD choir
Still singing Galway Bay
And the bells are ringing out
For Christmas day
I could have been someone
Well so could anyone
You took my dreams from me
When I first found you
I kept them with me babe
I put them with my own
Can't make it all alone
I've built my dreams around you
The boys of the NYPD choir
Still singing Galway Bay
And the bells are ringing out
For Christmas day
                    """,
                    """
                    I really can't stay
Baby, it's cold outside
I've got to go away
Baby, it's cold outside
This evening has been
Hoping that you'd drop in
So, very nice
I'll hold your hands, they're just like ice
My mother will start to worry
Beautiful, what's your hurry?
My father will be pacing the floor
Listen to that fireplace roar
So, really I'd better scurry
Beautiful, please don't hurry
But maybe just a hald a drink more
I'll put some records on while I pour
The neighbors might think
Baby, it's bad out there
Say, what's in this drink?
No cabs to be had out there
I wish I knew how
Your eyes are like starlight now
To break this spell
I'll take your hat, your hair looks swell
I ought to say, "No, no, no sir"
Mind if I move in closer?
At least I'm gonna say that I tried
What's the sense in hurting my pride?
I really can't stay
Baby, don't hold out
Baby, it's cold outside
Ugh, you're very pushy, you know?
I'd like to think of it as opportunistic
I simply must go
Baby, it's cold outside
The answer is, "No"
But, baby, it's cold outside
The welcome has been
How lucky that you dropped in
So nice and warm
Look out the window at that storm
My sister will be suspicious
Gosh, your lips look delicious
My brother will be there at the door
Waves upon a tropical shore
My maiden aunt's mind is vicious
Gosh, your lips are delicious
But maybe just cigarette more
Never such a blizzard before
I've got to get home
Baby, you'll freeze out there
Say, lend me your comb?
It's up to your knees out there
You've really been grand
I thrill when I touch your hand
But don't you see?
How can you do this thing to me?
There's bound to be talk tomorrow
Think of my life-long sorrow
At least there will be plenty implied
If you got pneumonia and died
I really can't stay
Get over that hold out
Baby, it's cold
Baby, it's cold outside
Okay, fine, just another drink
That took a lot of convincing
                    """,
                    """
                    Snow is fallin'
All around me
Children playin'
Having fun
It's the season
Love and understanding
Merry Christmas everyone
Time for parties and celebrations
People dancing all night long
Time for presents
And exchanging kisses
Time for singing Christmas songs
We're gonna have a party tonight
I'm gonna find that girl underneath the misteltoe
We'll kiss by candlelight
Room is swaying, records playing
All the old songs we love to hear
All I wish that everyday was Christmas
What a nice way to spend the year (woo, yeah)
We're gonna have a party tonight
I'm gonna find that girl underneath the mistletoe
We'll kiss by candlelight
Snow is fallin' (snow is fallin')
All around me (all around me)
Children playin' (children playin')
Having fun (having fun)
It's the season
Love and understanding
Merry Christmas everyone
Merry Christmas everyone
Ooh, merry Christmas everyone
Snow is fallin' (snow is fallin')
All around me (all around me)
Children playin' (children playin')
Having fun (having fun)
It's the season
Love and understanding
Merry Christmas everyone
Snow is fallin' (snow is fallin')
All around me (all around me)
Children playin' (children playin')
Having fun (having fun)
It's the season
Love and understanding
Merry Christmas everyone
Oh snow is fallin' (snow is fallin')
All around me (all around me)
Children playin' (children playin')
Having fun (having fun)
It's the season
Love and understanding
Merry Christmas everyone
Merry Christmas everyone
Ooh merry Christmas everyone
                    """,
                    """
                    It's Christmas time, and there's no need to be afraid
At Christmas time, we let in light and banish shade
And in our world of plenty
We can spread a smile of joy
Throw your arms around the world
At Christmas time
But say a prayer and pray for the other ones
At Christmas time, it's hard but while you're having fun
There's a world outside your window
And it's a world of dread and fear
Where a kiss of love can kill you
And there's death in every tear
And the Christmas bells that ring there are the clanging chimes of doom
Well tonight we're reaching out and touching you
Bring peace and joy this Christmas to West Africa
A song of hope they'll have is being alive
Why is comfort deadly fear
Why is to touch to be scared
How can they know it's Christmas time at all
Here's to you
Raise a glass to everyone
Here's to them
And all their years to come
Can they know it's Christmas time at all
Feed the world, let them know it's Christmas time again
Feed the world, let them know it's Christmas time again
Heal the world, let them know it's Christmas time again
Feed the world, let them know it's Christmas time again
Heal the world, let them know it's Christmas time again
Heal the world, let them know it's Christmas time again
Feed the world, let them know it's Christmas time again
Heal the world, let them know it's Christmas time again
Heal the world
                    """]
                    
#%% AI lyrics list

ai_lyrics_list = ["""
                  Snowflakes fall, and the city glows
The kind of warmth only December knows
We’re wrapped in scarves, hearts open wide
Lost in the magic, with you by my side

Under the Christmas lights, the world feels bright
Everything's golden in your arms tonight
The snow keeps falling, but we’re burning inside
Under the Christmas lights, love is alive

Carols echo from down the street
Footsteps crunching beneath our feet
Hot cocoa steam, and a frozen kiss
A winter moment I'll never miss

Under the Christmas lights, the world feels bright
Everything’s golden in your arms tonight
The snow keeps falling, but we’re burning inside
Under the Christmas lights, love is alive

This season comes and it fades too fast
But I know our love is built to last
Every shining bulb, every snowy flight
I'll remember you under the Christmas lights

Under the Christmas lights, the world feels bright
Everything’s golden in your arms tonight
The snow keeps falling, but we're burning inside
Under the Christmas lights, love is alive
                """,
                """
                Silent streets, where the cold winds sing
December carries a peaceful sting
Frozen branches, their diamonds gleam
Every snowflake dances, chasing a dream

Hear the snowflake serenade, soft and true
A melody crafted just for me and you
Each note whispers through the frosty air
Bringing moments only love can share

Icicles form on the rooftops near
Chiming softly, a song you hear
The winter choir, its voice so high
A thousand stars light the velvet sky

Hear the snowflake serenade, soft and true
A melody crafted just for me and you
Each note whispers through the frosty air
Bringing moments only love can share

As the snow falls, the world turns still
Hearts are warmed by winter's will
Hold me closer, we're wrapped in fate
Lost in this snowy serenade

Hear the snowflake serenade, soft and true
A melody crafted just for me and you
Each note whispers through the frosty air
Bringing moments only love can share
                """,
                """
                I don't need diamonds, I don't need gold
I've got the only gift I'll ever hold
The snow is falling, but I'm feeling warm
This Christmas love is my perfect storm

Every ribbon, every bow
Can't compare to the love we know
Under the tree, there's nothing I need
When your heart is the only gift I see

I'm wrapped in your love, it's all I want tonight
Your arms around me in the soft firelight
The world outside can freeze, but we're burning bright
I'm wrapped in your love, and it feels so right

The stockings hang, the carols play
But all of that fades when you look my way
The mistletoe knows we've got something real
This holiday magic's the way you make me feel

I'm wrapped in your love, it’s all I want tonight
Your arms around me in the soft firelight
The world outside can freeze, but we're burning bright
I'm wrapped in your love, and it feels so right

We could make this moment last
Hold on tight, don't let it pass
Every day could feel like this
Forever sealed with a Christmas kiss

I'm wrapped in your love, it's all I want tonight
Your arms around me in the soft firelight
The world outside can freeze, but we're burning bright
I'm wrapped in your love, and it feels so right
                """,
                """
                Frosty windows, I hear that sound
A Christmas classic spinning 'round
The melody fills the chilly air
Takes me back to a time we shared

It's magic on the radio
A song of love wrapped in winter's glow
Every verse, every rhyme
Brings me back to Christmastime

Driving slow through the city lights
Snowflakes twirl like stars tonight
The DJ says, “Now here's a hit”
The song starts playing, and I'm lost in it

It's magic on the radio
A song of love wrapped in winter's glow
Every verse, every rhyme
Brings me back to Christmastime

I remember us dancing, just you and me
To a Christmas tune under the tallest tree
The words are simple, the feeling's grand
As we spin together, hand in hand

It's magic on the radio
A song of love wrapped in winter's glow
Every verse, every rhyme
Brings me back to Christmastime

So play it again, let the memories flow
It's more than a song, it's the love I know
Forever a part of the holidays
This tune's the soundtrack of Christmas Day
                """,
                """
                Lights are up, snow's coming down
Shoppers rushing all through the town
But I've got something else on my mind
Counting the days 'til your heart is mine

Five days to Christmas, and all I see
Is your smile lighting up the tree
Four days to go, I'm holding on tight
To the thought of your kiss on Christmas night

Three days to Christmas, I can't sleep
You're the only present I want to keep
Two days left, it's almost here
The best gift of all is having you near

One more night, and you're finally home
No more wishing under the phone
The countdown's over, love's in the air
This Christmas, I'll show you how much I care

No more waiting, the moment's here
A season of magic, and you appear
Forever wrapped in holiday cheer
This Christmas countdown led me to you, my dear
                """,
                """
                The frost paints the windows, the streets are white
Everywhere I look, it feels so right
But the only thing missing is you tonight
So I'm hoping you'll meet me in December's light

Meet me where the snowflakes kiss the ground
Where love feels like the only sound
I'll wait for you by the old town square
Just meet me in December, I'll be there

The clock strikes twelve, the bells will ring
We'll dance to the melody the carolers sing
The world is quiet, but my heart is loud
When I'm with you, lost in the crowd

Meet me where the snowflakes kiss the ground
Where love feels like the only sound
I'll wait for you by the old town square
Just meet me in December, I'll be there

The year may end, but love will stay
If we start forever on Christmas Day
Take my hand, let's make it true
Every December, I'll meet you

Meet me where the snowflakes kiss the ground
Where love feels like the only sound
I'll wait for you by the old town square
Just meet me in December, I'll be there
                """,
                """
                The tinsel's hanging on the tree
But it feels so empty without you here with me
The lights are shining, the fire glows
But this Christmas feels colder than the snow

I smile for the pictures, but my heart aches
It's a holiday season I just can’t fake
Every ornament's a memory of years gone by
Tinsel and tears, I can’t help but cry

They say this season is meant for joy
For laughing, for loving, for every girl and boy
But tonight, I'm wishing on a falling star
That wherever you are, you're not too far

I smile for the pictures, but my heart aches
It's a holiday season I just can't fake
Every ornament's a memory of years gone by
Tinsel and tears, I can't help but cry

I'll hang my hope on the mistletoe
Dreaming of a love that'll one day grow
But for now, I'll toast to what we had
And make this Christmas the best of the bad

I smile for the pictures, but my heart aches
It's a holiday season I just can’t fake
Every ornament's a memory of years gone by
Tinsel and tears, I can't help but cry
                """,
                """
                I hear the jingle of sleigh bells near
And I know this ride will bring you here
The frost in the air, the moon shining bright
A sleigh ride to forever starts tonight

Hold on tight, the reins are gold
This love is the story I want told
Through snowy fields and evergreen skies
This sleigh ride to forever never dies

Your laughter's warm, it melts the cold
The kind of magic that never grows old
The stars above light the way
As we ride through a perfect holiday

Hold on tight, the reins are gold
This love is the story I want told
Through snowy fields and evergreen skies
This sleigh ride to forever never dies

When the sleigh ride ends, and the snow clears away
I'll still be here, every Christmas Day
No matter the season, no matter the weather
We'll always have this sleigh ride to forever
                """,
                """
                Crowds are rushing, lights are bright
The air is sparkling, a perfect night
But all I see is you standing there
Under the mistletoe, beyond compare

Kiss me under the mistletoe glow
Where our love lights the world below
In this holiday haze, let it be known
You're the only gift I've ever known

The choir's singing, the bells ring clear
But nothing else matters when you're near
The snow falls softly, but my heart beats loud
Under the mistletoe, lost in the crowd

Kiss me under the mistletoe glow
Where our love lights the world below
In this holiday haze, let it be known
You're the only gift I've ever known

Through every winter, I'll meet you there
With your lips on mine, we'll chase the air
The years may pass, the seasons flow
But I'll always find you in the mistletoe glow
                """,
                """
                Wake up slow, the world's a dream
Snow outside, it's a winter scene
Stockings hang, the fire's warm
A Christmas morning, the perfect storm

Christmas morning magic, it's all we need
With your love, my heart's guaranteed
Presents wrapped in paper and bows
But the real gift is the love we've chosen

The smell of cinnamon in the air
The soft glow of lights everywhere
But nothing shines brighter than the way you do
This Christmas morning belongs to you

Christmas morning magic, it's all we need
With your love, my heart's guaranteed
Presents wrapped in paper and bows
But the real gift is the love we've chosen

As the day fades into twilight's hue
I'm still grateful for every part of you
This season's joy will come and go
But this love is the only thing I know
                """,
                """
                It falls so soft, a quiet scene
A blanket of white where the world's serene
We step outside, the night feels right
The first snow of Christmas is pure delight

Under the sky, we make our mark
Snow angels glowing in the dark
Each flake whispers a promise true
Of Christmas magic, me and you

The first snow of Christmas, it's more than cold
It's the story of love waiting to be told
Every step we take leaves a trace
A winter wonderland, our sacred space

The stars shine bright, the world's asleep
But in your arms, my heart takes a leap
With every snowflake that falls so free
This first snow feels like destiny

The first snow of Christmas, it's more than cold
It's the story of love waiting to be told
Every step we take leaves a trace
A winter wonderland, our sacred space
                """,
                """
                The gifts are wrapped, the halls are decked
The tree is glowing, what's left to perfect?
The carols play, the world's so bright
But all I want is Christmas night

Just you and me, the fire's low
Holding on while the embers glow
The world outside can keep its cheer
As long as I’ve got you right here

All I want is Christmas night
Your love shining like the candlelight
The snow can fall, the stars can shine
But nothing compares to calling you mine

The holidays come, they fly away
But my love for you is here to stay
Let's make this moment last forever
This Christmas night, we’re better together

All I want is Christmas night
Your love shining like the candlelight
The snow can fall, the stars can shine
But nothing compares to calling you mine
                """,
                """
                I can feel it in the air tonight
The way the world sparkles in winter's light
There's joy in the streets, there's hope in our eyes
A season of wonder under December skies

Christmas in the air, it's everywhere
A melody of magic we can't compare
From the city lights to the forest pine
Christmas in the air, and it's yours and mine

Every heart beats to the same song
A rhythm of love that's been here all along
The bells are ringing, the choirs sing loud
Christmas unites us, we’re part of the crowd

Christmas in the air, it's everywhere
A melody of magic we can't compare
From the city lights to the forest pine
Christmas in the air, and it's yours and mine

So take my hand, let's make this true
This holiday season starts with you
Together we'll shine like the brightest star
Christmas in the air is who we are
                """,
                """
                The tree's decorated, the table's set
The kind of season you don’t forget
But nothing here feels quite the same
Without your smile to light the flame

Just one more Christmas with you
To feel the love that we once knew
No gift could ever take your place
I just want to see your face

The lights are twinkling, the fire's bright
But my heart's missing its guiding light
Every carol, every tune
Takes me back to Christmases with you

Just one more Christmas with you
To feel the love that we once knew
No gift could ever take your place
I just want to see your face

If wishes worked like snowflakes do
I'd gather a blizzard to bring me you
So here I stand, beneath the tree
Hoping your love will come back to me
                """,
                """
                The cold wind blows, the night feels long
But your love is my compass, keeps me strong
Through every storm, through every chill
Your heart is my North Star, guiding still

North Star Christmas, you light my way
Through the darkest night, to a brighter day
No matter where this season finds me
Your love's the star I'll always see

The candles flicker, the frost takes hold
But your warmth is the story I've always told
Through every year, through every fight
Your love is the reason I shine so bright

North Star Christmas, you light my way
Through the darkest night, to a brighter day
No matter where this season finds me
Your love's the star I'll always see

Forever shining in the midnight blue
My North Star, I'll follow you
Across the seasons, through the years
Your love melts away my fears
                """,
                """
                The wreaths are hung, the stockings too
And here I am, thinking of you
Last year was hard, we drifted away
But something tells me it's Christmas today

It's gonna be Christmas again
Love will find a way to mend
The sleigh bells ring, our hearts will sing
It's gonna be Christmas again

The snow is fresh, the past feels far
Like a candle relit, or a shining star
Let's start anew, just me and you
This Christmas feels like a dream come true

It's gonna be Christmas again
Love will find a way to mend
The sleigh bells ring, our hearts will sing
It's gonna be Christmas again

No matter the miles, no matter the tears
The spirit of Christmas draws us near
I see it now, the magic is clear
This is our time, this is our year
                """]
#%% Add to data frames

common_words_df = pd.DataFrame(columns = ["word", "count"])

for song in xmas_lyrics_list:
    song_words_df = pd.DataFrame(find_common_words(song, 10), columns = ["word", "count"])
    common_words_df = pd.concat([common_words_df, song_words_df])

real_grouped_words = common_words_df.groupby("word").sum().reset_index().sort_values("count", ascending = False)


real_grouped_words["word_density"] = real_grouped_words["count"] / len(xmas_lyrics_list)


ai_common_words_df = pd.DataFrame(columns = ["word", "count"])

for song in ai_lyrics_list:
    song_words_df = pd.DataFrame(find_common_words(song, 10), columns = ["word", "count"])
    ai_common_words_df = pd.concat([ai_common_words_df, song_words_df])

ai_grouped_words = ai_common_words_df.groupby("word").sum().reset_index().sort_values("count", ascending = False)


ai_grouped_words["word_density"] = ai_grouped_words["count"] / len(ai_lyrics_list)

#%% Extract top 5 & make barchart

top_5_ai = ai_grouped_words.word[:5]
top_5_real = real_grouped_words.word[:5]

top_words = pd.concat([top_5_ai, top_5_real]).unique()

graph_data = pd.DataFrame({"word": top_words})

graph_data["ai"] = graph_data["word"].map(dict(zip(ai_grouped_words.word, ai_grouped_words.word_density))).fillna(0)
graph_data["real"] = graph_data["word"].map(dict(zip(real_grouped_words.word, real_grouped_words.word_density))).fillna(0)


#%% Plot
x = range(len(graph_data))
width = 0.4

plt.bar([p - width/2 for p in x], graph_data.ai, width, label='AI')
plt.bar([p + width/2 for p in x], graph_data.real, width, label='Real')

plt.xticks(x, graph_data['word'], rotation=45, ha='right')
plt.xlabel('Common Words')
plt.ylabel('Word Density')
plt.title('Average Words per Song')
plt.legend()
plt.tight_layout()
