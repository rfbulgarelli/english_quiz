def mashwork_english_quiz():
    print("Bem-vindo ao teste rápido de inglês! Vamos melhorar sua gramática e frequência na língua inglesa.")
    print("Leia a frase e responda se está 'Correto' ou 'Incorreto'.\n")
    
    questions = [
        {
            "question": "I always am happy when it’s sunny outside.",
            "correct": "Incorreto",
            "explanation": "A ordem correta é: 'I am always happy when it’s sunny outside.'"
        },
        {
            "question": "She usually drinks coffee in the morning.",
            "correct": "Correto",
            "explanation": "A ordem está correta: 'She usually drinks coffee in the morning.'"
        },
        {
            "question": "They often are going to the gym after work.",
            "correct": "Incorreto",
            "explanation": "A forma correta é: 'They often go to the gym after work.'"
        },
        {
            "question": "Sometimes we eat out on weekends.",
            "correct": "Correto",
            "explanation": "Ambas as formas podem estar corretas, mas esta enfatiza a frequência no início."
        },
        {
            "question": "We do not often visit our grandparents.",
            "correct": "Correto",
            "explanation": "A frase está gramaticalmente correta: 'We do not often visit our grandparents.'"
        },
        {
            "question": "He not usually works on Fridays.",
            "correct": "Incorreto",
            "explanation": "A forma correta é: 'He does not usually work on Fridays.'"
        },
        {
            "question": "I never have been to Australia.",
            "correct": "Incorreto",
            "explanation": "A ordem correta é: 'I have never been to Australia.'"
        },
        {
            "question": "She always is studying for her exams.",
            "correct": "Incorreto",
            "explanation": "A forma correta é: 'She is always studying for her exams.'"
        },
        {
            "question": "Usually he wakes up early.",
            "correct": "Incorreto",
            "explanation": "A forma mais comum é: 'He usually wakes up early.'"
        },
        {
            "question": "They sometimes are late to meetings.",
            "correct": "Incorreto",
            "explanation": "A ordem correta é: 'They are sometimes late to meetings.'"
        },
        {
            "question": "Not often do we have such cold weather.",
            "correct": "Incorreto",
            "explanation": "A forma correta é: 'We do not often have such cold weather.'"
        },
        {
            "question": "Never she forgets her friends’ birthdays.",
            "correct": "Incorreto",
            "explanation": "A forma correta é: 'She never forgets her friends’ birthdays.'"
        },
    ]
    
    score = 0
    
    for idx, question in enumerate(questions, 1):
        print(f"\nPergunta {idx}: {question['question']}")
        user_answer = input("Digite 'Correto' ou 'Incorreto': ").capitalize()
        
        if user_answer == question["correct"]:
            print("✔️ Correto!")
            score += 1
        else:
            print(f"❌ Errado! {question['explanation']}")
    
    print(f"\nTeste concluído! Você acertou {score} de {len(questions)} perguntas.")
    print("Continue praticando para melhorar ainda mais seu inglês!")

if __name__ == "__main__":
    mashwork_english_quiz()
