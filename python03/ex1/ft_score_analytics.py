#!/usr/bin/python3.10
import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) > 1:
        scores = []
        for i in sys.argv[1:]:   # bucle convertir los argumento en int
            try:
                scores.append(int(i))  # Añadir un elemento a una lista
                # int(i) son cada argumento ya que sys.argv[i] es una lista
            except ValueError:
                print(f"Invalid parameter: '{i}'")
        if scores:
            print(f"Scores processed: {scores}")
            # [1:] omitir nombre de archivo ya que es sys.argv[0]
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        else:
            print("No scores provided. Usage: "
                  "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
