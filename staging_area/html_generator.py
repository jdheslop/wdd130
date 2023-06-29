
import os
import csv

# For the file_names list
FILE_NAME_INDEX = 0
TITLE_INDEX = 1
DESCRIPTION_INDEX = 2
SUB_FILE_NAME_INDEX = 3


def main():

    #NEED TO FINISH FIXING THIS - COMPARE IT WITH THE ORIGINAL FILE
    # Generate Main Clothing Page
    clothing_page = ["ks/us/clothing.html", "The Kleider Schrank - Clothing", "Clothing"]
        
    file_name = clothing_page[FILE_NAME_INDEX]
    html_title = clothing_page[TITLE_INDEX]
    description = clothing_page[DESCRIPTION_INDEX]

    delete_old_file(file_name)

    generate_head(file_name, html_title)

    generate_secondary_header(file_name)

    generate_introduction(file_name)

    generate_main_categories(file_name, clothing_page)

    generate_werbung(file_name)

    generate_footer(file_name)


    # Generate Main Category Pages
    file_names = [
        ["ks/us/clothing-women.html", "The Kleider Schrank - Clothing", "Women", "files_for_python/women_file_names.csv"], 
        ["ks/us/clothing-men.html", "The Kleider Schrank - Clothing", "Men", "files_for_python/men_file_names.csv"], 
        ["ks/us/clothing-girls.html", "The Kleider Schrank - Clothing", "Girls", "files_for_python/girls_file_names.csv"], 
        ["ks/us/clothing-boys.html", "The Kleider Schrank - Clothing", "Boys", "files_for_python/boys_file_names.csv"]
    ]

    for file in file_names:
        file_name = file[FILE_NAME_INDEX]
        html_title = file[TITLE_INDEX]
        description = file[DESCRIPTION_INDEX]
        sub_text_file_name = file[SUB_FILE_NAME_INDEX]

        sub_file_names = []

        # CHANGE THIS TO A FUNCTION
        # Create women_file_names list
        with open (sub_text_file_name, mode="rt") as csv_file:
            csv_rows = csv.reader(csv_file)
            sub_file_names = list(csv_rows)

        delete_old_file(file_name)

        generate_head(file_name, html_title)

        generate_secondary_header(file_name)

        generate_introduction(file_name)

        generate_main_categories(file_name, file_names)

        generate_sub_categories(file_name, sub_file_names)

        generate_werbung(file_name)

        generate_footer(file_name)


def generate_werbung(file_name):

    line_01 = '            <div class="werbung">'
    line_02 = '                <img src="../images/werbung.png" alt="">'
    line_03 = '            </div>'

    with open(file_name, "at") as html_file:
        print(line_01, file=html_file)
        print(line_02, file=html_file)
        print(line_03, file=html_file)


def generate_sub_categories(file_name, sub_file_names):
    with open(file_name, "at") as html_file:

        line_01 = '            <div class="subClothingCategories" >'
        print(line_01, file=html_file)

        generate_category_line(file_name, html_file, sub_file_names)

        line_02 = '            </div>'
        line_03 = ''
    
        print(line_02, file=html_file)
        print(line_03, file=html_file)



def generate_main_categories(file_name, file_names):
    with open(file_name, "at") as html_file:    
        line_01 = '            <div class="clothingCategories" >'
        print(line_01, file=html_file)

        generate_category_line(file_name, html_file, file_names)

        line_02 = '                <hr>'
        line_03 = '            </div>'
        line_04 = ''

        print(line_02, file=html_file)
        print(line_03, file=html_file)
        print(line_04, file=html_file)


def generate_category_line(file_name, html_file, file_names):
        
        for file in file_names:
            href = get_href(file)
            description = file[DESCRIPTION_INDEX]

            if file_name == file[FILE_NAME_INDEX]:
                line = f'                <a class="category selectedCategory" href="{href}">{description}</a>'
            else:
                line = f'                <a class="category notSelectedCategory" href="{href}">{description}</a>'

            print(line, file=html_file)

def get_href(file):
                href = file[FILE_NAME_INDEX].split("/")
                index = len(href) - 1
                href = href[index]
                return href


def delete_old_file(file_name):
    "This function checks if the file name exists already and then erases it"
    if os.path.exists(file_name):
        os.remove(file_name)


def generate_head(file_name, html_title):
    line_01 = '<!DOCTYPE html>'
    line_02 = '<html lang="en">'
    line_03 = '<head>'
    line_04 = '    <meta charset="UTF-8">'
    line_05 = '    <meta name="viewport" content="width=device-width, initial-scale=1.0">'
    line_06 = '    <link rel="stylesheet" href="../styles/styles.css">'
    line_07 = f'    <title>{html_title}</title>'
    line_08 = '    <link rel="icon" type="image/x-icon" href="../images/logo.png">'
    line_09 = '</head>'
    line_10 = '<body>'
    line_11 = '    <div id="content">'
    line_12 = ''

    with open(file_name, "at") as html_file:
        print(line_01, file=html_file)
        print(line_02, file=html_file)
        print(line_03, file=html_file)
        print(line_04, file=html_file)
        print(line_05, file=html_file)
        print(line_06, file=html_file)
        print(line_07, file=html_file)
        print(line_08, file=html_file)
        print(line_09, file=html_file)
        print(line_10, file=html_file)
        print(line_11, file=html_file)
        print(line_12, file=html_file)


