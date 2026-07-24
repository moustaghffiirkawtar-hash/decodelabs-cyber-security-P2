from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich import print as rprint

console = Console()

def cypherchar(c):
    shift = 4
    return chr((ord(c.upper()) - 65 + shift) % 26 + 65)

def cyphertext(text):
    cytext = ""
    for c in text:
        if c.isalpha():
            encrypted = cypherchar(c)
            cytext += encrypted.lower() if c.isupper() else encrypted.upper()
        else:
            cytext += c
    return cytext

def decypherchar(c):
    shift = 4
    return chr((ord(c.upper()) - 65 - shift) % 26 + 65)

def decyphertext(text):
    decytext = ""
    for c in text:
        if c.isalpha():
            decrypted = decypherchar(c)
            decytext += decrypted.lower() if c.isupper() else decrypted.upper()
        else:
            decytext += c
    return decytext

# --- Rich UI ---
console.print(Panel.fit(
    "[bold cyan]Caesar Cipher[/bold cyan] — shift 4 + case reversal",
    border_style="cyan"
))

choice = Prompt.ask("\n[bold]Action[/bold]", choices=["e", "d"], default="e",
                    prompt_suffix=" ([green]e[/green]=encrypt / [red]d[/red]=decrypt) > ")

text = Prompt.ask("[bold]Enter your text[/bold]")

if choice == "e":
    result = cyphertext(text)
    console.print(Panel(
        f"[green]{result}[/green]",
        title="[bold green]Encrypted[/bold green]",
        border_style="green"
    ))
else:
    result = decyphertext(text)
    console.print(Panel(
        f"[yellow]{result}[/yellow]",
        title="[bold yellow]Decrypted[/bold yellow]",
        border_style="yellow"
    ))