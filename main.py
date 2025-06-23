import argparse

from src.Analyser import Analyser



def main():
    parser = argparse.ArgumentParser(description="Exemple de script avec paramètres.")
    parser.add_argument('--pair', type=str, help="Pair")
    parser.add_argument('--intervals', type=str, help="Interval")
    args = parser.parse_args()

    analyser = Analyser()
    analyser.loadKline(args.pair, args.intervals)
    # for pair in pairs:
    #     intervals = list(data[pair]['intervals'])
    #
    #     jsonLoader = Loader(CONFIG.data['type_loader'])
    #     # run_analys(pair, intervals)
    # print(pairs)


if __name__ == "__main__":
    main()
