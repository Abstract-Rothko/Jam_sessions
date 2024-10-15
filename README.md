# “Jam Sessions”

Hello and welcome to my project~!

Well, I say that, but the entire purpose behind this `jam sessions` repository is that it becomes a basket for any and all things I do that help develop my programming skills(specifically __python__). 

This will be where all my practice gets shown off, essentially.

__All of my sessions will be posted into 3 categories:__

1. **mini_project_sessions**: this will a collection of small projects to test what I've been learning.

2. **practice_sessions**: a collection of notes and other miscellaneous things.

3. **junk_sessions**: as stated, it's a collection of junk. Don't worry about it.

If you're curious, I'll do my best to regarly update this readme file with my progress. All feedback is welcome.

## Mini-Projects:

1. [logplan_module](1_mini_project_sessions/1_logplan_module) - this is a module with 25 functions that could be used in the logistics planning department(especially packaging).

```python

# 7.
def tot_inserts_per_day(annual_demand, lot_size, inserts_per_bin, total_production_days = 365):
    """
    Calculates the total inserts required per day
    
    :param annual_demand: total parts needed for 1 year(expected to be an integer)
    :param lot_size: lot size of a part(expected to be an integer)
    :param inserts_per_bin: total inserts used per bin(expected to be an integer)
    :param total_production_days: total days of expected production(expected to be an integer)
    :return: the total inserts required per day(expected to be a string)
    """
    tot_bins = annual_demand / lot_size
    tot_bins_per_day = tot_bins / total_production_days
    inserts_required = tot_bins_per_day * inserts_per_bin
    return f"Inserts required per day: {inserts_required:.2f}"

```

2. [one_piece_quiz](1_mini_project_sessions/2_one_piece_quiz) - this quiz tests you on a few basic questions on one piece and scores how well you've done.

```python
# 8. 
giant = input("What is the name of the giant that used to take care of Nico Robin? ").lower()

if giant == "jaguar d. saul":
    score += 1
    print("Correct!")
elif giant == "saul":
    score += .5
    print("Correct!")
else:
    print("Incorrect!")
```

3. [phoebe_adventures](1_mini_project_sessions/3_phoebe_adventures) - this is a "choose your own adventure"-style game that centres around helping Phoebe Erin Class get home.
4. [manga_eda](1_mini_project_sessions/4_manga_eda) - this is my first eda done on the "best-selling-manga.csv" dataset. I even made some charts!

![manga publisher](1_mini_project_sessions/4_manga_eda/assets/Publisher_chart.png)

## Practice/Study Notes:

1. _In Progress_


## Junk Ideas:

1. __As previously stated, it will be a collection of junk. Don't worry about it.__
