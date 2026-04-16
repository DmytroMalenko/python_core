# Task 1
import time
import random
from rich.progress import track
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt

console = Console()
result =[]
console.print(Panel("[black][1] [green]Start\n[black][2] [white]Play History\n[black][3] [red]Quit", title="Welcome", style="bold"))

while True:
    choice = Prompt.ask(
    "Choose option",
    choices=["1", "2", "3"],
    default="1"
    )

    if choice == "1":

        for i in track(range(3), description="[red]Processing..."):
            time.sleep(1)

        ask = Prompt.ask(
            "Enter Stone, Shears or Papier",
            choices=["Stone", "Shears", "Papier"],
            default="Stone"
            )
        
        computer = random.choice(["Stone", "Shears", "Papier"])
        print("Your chose ->",ask,".")
        print("Computer chose ->",computer,".")

        if ask == computer:
            new_result =  "Draw"
            console.print("[bold yellow]DRAW[/bold yellow]")

        elif ask == "Stone" and computer == "Shears" or ask == "Shears" and computer == "Papier" or ask == "Papier" and computer == "Stone":
            new_result = "Win"
            console.print("[bold green]You WIIIN[/bold green]")

        else:
            new_result = "Lose"
            console.print("[bold red]You LOSE[/bold red]")

        result.append({
            "Round": len(result) + 1,
            "You": ask,
            "Computer": computer,
            "Result": new_result
        })

    elif choice == "2":
        if not result:
            print("[black]History empty![black]")
        else:
            table = Table(title="Play History", header_style="bold cyan")
            table.add_column("Round", justify="center")
            table.add_column("You", justify="center")
            table.add_column("Computer", justify="center")
            table.add_column("Result", justify="center")
           
            wins = 0
            loses = 0
            draws = 0

        for item in result:
            if item["Result"] == "Win":
                color = "green"
                wins += 1
            elif item["Result"] == "Lose":
                color = "red"
                loses += 1
            else:
                color = "yellow"
                draws += 1


            table.add_row(
                str(item["Round"]),
                item["You"],
                item["Computer"],
                f"[bold {color}]{item['Result']}[/bold {color}]"
                )
        console.print(table)

        console.print(
            f"[green]Wins:[/green] {wins}  "
            f"[red]Lose:[/red] {loses}  "
            f"[yellow]Draw:[/yellow] {draws}")

        
    elif choice == "3":
                console.print("[red]Good Bye![/red]")
                break