def generate_secondary_header(file_name):
   
    line_01 = '        <header>'
    line_02 = '            <div id="headerBox">'
    line_03 = '                <a class="logoLink" href="../us/intro.html">'
    line_04 = '                    <img class="logo" src="../images/logo.png" alt="The Kleider Schrank Logo">'
    line_05 = '                </a>'
    line_06 = '                <div class="headerMsg">'
    line_07 = '                    <h2>The Kleider Schrank</h2>'
    line_08 = '                    <h3>Define Your Style - A Fashion Creation for Every Situation</h3>'
    line_09 = '                </div>'
    line_10 = '            </div>'
    line_11 = '            <div id="stickIt">'
    line_12 = '                <nav>'
    line_13 = '                    <a href="themes.html">My Theme</a>'
    line_14 = '                    <a href="clothing.html">Clothing</a>'
    line_15 = '                    <a href="wardrobe.html">Wardrobe</a>'
    line_16 = '                </nav>'
    line_17 = '            </div>'
    line_18 = '        </header>'
    line_19 = ''
    
    with open(file_name, "at") as html_file:
        print(line_01, file=html_file)
        print(line_02, file=html_file)
        print(line_03, file=html_file)
        print(line_04, file=html_file)
        print(line_05, file=html_file)
        print(line_06, file=html_file)
        print(line_07, file=html_file)
        print(line_08, file=html_file)
        print(line_09, file=html_file)
        print(line_10, file=html_file)
        print(line_11, file=html_file)
        print(line_12, file=html_file)
        print(line_13, file=html_file)
        print(line_14, file=html_file)
        print(line_15, file=html_file)
        print(line_16, file=html_file)
        print(line_17, file=html_file)
        print(line_18, file=html_file)
        print(line_19, file=html_file)


def generate_introduction(file_name):

    line_01 = '        <main>'
    line_02 = '            <h2 id="themeBox">YOUR THEME</h2>'
    line_03 = '            <div class="productIntro">'
    line_04 = '                <h3>Clothing and Accessories</h3>'
    line_05 = '                <p>Select from the clothing and accessories categories to narrow down your search for items you would like to add to your Wardrobe. When you are finished with your intitial selection, go to your Wardrobe to select the perfect outfit.</p>'
    line_06 = '            </div>'
    line_07 = ''

    with open(file_name, "at") as html_file:
        print(line_01, file=html_file)
        print(line_02, file=html_file)
        print(line_03, file=html_file)
        print(line_04, file=html_file)
        print(line_05, file=html_file)
        print(line_06, file=html_file)
        print(line_07, file=html_file)


def generate_footer(file_name):

    line_01 = '        </main>'
    line_02 = ''
    line_03 = '        <footer>'
    line_04 = '            <a class="logoLink" href="../us/intro.html">'
    line_05 = '                <img class="logo" src="../images/logo.png" alt="The Kleider Schrank Logo">'
    line_06 = '            </a>'
    line_07 = '            <div class="footerText">'
    line_08 = '                <p>The Kleider Schrank &copy; 2023 - Jackson Heslop</p>'
    line_09 = '            </div>'
    line_10 = '            <div class="footerLinks">'
    line_11 = '                <a href="imprint.html">Imprint</a>'
    line_12 = '                <a href="privacy.html">Privacy</a>'
    line_13 = '            </div>'
    line_14 = '        </footer>'
    line_15 = ''
    line_16 = '    </div>'
    line_17 = '    <script src="../scripts/main.js"></script>'
    line_18 = '</body>'
    line_19 = '</html>'

    with open(file_name, "at") as html_file:
        print(line_01, file=html_file)
        print(line_02, file=html_file)
        print(line_03, file=html_file)
        print(line_04, file=html_file)
        print(line_05, file=html_file)
        print(line_06, file=html_file)
        print(line_07, file=html_file)
        print(line_08, file=html_file)
        print(line_09, file=html_file)
        print(line_10, file=html_file)
        print(line_11, file=html_file)
        print(line_12, file=html_file)
        print(line_13, file=html_file)
        print(line_14, file=html_file)
        print(line_15, file=html_file)
        print(line_16, file=html_file)
        print(line_17, file=html_file)
        print(line_18, file=html_file)
        print(line_19, file=html_file)




if __name__ == "__main__":
    print()
    main()
    print()



""" VORLAGE:
    line_01 = ''
    line_02 = ''
    line_03 = ''
    line_04 = ''
    line_05 = ''
    line_06 = ''
    line_07 = ''
    line_08 = ''
    line_09 = ''
    line_10 = ''
    line_11 = ''
    line_12 = ''
    line_13 = ''
    line_14 = ''
    line_15 = ''
    line_16 = ''
    line_17 = ''
    line_18 = ''
    line_19 = ''
    line_20 = ''

    with open(file_name, "at") as html_file:
        print(line_01, file=html_file)
        print(line_02, file=html_file)
        print(line_03, file=html_file)
        print(line_04, file=html_file)
        print(line_05, file=html_file)
        print(line_06, file=html_file)
        print(line_07, file=html_file)
        print(line_08, file=html_file)
        print(line_09, file=html_file)
        print(line_10, file=html_file)
        print(line_11, file=html_file)
        print(line_12, file=html_file)
        print(line_13, file=html_file)
        print(line_14, file=html_file)
        print(line_15, file=html_file)
        print(line_16, file=html_file)
        print(line_17, file=html_file)
        print(line_18, file=html_file)
        print(line_19, file=html_file)
        print(line_20, file=html_file)
"""