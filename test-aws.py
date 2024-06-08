import subprocess

def test_aws_cli():
    # Verify AWS CLI installation
    try:
        output = subprocess.check_output(["aws", "--version"])
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e)

    # Verify AWS CLI configuration
    try:
        output = subprocess.check_output(["aws", "sts", "get-caller-identity"])
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("Error:", e)

if __name__ == "__main__":
    test_aws_cli()
