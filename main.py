import argparse
from fastapi import FastAPI
import uvicorn
from src.interface.api.routes import router
from src.interface.cli.commands import run_analyse, run_fetch, run_fetch_contracts, run_all_4h

app = FastAPI()
app.include_router(router)

def main():
    parser = argparse.ArgumentParser(description="Lancer l'app en mode API ou CLI")
    parser.add_argument('--mode', choices=['api', 'analyse', 'fetch', 'fetch_contracts', 'run_all'], required=True)
    parser.add_argument('--pair', type=str)
    parser.add_argument('--interval', type=str)

    args = parser.parse_args()

    if args.mode == "api":
        uvicorn.run("main:app", host="0.0.0.0", port=8000)  # <-- main:app (pas app directement)
    elif args.mode == "analyse":
        run_analyse(args.pair, args.interval)
    elif args.mode == "fetch":
        run_fetch(args.pair)
    elif args.mode == "fetch_contracts":
        run_fetch_contracts()
    elif args.mode == "run_all":
        run_all_4h()

if __name__ == "__main__":
    main()