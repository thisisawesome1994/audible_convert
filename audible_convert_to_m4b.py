import os
import subprocess
import sys

def main():
    # Ensure the -activation_bytes argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <activation_bytes>")
        sys.exit(1)

    activation_bytes = sys.argv[1]

    # Get the list of .aax files in the current directory
    aax_files = [f for f in os.listdir('.') if f.endswith('.aax')]

    if not aax_files:
        print("No .aax files found in the current directory.")
        sys.exit(0)

    # Iterate over each .aax file and execute the ffmpeg command
    for aax_file in aax_files:
        # Extract the base name without the extension
        base_name = os.path.splitext(aax_file)[0]
        output_file = f"{base_name}.m4b"

        # Construct the ffmpeg command
        command = [
            "./ffmpeg.exe",
            "-y",
            f"-activation_bytes",
            activation_bytes,
            "-i",
            f"./{aax_file}",
            "-codec",
            "copy",
            output_file
        ]

        print(f"Processing: {aax_file} -> {output_file}")
        try:
            # Run the ffmpeg command
            subprocess.run(command, check=True)
            print(f"Successfully processed: {aax_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {aax_file}: {e}")

if __name__ == "__main__":
    main()