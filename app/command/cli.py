import logging as logger
import os
import filecmp
import shutil
import click
from typing import Optional
import dotenv

from .main import main
from app.update.updateengine import update


@main.command('update')
@click.option('-a','--all', is_flag=True, help='Update all alias files')
@click.option('-v','--verbose', is_flag=True, help='Show verbose output')
@click.argument('filename', required=False)
def update(
	filename: Optional[str],
	all: bool,
	verbose: bool
):
	"""Update alias files"""
	
	logger.debug("-- command:update --")
	if(all):
		print("ALL has been selected")
		obj = update()
		obj.updateAliases()
	
	if(filename == "update"):
		print(f'Filename: {filename} has been updated')

	else:
		msg="You either passed an option not valid or no option at all."
		click.echo(click.style(msg,fg="magenta"))