class BowlingGame:
    def __init__(self):
        self.rolls = []
"""Initialize a new BowlingGame instance.

        This method initializes the rolls list to keep track of pins knocked down.
        """
    def roll(self, pins):
        self.rolls.append(pins)
         """Record the number of pins knocked down in a roll.

        Args:
            pins (int): The number of pins knocked down in the roll.

        Raises:
            ValueError: If the pins value is outside the range of 0 to 10.
        """

    def score(self): #whole scoring system with total score,frame index"
        total_score = 0
        roll_index = 0
        frame_scores = []
 """Calculate the total score of the game.

        Returns:
            list: A list containing the scores for each frame in the game.
        """
        for frame in range(12):
            if self.is_strike(roll_index) and len(self.rolls) > roll_index + 2:
                total_score += 10 + self.strike_bonus(roll_index)
                frame_scores.append(total_score)
                roll_index += 1
                """frame index for strikes"""
            elif self.is_spare(roll_index) and len(self.rolls) > roll_index + 2:
                total_score += 10 + self.spare_bonus(roll_index)
                frame_scores.append(total_score)
                roll_index += 2
                """frame index for spares"""
            elif len(self.rolls) > roll_index + 1:
                total_score += self.frame_score(roll_index)
                frame_scores.append(total_score)
                roll_index += 2
            else:
                break

        return frame_scores

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10 if roll_index < len(self.rolls) else False

    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10 if roll_index + 1 < len(self.rolls) else False

    def strike_bonus(self, roll_index):
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2]

    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]

# The main function and input handling logic can be kept without specific PythonDoc comments as it's user interaction logic.
def main():
    game = BowlingGame()
# logic
    print("Welcome to the Bowling Game!")
# total  12 frames
    for frame in range(12):
        while True:
            try:
                roll1 = int(input(f"Enter number of pins knocked down in frame {frame + 1}, roll 1: "))
                if roll1 < 0 or roll1 > 10:
                    raise ValueError("Please enter a valid number of pins (0-10)!")
                game.roll(roll1)
                break
            except ValueError as e:
                print(e)

        if roll1 < 10:
            while True:
                #for perfect roll sytem as 4 in first pin then only 6 pins left for the second how it's working
                try:
                    roll2 = int(input(f"Enter number of pins knocked down in frame {frame + 1}, roll 2: "))
                    if roll2 < 0 or roll2 > (10 - roll1):
                        raise ValueError(f"Please enter a valid number of pins (0-{10 - roll1})!")
                    game.roll(roll2)
                    break
                except ValueError as e:
                    print(e)
        else:
            roll2 = 0
            game.roll(0)

        frame_scores = game.score()
        print(f"Total Score after frame {frame + 1}: {frame_scores[frame] if frame < len(frame_scores) else frame_scores[-1]}")

if __name__ == "__main__":
    main()
