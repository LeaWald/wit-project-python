from abc import ABC

import click
import os
from Repository import Repository
from ui import ui

repo = Repository()

@click.group()
def cli():
    pass

@cli.command()
def init():
    current_path = os.getcwd()
    repo.wit_init()
    click.echo(f"Initialized repository at {current_path}")

@cli.command()
@click.argument('file')
def add(file):
    repo.wit_add(file)
    click.echo(f"Added {file} to the staging area")

@cli.command()
@click.argument('message')
def commit(message):
    repo.wit_commit(message)
    click.echo(f"Committed with message: {message}")

@cli.command()
def log():
    repo.wit_log()

@cli.command()
def status():
    repo.wit_status()

@cli.command()
@click.argument('commit_id')
def checkout(commit_id):
    repo.wit_check_out(commit_id)
    click.echo(f"Checked out commit: {commit_id}")

if __name__ == '__main__':
    cli()

