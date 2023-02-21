
###################     How the program should work    ########################
# You have been provided with three variables with Einstein in ASCII!
# In one he's Thrilled, on the other he's Sad and on the last he's indifferent/confused.
# In the terminal, make Einsten Thrilled with the right(True) math, sad with the (False) math, and indifferent when the user type anything else than True or False.
# NOTE: The input must accept capitals, lowercase or uppercase on the user answers.
# Example:
# 1 + 1 = 3 | Is that "True" or "False"? Your answer: True
# False 
#
#          -''--.
#          _`>   `\.-'<
#       _.'     _     '._
#     .'   _.‾'   '‾._   '.
#    /      / / -- \      \
#     >_   / _/\ /\_ \   _<
#       / (  \_/ \_/  ) \
#       >._\  ` _) ` /_.<
#           /__/ \__\
#             | ⁀ |
#              ‾‾‾‾
#
###########################################
# --------------------------------------
# TEXT CASE: TRUE
#
# Output-------------------
# 1 + 1 = 3 | Is that "True" or "False"? Your answer: TRUE
# False 
#
#          -''--.
#          _`>   `\.-'<
#       _.'     _     '._
#     .'   _.‾'   '‾._   '.
#    /      / / -- \      \
#     >_   / _/\ /\_ \   _<
#       / (  \_/ \_/  ) \
#       >._\  ` _) ` /_.<
#           /__/ \__\
#             | ⁀ |
#              ‾‾‾‾
# --------------------------------------
# TEXT CASE: False
#
# Output-------------------
# 1 + 1 = 3 | Is that "True" or "False"? Your answer: falSE
# False 
#          -''--.
#          _`>   `\.-'<
#       _.'     _     '._
#     .'   _.‾'   '‾._   '.
#    /      / ==‾== \      \
#     >_   / / \ / \ \   _<
#       / (  \o/\o/  ) \
#       >._\ .- _)-. /_.<
#           /__/ \__\
#             | O |
#             '---'
# --------------------------------------
# TEXT CASE: 111
#
# Output-------------------
# 1 + 1 = 3 | Is that "True" or "False"? Your answer: 111
# False 
#          -''--.
#          _`>   `\.-'<  ???
#       _.'     _     '._
#     .'   _.‾'   '‾._   '.
#     >_   / /_\/_\  \   _<
#       / (  \o/\o/   ) \
#       >._\ .-,_)-. /_.<
#           /__/ \__\
#             '---'



einsteinThrilled = """

         -''--.
         _`>   `\.-'<
      _.'     _     '._
    .'   _.‾'   '‾._   '.
   /      / ==‾== \      \\
    >_   / / \ / \ \   _<
      / (  \o/\\o/  ) \\
      >._\ .- _)-. /_.<
          /__/ \__\\
            | O |
            '---'   
"""

einsteinSad = """

         -''--.
         _`>   `\.-'<
      _.'     _     '._
    .'   _.‾'   '‾._   '.
   /      / / -- \\      \\
    >_   / _/\ /\_ \   _<
      / (  \_/ \_/  ) \\
      >._\  ` _) ` /_.<
          /__/ \__\\
            | ⁀ |
             ‾‾‾‾
"""

einstein = """
         -''--.
         _`>   `\.-'<  ???
      _.'     _     '._
    .'   _.‾'   '‾._   '.
    >_   / /_\/_\  \   _<
      / (  \o/\o/   ) \\
      >._\ .-,_)-. /_.<
          /__/ \__\\
            '---'
"""


######### Start coding here ###############

from re import ASCII


# ANSWER
def main ():
    question1 = False
    answer = input('1 + 1 = 3 | Is that "True" or "False"? Your answer: ').lower()

    if answer == "false":
        print(question1, einsteinThrilled)
    elif answer == "true":
        print(question1, einsteinSad)
    else:
        print(question1, einstein)
main()