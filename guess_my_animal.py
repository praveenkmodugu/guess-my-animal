from animal import get_random_animal
from ai import call_gpt


def main():
    animal = get_random_animal()
    # print(animal)
    
    print("I am thinking of an animal.")
    print("Can you guess what animal it is?")
    # Start asking first question
    question = input(f"Ask me a yes or no question: ")
    # Prompt the GPT with that question and respond back with yes or no answer
    gpt_response = call_gpt(f"You have to answer to this question {question} of guessing a game for this {animal} with just 'yes' and 'no'.")
    if question != animal:
        print(gpt_response)
    # Continue asking as long as the user not guessed correctly
    while question != animal:
        question = input(f"Ask me a yes or no question: ")
        gpt_response = call_gpt(f"You have to answer to this question {question} of guessing a game for this {animal} with just 'yes' and 'no'")
        # Print only when the user not guessed correctly
        if question != animal:
            print(gpt_response)
    # Print out correct when the user guessed correctly
    print("Correct!")

    # TODO: your code here!
    pass



if __name__ == "__main__":
    main()
