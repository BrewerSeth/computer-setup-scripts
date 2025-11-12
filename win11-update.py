# Import the subprocess module to run command-line programs from Python
import subprocess

# Print a message indicating we're starting the update process
print("Now attempting to update all winget programs...")

# Run the winget upgrade command for all programs
# --all updates every installed program
# -h = silent installation (no user prompts)
# --accept-package-agreements automatically accepts license agreements
# --accept-source-agreements automatically accepts source agreements
result = subprocess.run(
    ["winget", "upgrade", "--all", "-h", "--accept-package-agreements", "--accept-source-agreements"],
    capture_output=True,
    text=True
)

# Print that the update process is complete
print("\nUpdate process completed.")

# Print the output from winget so you can see what happened
print("\nWinget output:")
print(result.stdout)
