# main.py

import hydra

@hydra.main()
def main(cfg):
    print(cfg)

if __name__ == '__main__':
    main()