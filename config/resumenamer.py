import random
import difflib

# Resume files
resumepaths = [
    "CV_3DArtist_3DGeneralist", 
    "CV_CharacterArtist_CharacterSpecialist", 
    "CV_GameDev", 
    "CV_GameDev_LevelDesigner",
    "CV_TechArtist_GameDev"
]

# Step 1: Create five lists of keywords to see in job titles
words_list_1 = ["Art","3d animation", "3d modelling", "3d designer", "3d artist", "3d vfx","3d modeller"]
words_list_2 = ["Character Animation","character design", "character artist", "rigging", "character animator", "3d character"]
words_list_3 = ["game developer", "game designer", "game programmer", "unreal engine", "game artist","gameplay"]
words_list_4 = ["environment artist", "level designer", "level artist"]
words_list_5 = ["technical","technical artist", "pipeline", "game developer", "unreal engine","realtime technical"]

all_lists = [words_list_1, words_list_2, words_list_3, words_list_4, words_list_5]

# Step 3: Function to calculate similarity score for each list
def calculate_similarity_score(word, word_list):
    score = 0
    for w in word_list:
        # Check for partial match using difflib's SequenceMatcher
        if difflib.SequenceMatcher(None, word, w).ratio() > 0.5:  # Consider as similar if match ratio > 0.5
            score += 1
    return score

def selectResumePath(jtitle):
    exact_match_counts = [0] * len(all_lists)

    # Count exact matches for each list
    for index, word_list in enumerate(all_lists):
        for w in word_list:
            if w.lower() in jtitle.lower():
                exact_match_counts[index] += 1

    # Check if there are any exact matches
    max_exact_matches = max(exact_match_counts)
    if max_exact_matches > 0:
        best_match_index = exact_match_counts.index(max_exact_matches)
        print(f"\n\n>>>>Resume is {resumepaths[best_match_index]} for title '{jtitle}' (exact match found in {max_exact_matches} keywords)")
        return f"all resumes/default/{resumepaths[best_match_index]}.pdf"

    # Calculate similarity scores if no exact matches are found
    similarity_scores = [calculate_similarity_score(jtitle, word_list) for word_list in all_lists]
    best_match_index = similarity_scores.index(max(similarity_scores))

    # Step 5: Assign the word to the best matching list
    print(f"\n\n>>>>Resume is {resumepaths[best_match_index]} for title '{jtitle}' (best match based on similarity)")
    
    return f"all resumes/default/{resumepaths[best_match_index]}.pdf"
