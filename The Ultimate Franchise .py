import random
import sys
import time

def roll_dice():
    return random.randint(1, 6)

def simulate_game(teams, rolls):
    results = {}
    
    for team_name, players in teams.items():
        team_total = 0
        for player in players:
            player_total = 0
            for _ in range(rolls):
                player_total += roll_dice()
            team_total += player_total
            results[player] = player_total
        results[team_name] = team_total
    
    return results

def announce_results(results):
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    print("Final Scores:")
    for rank, (name, score) in enumerate(sorted_results, start=1):
        if name in teams:
            print(f"{rank}. {name} ({', '.join(teams[name])}) - {score} points")
        else:
            print(f"{rank}. {name} - {score} points")
        if rank == 3:
            break
    print(f"\nThe winner is {sorted_results[0][0]} with {sorted_results[0][1]} points!")
    print(f"2nd place: {sorted_results[1][0]} with {sorted_results[1][1]} points")
    print(f"3rd place: {sorted_results[2][0]} with {sorted_results[2][1]} points")

if __name__ == "__main__":
    teams = {
        "Tom and Jerry": ["Tom", "Jerry", "Spike"],
        "Harry Potter Franchise": ["Harry", "Hermione", "Ron"],
        "Breaking Bad": ["Walter White", "Jesse Pinkman", "Saul Goodman"]
    }
    
    rolls = 3
    
    results = simulate_game(teams, rolls)
    announce_results(results)

    time.sleep(1)  # Using time.sleep() from the time library

    sys.exit(0)
