import time
import random
from rich.progress import track
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt

console = Console()
result = []

# Главное меню
console.print(
    Panel(
        "[black][1] [green]Start\n[black][2] [white]Play History\n[black][3] [red]Quit",
        title="Welcome",
        style="bold"
    )
)

# Бесконечный цикл меню
while True:
    choice = Prompt.ask(
        "Choose option",
        choices=["1", "2", "3"],
        default="1"
    )

    # Если пользователь выбрал игру
    if choice == "1":
        # Просто анимация загрузки
        for _ in track(range(3), description="[red]Processing..."):
            time.sleep(1)

        # Ввод хода игрока
        ask = Prompt.ask(
            "Enter Stone, Shears or Papier",
            choices=["Stone", "Shears", "Papier"],
            default="Stone"
        )

        # Случайный ход компьютера
        computer = random.choice(["Stone", "Shears", "Papier"])

        console.print(f"Your chose -> {ask}.")
        console.print(f"Computer chose -> {computer}.")

        # Проверка на ничью
        if ask == computer:
            new_result = "Draw"
            console.print("[bold yellow]DRAW[/bold yellow]")

        # Проверка на победу
        elif (ask == "Stone" and computer == "Shears") or \
             (ask == "Shears" and computer == "Papier") or \
             (ask == "Papier" and computer == "Stone"):
            new_result = "Win"
            console.print("[bold green]You WIN[/bold green]")

        # Иначе поражение
        else:
            new_result = "Lose"
            console.print("[bold red]You LOSE[/bold red]")

        # Сохраняем результат в историю
        result.append({
            "Round": len(result) + 1,
            "You": ask,
            "Computer": computer,
            "Result": new_result
        })

    # Если пользователь выбрал показ истории
    elif choice == "2":
        if not result:
            console.print("[yellow]History empty![/yellow]")
        else:
            # Создаём таблицу один раз
            table = Table(title="Play History", header_style="bold cyan")
            table.add_column("Round", justify="center")
            table.add_column("You", justify="center")
            table.add_column("Computer", justify="center")
            table.add_column("Result", justify="center")

            # Счётчики побед, поражений и ничьих
            wins = 0
            losses = 0
            draws = 0

            # Добавляем все строки в таблицу
            for item in result:
                if item["Result"] == "Win":
                    color = "green"
                    wins += 1
                elif item["Result"] == "Lose":
                    color = "red"
                    losses += 1
                else:
                    color = "yellow"
                    draws += 1

                table.add_row(
                    str(item["Round"]),
                    item["You"],
                    item["Computer"],
                    f"[bold {color}]{item['Result']}[/bold {color}]"
                )

            # Печатаем таблицу только после цикла
            console.print(table)

            # Печатаем статистику тоже один раз
            console.print(
                f"[green]Перемоги:[/green] {wins}  "
                f"[red]Поразки:[/red] {losses}  "
                f"[yellow]Нічиї:[/yellow] {draws}"
            )

    # Если пользователь хочет выйти
    elif choice == "3":
        console.print("[red]Вихід...[/red]")
        break