import random
def search_location():
    search_list = [
    "Canada"
    ,"Pakistan",
    "United States", 
    "Germany", 
    "United Kingdom", 
    "Australia", 
    "France", 
    "Japan", 
    "Netherlands", 
    "Switzerland", 
    "Singapore", 
    "Sweden", 
    "South Korea", 
    "Ireland", 
    "Norway", 
    "Italy",
    "Spain",      
    "Finland",   
    "Denmark",    
    "Poland",     
    "New Zealand" 
    ]   
    return random.choice(search_list)
#LINKEDIN SEARCH PREFERENCES

# Keywords to look for in LinkedIn job postings
# Provide your desired search terms within quotes ' "your search term" ', separated by commas. For example: ["Software Engineer", "Software Developer", "Selenium Developer"]
search_terms = ["After Effects","3D Animator","Technical Artist", "Shader specialist", "Game Programming", "3D Characters", "3D Environments", "3D Generalist", "3D Artist", "Level Designer", "Game Designer", "Game Developer"]

# Specify the location for your job search. This will populate the "City, state, or zip code" field. Leave empty as "" to skip.
search_loc = search_location()              # Examples: "", "United States", "India", "Chicago, Illinois, United States", "90001, Los Angeles, California, United States", "Bengaluru, Karnataka, India", etc.

# Number of applications to submit for the current search term before moving to the next
switch_number = 30                 # Must be a number greater than 0. Do not enclose in quotes.

# Shuffle the order of search terms randomly?
randomize_search_order = True     # True or False


# >>>>>>>>>>> Fine-tune Your Job Search <<<<<<<<<<<
''' 
Customize your search criteria or leave fields blank to use default settings (except for True/False options). Here's how to leave fields empty:
Format: QUESTION = VALID_ANSWER

## Examples of empty fields: 
* question_1 = ""                    # answer1, answer2, answer3, etc.
* question_2 = []                    # (multiple choice)
* question_3 = []                    # (dynamic multiple choice)

## Examples of how to answer questions:
* question_1 = "answer1"                  # "answer1", "answer2", "answer3" or ("" for no selection). Answers are case-sensitive.
* question_2 = ["answer1", "answer2"]     # (multiple choice) "answer1", "answer2", "answer3" or ([] for no selection). Answers must be in [] and are case-sensitive.
* question_3 = ["answer1", "Random AnswER"]     # (dynamic multiple choice) "answer1", "answer2", "answer3" or ([] for no selection). Answers must be in [] and don't need to match available options exactly.

'''

sort_by = "Most relevant"                       # "Most recent", "Most relevant" or ("" to disable) 
date_posted = "Past month"         # "Any time", "Past month", "Past week", "Past 24 hours" or ("" to disable)
salary = ""                        # "$40,000+", "$60,000+", "$80,000+", "$100,000+", "$120,000+", "$140,000+", "$160,000+", "$180,000+", "$200,000+"

easy_apply_only = True             # True or False

experience_level = ["Entry level", "Associate", "Mid-Senior level", "Director", "Executive"]              # (multiple choice) "Internship", "Entry level", "Associate", "Mid-Senior level", "Director", "Executive"
job_type = ["Full-time", "Part-time", "Contract", "Temporary"]                      # (multiple choice) "Full-time", "Part-time", "Contract", "Temporary", "Volunteer", "Internship", "Other"
on_site = ["On-site", "Remote", "Hybrid"]                       # (multiple choice) "On-site", "Remote", "Hybrid"

companies = []                     # (dynamic multiple choice) Ensure company names match exactly, including capitalization. 
                                   # Examples: "7-eleven", "Google","X, the moonshot factory","YouTube","CapitalG","Adometry (acquired by Google)","Meta","Apple","Byte Dance","Netflix", "Snowflake","Mineral.ai","Microsoft","JP Morgan","Barclays","Visa","American Express", "Snap Inc", "JPMorgan Chase & Co.", "Tata Consultancy Services", "Recruiting from Scratch", "Epic", and so on...
location = ["Europian Union","United States","Canada","Germany","Pakistan","Singapore","United Kingdom","Australia","Norway","Sweden","Denmark"]                      # (dynamic multiple choice)
industry = []                      # (dynamic multiple choice)
job_function = []                  # (dynamic multiple choice)
job_titles = []                    # (dynamic multiple choice)
benefits = []                      # (dynamic multiple choice)
commitments = []                   # (dynamic multiple choice)

under_10_applicants = False        # True or False
in_your_network = False            # True or False
fair_chance_employer = False       # True or False






## >>>>>>>>>>> Exclude Irrelevant Jobs <<<<<<<<<<<
 
# Blacklist: Companies and keywords to avoid in the "About Company" section 
about_company_bad_words = ["React.js"]       # (dynamic multiple search) or leave empty as []. For example: ["Staffing", "Recruiting", "Company Name"]

# Whitelist: Exceptions to the 'about_company_bad_words' filter (e.g., "Robert Half" even though it's a staffing company)
about_company_good_words = ["c++","Game","Unreal"]      # (dynamic multiple search) or leave empty as []. For example: ["Robert Half", "Dice"]

# Exclude jobs with these keywords in their descriptions (case-insensitive, in development)
bad_words = []                     # (dynamic multiple search) or leave empty as []. Examples: ["word_1", "phrase 1", "word word", "polygraph", "US Citizenship", "Security Clearance"]

# Do you possess an active Security Clearance? 
security_clearance = False         # True or False

# Do you have a Master's degree? If True, the tool will prioritize jobs mentioning "master" in the description, considering your experience level (if 'current_experience' is not set to -1).
did_masters = True                 # True or False

# Set your current experience level in years. Use -1 to apply to all jobs regardless of experience requirements.
current_experience = 5             # Integers greater than or equal to -1 (e.g., -1, 0, 1, 2, 3, 4...)
##






