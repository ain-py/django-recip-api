"""
Django command to wait for the databasse to be availabe
"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """ Django commmand to wait for databse."""
    
    def handle(self,*args,**options):
        self.stdout.write('Waiting for database..')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2Error, OperationalError):
                self.stdout.write(self.style.ERROR_OUTPUT("databases unavailable trying again in 1 sec!"))
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS("Databse available!"))
                
    
    