# Log Analyzer CLI Tool

A small, cross-platform command-line utility to analyze plain-text log files. It scans a log file and counts lines that start with the common log level prefixes: `INFO`, `WARNING`, and `ERROR`. The tool prints a quick summary to the console and writes a simple report file to `output/report.txt` by default.

## Highlights

- Fast, zero-dependency Python script (single-file: `analyzer.py`).
- Counts `INFO`, `WARNING`, and `ERROR` lines.
- Writes a human-readable report to a file (default `output/report.txt`).

## Requirements

- Python 3.7 or newer.
- No external Python packages required.

## Quickstart — Windows PowerShell

1. Open PowerShell and change to the project folder (replace the path below if different):

```powershell
cd 'C:\Filename\Log-analyzer'
```

2. Run the analyzer against a log file (example: `logs/example.log`). The script prints a summary and creates `output/report.txt` by default:

```powershell
python .\analyzer.py .\logs\your-log-file.log
```

3. To specify a custom output file:

```powershell
python .\analyzer.py .\logs\your-log-file.log -o .\output\my-report.txt
```

## Example

Given a log file `logs/server.log` that contains lines like:

```
INFO Server started
WARNING High memory usage detected
ERROR Failed to open socket
INFO New connection
```

The script will print something like:

```
Log Summary: {'INFO': 2, 'WARNING': 1, 'ERROR': 1}
Report saved to output/report.txt
```

And `output/report.txt` will contain:

```
INFO: 2
WARNING: 1
ERROR: 1
```

## Project layout

- `analyzer.py` — main script. Run this directly with Python.
- `logs/` — example input logs (add your own logs here).
- `output/` — generated reports are written here.
- `README.md`, `LICENSE` — repo metadata.

## Usage contract (short)

- Input: path to a plain-text log file where log lines start with `INFO`, `WARNING`, or `ERROR`.
- Output: console summary (dict) and a text report written to the `-o/--output` path (default: `output/report.txt`).
- Errors: script raises a readable Python exception if the input file does not exist or is not readable.

## Notes & edge cases

- The parser looks for lines that start with the exact prefixes `INFO`, `WARNING`, or `ERROR` (case-sensitive). If your logs use another format (timestamps before level, different casing, or bracketed levels like `[ERROR]`), you'll need to adapt `parse_log_file` in `analyzer.py`.
- Large log files are processed line-by-line and should work with modest memory usage, but there is no progress indicator for very large files..

## Contributing

Contributions are welcome. Please open an issue or submit a pull request with a clear description of your change.

## License

This project includes a `LICENSE` file in the repository root. Check it for terms.