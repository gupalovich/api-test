from django.core.management.base import BaseCommand, CommandError

from elastic.manager import ElasticManager


class Command(BaseCommand):
    help = "Менеджер elasticsearch"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument(
            "--create",
            action="store_const",
            dest="action",
            const="create",
            help="Create the indices in elasticsearch",
        )
        parser.add_argument(
            "--populate",
            action="store_const",
            dest="action",
            const="populate",
            help="Populate elasticsearch indices with models data",
        )
        parser.add_argument(
            "--delete",
            action="store_const",
            dest="action",
            const="delete",
            help="Delete the indices in elasticsearch",
        )
        parser.add_argument(
            "--rebuild",
            action="store_const",
            dest="action",
            const="rebuild",
            help="Delete the indices and then recreate and populate them",
        )

    def handle(self, *args, **options):
        if not options["action"]:
            raise CommandError(
                "No action specified. Must be one of" " '--create','--populate', '--delete' or '--rebuild' ."
            )

        action = options["action"]

        if action == "create":
            ElasticManager.index()
        elif action == "populate":
            ElasticManager.populate()
        elif action == "delete":
            ElasticManager.delete()
        elif action == "rebuild":
            raise NotImplementedError()
        else:
            raise CommandError(
                "Invalid action. Must be one of" " '--create','--populate', '--delete' or '--rebuild' ."
            )
