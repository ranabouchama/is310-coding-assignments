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

