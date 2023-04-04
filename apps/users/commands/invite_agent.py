import argparse

from apps.users.services import InviteAgentStory


def parse_args(*args, **kwargs):
    parser = argparse.ArgumentParser(description='Check and fix users profiles.')
    parser.add_argument('command_name', type=str, default='command', help='Name of the command.')
    parser.add_argument('-email', type=str, help='New agents email.')

    return parser.parse_args()


async def command(settings, app, parsed_args):
    # Add the following three lines to init tortoise routers
    from tortoise import Tortoise

    from config.orm import TORTOISE_ORM

    await Tortoise.init(config=TORTOISE_ORM)

    return await InviteAgentStory().execute(parsed_args.email)
