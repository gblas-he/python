from typing import Any, Protocol
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    name: str = "Data Processor"

    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise ValueError("No data available")
        item = self._data.pop(0)
        current_rank = self._rank
        self._rank += 1
        return (current_rank, item)


class NumericProcessor(DataProcessor):
    name: str = "Numeric Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for x in data:
                self._data.append(str(x))
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    name: str = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for x in data:
                self._data.append(x)
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):
    name: str = "Log Processor"

    def _is_valid_dict(self, d: Any) -> bool:
        return (
            isinstance(d, dict)
            and "log_level" in d
            and "log_message" in d
            and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()
            )
        )

    def validate(self, data: Any) -> bool:
        if self._is_valid_dict(data):
            return True
        if isinstance(data, list) and len(data) > 0:
            return all(self._is_valid_dict(x) for x in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for x in data:
                self._data.append(f"{x['log_level']}: {x['log_message']}")
        else:
            self._data.append(f"{data['log_level']}: {data['log_message']}")


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(val for _, val in data))


class JSONPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = ", ".join(f'"item_{rank}": "{val}"' for rank, val in data)
        print("{" + items + "}")


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    "DataStream error - Can't process element "
                    f"in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
        else:
            for proc in self._processors:
                total = len(proc._data) + proc._rank
                remaining = len(proc._data)
                print(f"{proc.name}: total {total} items processed, "
                      f"remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            extracted: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    extracted.append(proc.output())
                except ValueError:
                    break
            if extracted:
                plugin.process_output(extracted)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors\n")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(num_proc)
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    batch1: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch1}\n")
    ds.process_stream(batch1)
    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVPlugin())
    print()
    ds.print_processors_stats()

    batch2: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"\nSend another batch of data: {batch2}\n")
    ds.process_stream(batch2)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONPlugin())
    print()
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
