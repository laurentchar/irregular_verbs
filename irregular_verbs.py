#!/usr/bin/env python

import csv
import random

def load_verbs_from_csv(file_path):
    verbs = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            french_verb = row['French']
            english_forms = (row['Infinitive'], row['Preterit'], row['Past Participle'])
            verbs[french_verb] = english_forms
    return verbs

def quiz(verbs, num_questions=20):
    print("Bienvenue au quiz des verbes irréguliers anglais!")
    score = 0
    total = min(num_questions, len(verbs))
    selected_verbs = random.sample(list(verbs.items()), total)
    
    for french_verb, english_forms in selected_verbs:
        print(f"\nQuel est le verbe anglais pour '{french_verb}'?")
        infinitive = input("Infinitif: ").strip().lower()
        preterit = input("Prétérit: ").strip().lower()
        past_participle = input("Participe passé: ").strip().lower()
        
        if (infinitive, preterit, past_participle) == english_forms:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! La réponse correcte est: {english_forms}")
    
    print(f"\nVotre score: {score}/{total}")
    if score == total:
        print("Félicitations! Vous avez tout juste!")
    else:
        print("Continuez à pratiquer pour vous améliorer!")

if __name__ == "__main__":
    file_path = 'verbs.csv'  # Update this path to the location of your CSV file
    verbs = load_verbs_from_csv(file_path)
    quiz(verbs)
