# -*- coding: utf-8 -*-
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Install fixtures in order in single command
    """

    help = 'Install fixtures in order'

    def handle(self, *args, **options):
        call_command(
            'loaddata',
            'prod-auth-user.json',
        )

        self.stdout.write('Successfully installed fixtures')
