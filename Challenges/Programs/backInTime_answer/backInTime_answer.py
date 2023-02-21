###################     How the program should work    ########################
# Show the current time together with the date but from one year ago, you must use "datetime" import from Python (already provided).
# Show EXACTLY the text below, with current time and date from one year ago in terminal.
# NOTE: The date and time needs to be dynamic (hardcode is not allowed).
# Example: 
#
# At this time one year ago 12:58:49 of 2021-12-02 I was NOT doing CODEFLEX! WOW! Look where I am now =)
# --------------------------------------

# TEXT CASE
#
# At this time one year ago 12:58:49 of 2021-12-02 I was NOT doing CODEFLEX! WOW! Look where I am now =)


######### Start coding here ###############

from datetime import datetime, date, timedelta


def main ():
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    today = date.today()
    oneYearAgo = timedelta(days=365)
    oneYearAgoDate = today - oneYearAgo
    textEnd = "I was NOT doing CODEFLEX! WOW! Look where I am now =)"

    print("At this time one year ago", currentTime, "of" ,oneYearAgoDate, textEnd)
main()
