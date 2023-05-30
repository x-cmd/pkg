
import os
import csv

# | id | candidate \ osarch | <file1> | <file2> |
# | -- | ----------------- | ------- | ------- |
# | 1 | <candidate1>      | <value> | <value> |

def main():
    """
    combine all csv files in the doc/xbin directory into
    a single markdown table use different row for each file
    write the table to doc/xbin/README.md
    """
    # file end with .csv at doc/xbin
    file_list = [file[:-4] for file in os.listdir("doc/xbin") if file.endswith(".csv")]
    title = "| id | candidate \ osarch | " + " | ".join(file_list) + " |"
    title = title + "\n| -- | ---- | " + " | ".join(["-------"] * len(file_list)) + " |"
    with open("doc/xbin/README.md", "w", encoding='utf-8') as f:
        f.write("# X-Bin\n")
        f.write(title)

    res = {}
    for root, dirs, files in os.walk("doc/xbin"):
        for file in files:
            if file.endswith(".csv"):
                with open(os.path.join(root, file), newline='', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                    for row in reader:
                        res[ row[0].strip() ] = res.get(row[0].strip(), []) + [row[1].strip()]

    with open("doc/xbin/README.md", "a" , encoding='utf-8') as f:
        count = 1
        for k, v in res.items():
            f.write("\n| " + str(count) + " | " + k + " | " + " | ".join(v) + " |")
            count += 1

def gen_error_map():
    """
    if row[1] == "❌" then
    """

    error_map = {}
    unsupport_map = {}
    total_map = {}
    for i in [file for file in os.listdir("doc/xbin") if file.endswith(".csv")] :
        error_map[i] = []
        unsupport_map[i] = []
        total_map[i] = []

    for root, dirs, files in os.walk("doc/xbin"):
        for file in files:
            if not file.endswith(".csv"):
                continue
            with open(os.path.join(root, file), newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row in reader:
                    if "❌" in row[1].strip():
                        error_map[ file.strip() ] = error_map.get(file.strip(), []) + [row[0].strip()]
                    if row[1].strip() == "-":
                        unsupport_map[ file.strip() ] = unsupport_map.get(file.strip(), []) + [row[0].strip()]
                    total_map[ file.strip() ] = total_map.get(file.strip(), []) + [row[0].strip()]

    with open("doc/xbin/README.md", "a", encoding='utf-8') as f:
        f.write("\n\n## Error Map\n")
        for osarch, error_cand in error_map.items():
            f.write("\n- " +  osarch[:-4] + "  error=" + str(len(error_cand)) + \
                "  unsupport=" + str(len(unsupport_map[osarch])) + "  total=" + str(len(total_map[osarch])) + \
                "  error_rate=" + str(len(error_cand) / len(total_map[osarch]))[:5])

if __name__ == "__main__":
    print("generate table")
    main()
    gen_error_map()
