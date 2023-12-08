class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        roll_index = 0
        frame_scores = []

        for frame in range(12):
            if self.is_strike(roll_index) and len(self.rolls) > roll_index + 2:
                total_score += 10 + self.strike_bonus(roll_index)
                frame_scores.append(total_score)
                roll_index += 1
            elif self.is_spare(roll_index) and len(self.rolls) > roll_index + 2:
                total_score += 10 + self.spare_bonus(roll_index)
                frame_scores.append(total_score)
                roll_index += 2
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


def main():
    game = BowlingGame()

    print("Welcome to the Bowling Game!")

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
