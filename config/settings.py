# LinkedIn Settings

# Should the application close browser tabs for external applications? 
# It's recommended to keep this True. If set to False, ensure all tabs are closed before closing the browser.
close_tabs = True                  # True or False

apiserver="gemini"

# Your about yourself section on LinkedIn
about_yourself="I’m a multidisciplinary 3D artist, technical expert, and game developer with a strong foundation in computer science and a passion for optimizing complex workflows. With expertise in Unreal Engine and a broad range of digital content creation tools, I specialize in procedural modeling, shader development, and pipeline optimization for 3D animation, game development, and VFX projects. I’ve collaborated with clients globally, delivering high-quality cinematic trailers, character animations, and immersive environments for both commercial and metaverse projects. As the co-founder and Lead Technical Artist at SparkE Production, I have designed futuristic cityscapes, developed custom tools for asset creation, and led technical teams to streamline production for high-impact results. My work spans character design, environment modeling, and level design, integrating advanced game mechanics and interactivity to enhance user experience. I’m always eager to solve complex technical challenges, combining my artistic vision and programming skills to push the boundaries of 3D content creation and deliver innovative solutions across CGI, gaming, and metaverse industries."

# Features currently under development
# Send connection requests to HR professionals
# connect_hr = True                  # True or False

# Message to send with connection requests. Limit to 200 characters.
# Leave empty to send without a message. This is recommended as personalized invites are limited without LinkedIn Premium.
# connect_request_message = ""       

# Run the program continuously until manually stopped (Beta). 
# This setting is ignored if run_in_background is True.
run_non_stop = False               # True or False 
alternate_sortby = True            # True or False
cycle_date_posted = True           # True or False
stop_date_cycle_at_24hr = True     # True or False

# Resume Generator Settings (Experimental & In Development)

# Path to the folder for saving generated resumes
generated_resume_path = "all resumes/" 

# Global Settings

# File paths for storing application history
# The text after the last "/" will be used as the file name.
file_name = "all excels/all_applied_applications_history.csv"
failed_file_name = "all excels/all_failed_applications_history.csv"
logs_folder_path = "logs/"

# Maximum time in seconds to wait between clicks (Non-negative integers only)
click_gap = 1                      

# Set to False to see the browser window (May reduce performance)
run_in_background = False          
# When True, the following settings are automatically set to False: pause_at_failed_question, pause_before_submit

# Disable browser extensions for better performance
disable_extensions = True          

# Run in safe mode (guest profile) - useful if Chrome is slow or has multiple profiles
safe_mode = False                 

# Enable smooth scrolling (May reduce performance)
smooth_scroll = True             

# Keep the screen active to prevent the PC from sleeping
# Alternatively, disable this and adjust PC sleep settings
keep_screen_awake = True           

# Enable undetected mode to bypass anti-bot measures (Experimental and unstable)
stealth_mode = True             
# This feature might require 'stealth_mode = True' due to anti-bot measures on ChatGPT's website.
# use_resume_generator = False       
