#Resume Selector

import random
import difflib

#Resume paths

resumepaths = ["resume", "resume2", "resume3", "resume4"]

# Step 1: Create keywords for each path / resume
words_list_1 = ["3d animation", "3d modelling", "3d designer", "3d artist", "3d vfx"]
words_list_2 = ["character design", "character artist", "rigging", "character animator", "3d character"]
words_list_3 = ["Game developer", "game designer", "game programmer", "level designer", "game artist"]
words_list_4 = ["technical artist", "pipeline designer", "game developer", "unreal engine", "gameplay designer"]

# add lists to all_lists
all_lists = [words_list_1, words_list_2, words_list_3, words_list_4]

# Step 3: Function to calculate similarity score for each list
def calculate_similarity_score(word, word_list):
    score = 0
    for w in word_list:
        # Check for partial match using difflib's SequenceMatcher
        if difflib.SequenceMatcher(None, word, w).ratio() > 0.5:  # Consider as similar if match ratio > 0.5
            score += 1
    return score
def selectResumePath(jtitle):
    similarity_scores = [calculate_similarity_score(jtitle, word_list) for word_list in all_lists]
    best_match_index = similarity_scores.index(max(similarity_scores))

    # Step 5: Assign the resune path to the best matching list
    return ("all resumes/default/"+resumepaths[best_match_index]+".pdf")