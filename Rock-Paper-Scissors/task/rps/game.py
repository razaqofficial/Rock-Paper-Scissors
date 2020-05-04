# Write your code here
import random


class RockPaperScissors:
    def __init__(self):
        self.valid_input = ['rock', 'paper', 'scissors', '!exit', '!rating']
        self.game_state = True
        self.player_list = dict()
        self.initialize_players()
        self.default_options = {'rock': ['scissors'], 'paper': ['rock'], 'scissors': ['paper']}
        self.game_options = dict()
        self.player_name = input('Enter your name: ')
        print('Hello,', self.player_name)
        if self.player_name not in self.player_list:
            self.player_list[self.player_name] = 0

        option_input = input()
        if option_input == '':
            self.game_options = self.default_options
        else:
            self.set_game_options(option_input)
        print("Okay, let's start")
        self.start_game()

    def set_game_options(self, option_input):
        all_options = option_input.split(',')
        for option in all_options:
            other_options = all_options[all_options.index(option) + 1:]
            list_wo_option = [item for item in all_options if item != option]
            other_options.extend(list_wo_option)
            unique_list = list(dict.fromkeys(other_options))
            # get the half of the list
            weaker_element = unique_list[len(unique_list) // 2:]
            self.game_options[option] = weaker_element

    def initialize_players(self):
        rating_file = open('rating.txt', 'r+', encoding='utf-8')
        players_lines = [player.rstrip('\n') for player in rating_file.readlines()]
        for player in players_lines:
            name, score = player.split()
            self.player_list[name] = int(score)

    def start_game(self):
        while True:
            command = input()
            r_word = random.choice(list(self.game_options.keys()))
            # print(r_word)
            if command == '!exit':
                print('Bye!')
                exit()
            elif command == '!rating':
                print('Your rating: {}'.format(self.player_list[self.player_name]))
            elif command == r_word:
                self.player_list[self.player_name] = self.player_list[self.player_name] + 50
                print('There is a draw ({})'.format(command))
            elif command not in self.game_options:
                print('Invalid input')
            else:
                self.process_option_input(r_word, command)

    def process_option_input(self, random_word, user_word):
        option_values = self.game_options[user_word]
        if random_word in option_values:
            self.player_list[self.player_name] = self.player_list[self.player_name] + 100
            print('Well done. Computer chose {} and failed'.format(random_word))
        else:
            print('Sorry, but computer chose {}'.format(random_word))


rock_paper_scissors = RockPaperScissors()
