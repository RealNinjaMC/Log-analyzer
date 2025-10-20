import argparse
import os

def parse_log_file(file_path):
    """
    Reads a log file and counts the number of INFO, WARNING, and ERROR lines.
    """
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("INFO"):
                counts["INFO"] += 1
            elif line.startswith("WARNING"):
                counts["WARNING"] += 1
            elif line.startswith("ERROR"):
                counts["ERROR"] += 1

    return counts

def write_report(counts, output_file):
    """
    Writes the summary report to a file.
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as f:
        for level, count in counts.items():
            f.write(f"{level}: {count}\n")

    print(f"Report saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Log Analyzer Tool")
    parser.add_argument("logfile", help="Path to the log file")
    parser.add_argument("-o", "--output", default="output/report.txt", help="Output report file")
    args = parser.parse_args()

    counts = parse_log_file(args.logfile)
    print("Log Summary:", counts)
    write_report(counts, args.output)

if __name__ == "__main__":
    main()
