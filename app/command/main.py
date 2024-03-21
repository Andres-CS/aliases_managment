import functools
import logging as logger
import os
import click
import uuid
import dotenv

ENV_FILES = ['.env', '.env.dist']

def load_env_config(*env_files):
	"""Load environment variable files"""
	def decorator(func):
		try:
			cwd = os.getcwd()
			for env_file in env_files:
				filePath = cwd+"/"+env_file
				if(os.path.isfile(filePath)):
					dotenv.load_dotenv(filePath)
		except:
			msg="ERROR - .env file could not be loaded."
			click.echo(click.style(msg,fg="magenta"))
			exit(code=0)

		return func
	return decorator


# Set Logging
def logging_levels():
	"""Set logging level"""
	def decorator(func):
		try:
			myUUID = uuid.uuid4()
			filepath = str(os.getenv("LOGPATH"))+str(os.getenv("LOGFILE"))
			envApp = str(os.getenv("ENV"))
			logger.basicConfig(
				filename=filepath, 
				level=logger.DEBUG,
				format=f'%(levelname)s::%(asctime)s::{envApp}::{myUUID}::%(message)s',
			)
		except:
			msg="ERROR - could not set logger"
			click.echo(click.style(msg,fg="magenta"))
			exit(code=0)

		return func
	return decorator



@logging_levels()
@load_env_config(*ENV_FILES)
@click.group(context_settings=dict(help_option_names=['-h','--help']))
def main():
	"""Application for managind aliases system files"""