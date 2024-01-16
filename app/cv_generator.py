from PIL import Image, ImageFont, ImageDraw



class Positions :
    
    # Personal Information
    NAME_xy = (221,178)
    EMAIL_xy = (217,230)
    PHONE_xy = (658, 178)
    ADDRESS_xy = (675, 230)


    ABOUT_ME_XY = (230, 458)

class Cv_Generator (Positions):

    def __init__(self, about_me : str ,personl_info : dict, projects : list) :

        self.personal_info = personl_info
        self.projects = projects

        if len(projects) > 4 : 
            raise ValueError("Projects Cannot be more than 4 ")

        self.bold_font = ImageFont.truetype('factor/font/Segoe UI Bold.ttf',size=20)
        self.light_font = ImageFont.truetype('factor/font/Segoe UI.ttf', size=20)
        self.about_me = about_me

    def light_cv_mode (self)  :
        self.img = Image.open('factor/cv-light.png').convert("RGB")
        self.generate_()
        return self.img

    def dark_cv_mode (self) : 
        self.img = Image.open('factor/cv-dark.png').convert("RGB")
        self.generate_()
        return self.img


    
    def generate_(self) : 
        self.img_dr = ImageDraw.Draw(self.img)

        self.insert_personal_info()

        self.insert_about()

        proj_count = 0
        title_y = 946
        descriptoin_y = 998
        
        for i in self.projects : 
            
            proj_count += 1
            title = f'{proj_count}. {i.get("title")}'


            self.insert_project(
                title = title,
                description = i.get('description'),
                title_y = title_y,
                descriptoin_y = descriptoin_y
            )

            title_y += 126
            descriptoin_y += 126
                


    def insert_project (self, title, description, title_y, descriptoin_y) : 



        self.bold_font.size = 30
        # insert title
        self.img_dr.text(
            (142, title_y),
            title,
            fill=(112,112,112),
            font=ImageFont.truetype('factor/font/Segoe UI Bold.ttf',size=30)
        )

        # insert description
        self.img_dr.text(
            (142, descriptoin_y),
            description,
            fill=(112,112,112),
            font=self.light_font
        )

    def insert_about (self) : 
        splited_text = self.about_me.split(' ')
        lines = []

        for text in splited_text :
            if len(splited_text) > 10 :

                lines.append(
                    ' '.join(splited_text[:10])
                )

                splited_text = splited_text[10:len(splited_text)]
            else:
                lines.append(
                    ' '.join(splited_text)
                )

                break


        last_line_y = self.ABOUT_ME_XY[1]
        for line in lines : 

            self.img_dr.text(
                (self.ABOUT_ME_XY[0], last_line_y),
                line,
                fill=(112,112,112),
                font=self.bold_font,
                align="center",
            )

            last_line_y += 50


    def insert_personal_info(self) : 
        
        self.img_dr.text(
            self.NAME_xy,
            self.personal_info.get('name'),
            fill=(112,112,112),
            font=self.bold_font
        )

        self.img_dr.text(
            self.EMAIL_xy,
            self.personal_info.get('email'),
            fill=(112,112,112),
            font=self.bold_font
        )


        self.img_dr.text(
            self.PHONE_xy,
            self.personal_info.get('phone'),
            fill=(112,112,112),
            font=self.bold_font
        )

        self.img_dr.text(
            self.ADDRESS_xy,
            self.personal_info.get('address'),
            fill=(112,112,112),
            font=self.bold_font
        )




# my_projects = [
#     {
#         'title' : "Todo App",
#         "description" : "Nice And Cool App i created using Django for testing my skills"
#     },
#     {
#         'title' : "Car App",
#         "description" : "Nice And Cool App i created using Django for testing my skills"
#     },
# ]



# my_personal_info_dict = {    
#     "name" : "Radwan Gaber Hijazi",
#     "phone" : "01009675007",
#     "address" : "Mansura, Bilqas",
#     "email" : "radawngaber22@gmail.com"
# }

# about_me = """
# Hello Gys My Name is Radwan Gaber Hijazi,
# And i love programming so much as u can see,
# I intersted in back-end development field.

# I Started With flask in 2020 then i go to django in the same year.
# """

# my_img = Cv_Generator(
#     personl_info = my_personal_info_dict ,
#     projects = my_projects,
#     about_me=about_me
# )

# my_img.light_cv_mode().show()
# my_img.dark_cv_mode().show()