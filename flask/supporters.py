ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

profile_fields =[
    "Profile Name",
    "Your Name",
    "Instagram",
    "Linkedin",
    "Facebook",
    "Github",
    "YouTube"
]

image_save_path = './static/profile_images/'