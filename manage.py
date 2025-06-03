from peewee_migrate import Router
import typer
import subprocess
from settings import db


app = typer.Typer()
router = Router(db)

@app.command()
def makemigrations(name: str):
    """Create a new migration with the given name."""
    subprocess.run([f'pw_migrate', 'create', '--auto', '--auto-source', 'models', '--database',
                    'sqlite:///db.db', '--directory', 'migrations', name])
    typer.echo(f"Migration '{name}' created.")


@app.command()
def migrate():
    """Apply all pending migrations."""
    router.run()
    typer.echo("Migrations applied successfully.")


if __name__ == "__main__":
    app()
