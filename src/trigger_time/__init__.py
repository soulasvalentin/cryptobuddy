import logging
import azure.functions as func
from scrapers import run_all

def main(mytimer: func.TimerRequest) -> None:
    run_all()