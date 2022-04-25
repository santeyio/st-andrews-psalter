# What is this?

I have a PDF version of the plams that I copied into the `all_psalms` file. I wasn't able to figure out how to get the underlines from the PDF into text so that I can display them within the app programmatically, so I opted to write a script (`convert.py`) to aid me in going through the `all_psalms` file and adding the underlines for indicating how the line is to be chanted, as well as to get them into a format and data structure that can be utilized by the vue app. 

I break the psalms down so that each psalm is contained in it's own file in the `out` directory. There is a script `out/_to_json.py` which will parse all of the files in the `out` directory into a single json object so that it can be used in the frontend.

as I go through the `all_psalms` file and convert the psalms into the necessary format for the app I store the line number I am on in the `saved_place` file and the number of the psalm I am currently on in the `psalm_num` file. The `convert.py` script uses the numbers stored in these files to keep track of where I am in processing the `all_psalms` file.

# How to use convert.py

Simply run `python convert.py` and a script will start running. It will print out the line that you are on in the `all_psalms` file. You should input the letters that should be underlined (in order to figure this out you need to have the St Andrews Psalter PDF open and will need to look at what letters are underlined and type them in).

Occasionally in the PDF you will find a line that should be indented. In this case just enter two spaces before the characters that should be underlined

Sometimes only a single vowel or a consonant and a vowl (e.g. 'in') will be underlined, and the script will not be able to determine what to underline because the input occurs multiple times. In this case an error will be printed out which you should note and go back and manually change in the file.

# Notes to go back and correct later:

Psalm 68 switches tones halfway through
Psalm 78 switches tones halfway through (at verse 57)

## Temp Notes:

- 
