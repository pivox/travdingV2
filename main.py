import argparse

from src.configLoader import CONFIG

def run_analys(pair, interval):
    data = CONFIG.get_active_pairs()
    pairs_dict = data
    print(pair)
    if pair in list(pairs_dict.keys()):
        print("ok")
    else:
        print("error")
    if interval in list(data[pair]['intervals']):
        print("ok")
    else:
        print("error")



def main():
    parser = argparse.ArgumentParser(description="Exemple de script avec paramètres.")
    parser.add_argument('--pair', type=str, help="Pair")
    parser.add_argument('--interval', type=str, help="Interval")
    args = parser.parse_args()
    run_analys(args.pair, args.interval)
    data = CONFIG.get_active_pairs()

    pairs_dict = data
    pairs = list(pairs_dict.keys())
    # for pair in pairs:
    #     intervals = list(data[pair]['intervals'])
    #
    #     jsonLoader = JsonLoader(CONFIG.data['type_loader'])
    #     # run_analys(pair, intervals)
    # print(pairs)


if __name__ == "__main__":
    main()
