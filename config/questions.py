
# Easy Apply Questions & Inputs

# Relative path of your default resume. If not found, uses your previously uploaded resume on LinkedIn.
default_resume_path = "all resumes/default/resume.pdf"

# Specify years of experience (different from current_experience).
years_of_experience = "5" 
# Do you require visa sponsorship now or in the future?
require_visa = "Yes"

# Link to your portfolio website (leave empty to skip).
website = "https://www.linkedin.com/in/muzahirabbas14/" 

# Link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/muzahirabbas14/"       

# Your citizenship status (leave empty to skip, but some companies require it).
# Options: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", 
# "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", 
# "Canadian Citizen/Permanent Resident", or "Other"
us_citizenship ="Non-citizen allowed to work for any employer"

## Handling Tricky Company Questions ##

# Desired salary (numbers only, some companies enforce this).
desired_salary = 400000          
# Notes:
# - For questions with "lakhs", the answer will be formatted as "XX.XX" (e.g., 2400000 becomes "24.00").
# - For monthly salaries, the answer will be divided by 12.

# Current CTC (numbers only, some companies require this).
current_ctc = 200000           
# Notes:
# - For questions with "lakhs", the answer will be formatted as "XX.XX".
# - For monthly salaries, the answer will be divided by 12.

# (In Development) Currency of salaries (e.g., "USD", "INR", "EUR").
# currency = "INR" 

# Notice period in days.
notice_period = 30
# Notes:
# - For questions in months or weeks, the answer will be divided by 30 or 7, respectively.

# Your LinkedIn headline.
headline = "Technical Artist | 3D Generalist | Game Developer: Expert in Procedural Workflows for CG, VFX, Cinematics & Game Dev" 

# Your LinkedIn summary (use \n for line breaks, leave empty to skip, but some companies require it).
summary = "I’m a multidisciplinary 3D artist and technical expert with a passion for optimizing workflows in game development and 3D animation. With expertise in Unreal Engine and a range of digital content creation (DCC) tools, I specialize in procedural modeling, shader development, and creating efficient pipelines that streamline production across teams. My skills include character design, environment modeling, and level design, focusing on integrating game mechanics and interactivity for immersive, engaging experiences. I thrive in solving complex technical challenges and enhancing artistic processes, ensuring top-tier quality in every project. Committed to continuous learning and innovation, I’m dedicated to driving efficiency and advancing game design, development, and production."

# Your cover letter (use \n for line breaks, leave empty to skip, but some companies require it).
cover_letter = ""
# Name of your most recent employer.
recent_employer = "SparkE" 

# Confidence level on a scale of 1-10 (for questions like "experience building web/mobile apps").
confidence_level = "8"

## Related Settings ##

## Manual Input Control

# Pause before each application submission during Easy Apply (disabled if run_in_background is True).
pause_before_submit = True

# Pause if the tool needs help answering a question (disabled if run_in_background is True).
# If False, answers randomly.
pause_at_failed_question = True 

# Overwrite previously saved answers.
overwrite_previous_answers = True
