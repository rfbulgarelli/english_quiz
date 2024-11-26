# Definindo as questões e as respostas
questions = [
    ("I am always happy when it’s sunny outside.", "I always am happy when it’s sunny outside."),
    ("She usually drinks coffee in the morning.", "She drinks usually coffee in the morning."),
    ("They often go to the gym after work.", "They often are going to the gym after work."),
    ("Sometimes we eat out on weekends.", "We sometimes eat out on weekends."),  # Note: Ambas estão corretas.
    ("We do not often visit our grandparents.", "We not often do visit our grandparents."),
    ("He does not usually work on Fridays.", "He not usually works on Fridays."),
    ("I have never been to Australia.", "I never have been to Australia."),
    ("She is always studying for her exams.", "She always is studying for her exams."),
    ("He usually wakes up early.", "Usually he wakes up early."),
    ("They are sometimes late to meetings.", "They sometimes are late to meetings."),
    ("We do not often have such cold weather.", "Not often do we have such cold weather."),  # Formal construction
    ("She never forgets her friends’ birthdays.", "Never she forgets her friends’ birthdays.")
]

# Função para verificar as respostas
def check_answer(correct_answer):
    # Pedindo ao usuário para inserir a resposta correta
    user_input = input("Digite a resposta correta: ")
    # Verificando se a resposta está correta
    if user_input == correct_answer:
        print("Correto!")
    else:
        print("Incorreto! A resposta correta era:", correct_answer)

# Loop principal que mostra as perguntas e verifica as respostas
for index, (correct, incorrect) in enumerate(questions, start=1):
    print(f"\nPergunta {index}:")
    print("Correto:", correct)
    print("Incorreto:", incorrect)
    # Chama a função para verificar a resposta do usuário
    check_answer(correct)
