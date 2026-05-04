from rich.console import Console
from rich.table import Table

console = Console()
console.print("Initial data to work with!:", style="italic pink")

table = Table(title="Favorite Movies")
table.add_column("Released", style="pink", no_wrap=True)
table.add_column("Title", style="orange")
table.add_row("December 14, 2018", "Into the Spider-Verse")
table.add_row("June 2, 2023", "Across the Spider-Verse")
table.add_row("August 31, 2016", "La La Land")
table.add_row("April 8, 2022", "Everything Everywhere All at Once")

console.print(table)
console.print("\n[italic pink]Now I want you to enter your preferred movies:[/bold cyan]")

while True:
    title = console.input("[bold cyan]Movie title (press Enter to finish): [/]")
    if not title.strip():
        break

    released = console.input("[bold cyan]Release date: [/]")
    if not released.strip():
        released = "Unknown"

    table.add_row(released.strip(), title.strip())
    console.print("[green]Added![/]")

    again = console.input("[bold cyan]Add another movie? (y/n): [/]")
    if again.strip().lower() not in ("y", "yes"):
        break

console.print("\n[italic pink]Updated movie list:[/bold cyan]")
console.print(table)

