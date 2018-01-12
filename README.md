# Roleplay Tools for Discord

For now this just calculates the likelihood of hitting a specific value when
throwing a custom die several times.

## Requirements

- Numpy
- Scipy

## Running the Script

    python prob_dice.py <Sum to Hit> <Number of Trials> <Number of Sides>

### Examples

    python dice_prob.py 12 2

    >> Roughly 3% chances of rolling a 12 with 2 dice of 6 faces each

    python dice_prob.py 20 4 10

    >> Roughly 6% chances of rolling a 20 with 4 dice of 10 faces each

    python dice_prob.py 5 3 "[-1, 0, 1, 2]"

    >> Roughly 5% chances of rolling a 5 with 3 dice of 4 faces each
