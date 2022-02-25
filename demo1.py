#		python code
#		script_name: demo1
#
#		author: sarea
#         
#       Set Up Part
from earsketch import *

init()
setTempo(90)     # how fast or slow you want the song to be played 
                 # a temple was translated of beats per minute and 
                 # can range from 45 to 220

#       Music Part 

drumbeat = COMMON_LOVE_DRUMBEAT_1
bkup = AK_UNDOG_VOCAL_BKUP_1
vocalsChorus = AK_UNDOG_LEAD_VOCALS_CHORUS
drums = RD_ROCK_POPRHYTHM_MAINDRUMS_2
bass = DKBEAR_FREE_THEME_BASS

fitMedia(drumbeat, 1, 1, 12)
setEffect(2, DELAY, DELAY_TIME, 1000)
fitMedia(AK_UNDOG_OOHS_4, 2, 1, 3)

fitMedia(bkup, 3, 4, 11)
fitMedia(AK_UNDOG_CLAPS_SNAPS_5, 2, 3, 8)
fitMedia(vocalsChorus, 4, 3, 12)

fitMedia(drums, 5, 5, 11)
fitMedia(bass, 6, 1, 3)
setEffect(6, DELAY, DELAY_TIME, 1000)


#       Finish Part
finish()
