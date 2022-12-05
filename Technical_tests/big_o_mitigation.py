import sys
import json
import pandas as pd


class Problem1:
    def __init__(self, template_loc=""):
        if template_loc == "":
            print("Template missing please correct")
            exit()

        with open(template_loc) as template_file:
            parameters = json.load(template_file)

        df = pd.read_csv(parameters["files"]["input1"], sep=" ", header=None)
        self.data = df[0].to_list()

    @staticmethod
    def find_two(data):
        data.sort()
        target = 2020
        result_out = {}

        for value in data:
            result = target - value
            if result in data:
                print(f"Found values that add to {target}\n{value} + {result}\nWhich multiply to {value*result}\n")
                result_out = {
                    "value_a": value, "value_b": result, "multiply": (value*result)
                }
                return result_out

        result_out["error"] = "Couldn't find any working values"
        print(result_out["error"])
        return result_out

    @staticmethod
    def find_three(data):
        data.sort()
        target = 2020
        result_out = {}

        for i, value_a in enumerate(data):
            sum_result = target - value_a
            for value_b in data[i:]:
                result = sum_result - value_b
                if result in data[i:]:
                    print(f"Found values that add to {target}\n{value_a} + {value_b} + {result}"
                          f"\nWhich multiply to {value_a * value_b * result}\n")
                    result_out = {
                        "value_a": value_a, "value_b": value_b, "value_c": result, "multiply": (value_a*value_b*result)
                    }
                    return result_out

        result_out["error"] = "Couldn't find any working values"
        print(result_out["error"])
        return result_out


class Problem2:
    def __init__(self, template_loc=""):
        if template_loc == "":
            print("Template missing please correct")
            exit()

        with open(template_loc) as template_file:
            parameters = json.load(template_file)

        self.data = pd.read_csv(parameters["files"]["input2"], sep=" ", header=None)

    @staticmethod
    def str_count(data):
        passes = 0

        data = data.rename(columns={0: "range", 1: "character", 2: "string"})
        data["character"] = data["character"].str.replace(":", "")

        for i, row in data.iterrows():
            str_range = row["range"].split("-")
            if int(str_range[0]) >= int(str_range[1]):
                print(f"Impossible range given of {str_range}")
                continue
            if int(str_range[0]) <= row["string"].count(row["character"]) <= int(str_range[1]):
                passes += 1

        print(f"{passes} records passed the criteria for problem 2.a\n")

        return passes

    @staticmethod
    def position_count(data):
        passes = 0

        data = data.rename(columns={0: "position", 1: "character", 2: "string"})
        data["character"] = data["character"].str.replace(":", "")

        for i, row in data.iterrows():
            check = 0
            str_pos = row["position"].split("-")
            if len(row["string"]) >= int(str_pos[0]):
                if row["string"][int(str_pos[0])-1] == row["character"]:
                    check += 1
            if len(row["string"]) >= int(str_pos[1]):
                if row["string"][int(str_pos[1])-1] == row["character"]:
                    check += 1
            if check == 1:
                passes += 1

        print(f"{passes} records passed the criteria for problem 2.b\n")

        return passes


def main():

    problem1 = Problem1(sys.argv[1])
    problem1.find_two(problem1.data)
    problem1.find_three(problem1.data)

    problem2 = Problem2(sys.argv[1])
    problem2.str_count(problem2.data)
    problem2.position_count(problem2.data)


if __name__ == "__main__":
    main()
