import random


def main():
    state_capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Florida': 'Tallahassee',
        'Hawaii': 'Honolulu',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'New Hampshire': 'Concord',
        'New York': 'Albany',
        'Ohio': 'Columbus',
        'Oregon': 'Salem',
        'Texas': 'Austin',
        'Wyoming': 'Cheyenne'
    }
    states = list(state_capitals.keys())
    correct_responses = 0
    incorrect_responses = 0

    while True:
        state = random.choice(states)
        answer = input(
            f'What is the capital of {state}? (or enter 0 to quit): '
        ).strip()

        if answer == '0':
            break
        if answer.lower() == state_capitals[state].lower():
            print('That is correct.')
            correct_responses += 1
        else:
            print('That is incorrect.')
            incorrect_responses += 1

    print(f'You had {correct_responses} correct responses and '
          f'{incorrect_responses} incorrect responses.')


if __name__ == '__main__':
    main()
