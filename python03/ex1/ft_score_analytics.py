#!/usr/bin/python3.10
import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) > 1:
        total = 0
        n = len(sys.argv[1:])
        for i in sys.argv[1:]: ## bucle convertir los argumento en int
            total += int(i) ## int(i) son cada argumento ya que sys.argv[i] es una lista
        print(f"Scores processed: {sys.argv[1:]}") ## [1:] omitir nombre de archivo ya que es sys.argv[0]
        print(f"Total players: {n}")
        print(f"Total score: {total}")
        print(f"Average score: ")
        print(f"High score: ")
        print(f"Low score: ")
        print(f"Score range: ")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
