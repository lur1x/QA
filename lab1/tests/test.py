import subprocess
import sys
import os

def run_triangle_test(parts):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        triangle_path = os.path.join(script_dir, '../triangle_app/triangle_app.py')

        result = subprocess.run(
            [sys.executable, triangle_path, parts[0], parts[1], parts[2]],
            capture_output=True,
            text=True,
            timeout=5
        )

        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        return "unknown_error"
    except Exception as e:
        print(f"Error running test: {e}")
        return "unknown_error"


def run_tests_from_file(input_file, output_file):
    results = []
    test_count = 0
    passed_count = 0

    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        input_path = os.path.join(script_dir, input_file)

        print(f"Opening file: {input_path}")

        with open(input_path, 'r', encoding='utf-8') as f:
            test_cases = f.readlines()

        for line_num, line in enumerate(test_cases, 1):
            line = line.strip()

            if not line:
                continue

            test_count += 1

            print(f"Processing test {test_count}: {line}")

            parts = line.split()

            try:

                expected = parts[-1]

                actual = run_triangle_test(parts[:-1])

                if actual.lower() == expected.lower():
                    results.append("success")
                    passed_count += 1
                    print(f"  Test passed: expected '{expected}', got '{actual}'")
                else:
                    results.append("error")
                    print(f"  Test failed: expected '{expected}', got '{actual}'")



            except Exception as e:
                print(f"Error processing line {line_num}: {e}")
                results.append("error")

        output_path = os.path.join(script_dir, output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            for result in results:
                f.write(result + "\n")

        print(f"\nTest results:")
        print(f"Total tests: {test_count}")
        print(f"Passed: {passed_count}")
        print(f"Failed: {test_count - passed_count}")
        print(f"Results saved to file: {output_path}")

    except FileNotFoundError:
        print(f"Error: file {input_file} not found")
        print(f"Current directory: {os.getcwd()}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python tester.py <input_file> <output_file>")
        print("Example: python tester.py test_cases_eng.txt results.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    triangle_path = os.path.join(script_dir, '../triangle_app/triangle_app.py')

    if not os.path.exists(triangle_path):
        print(f"Error: triangle.py file not found at path: {triangle_path}")
        print("Create triangle.py file or rename triangle.py to triangle_eng.py")
        sys.exit(1)

    run_tests_from_file(input_file, output_file)


if __name__ == "__main__":
    sys.exit(main())