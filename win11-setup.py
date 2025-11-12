# Import the subprocess module to run command-line programs from Python
import subprocess

# List of programs to install using their winget package IDs
programs = [
    "Python.Python.3.13",
    "Microsoft.WindowsTerminal",
    "Microsoft.VisualStudioCode",
    "Microsoft.PowerShell",
    "Mozilla.Firefox",
    "Microsoft.PowerToys",
    "Google.Chrome",
    "Git.Git",
    "GitHub.GitHubDesktop",
    "OpenJS.NodeJS.LTS",
    "VideoLAN.VLC",
    "7zip.7zip"
]

# Print a message showing how many programs we're about to install
print(f"Now attempting to install {len(programs)} programs via winget.")

# Create a counter to track which program we're installing
counter = 1

# Loop through each program in the list
for program_id in programs:
    # Show progress: which program we're installing and the count (e.g., "1/8")
    print(f"\nInstalling {program_id} ({counter}/{len(programs)})....")
    
    # Run the winget install command
    # -e = exact match on package ID
    # --id = specify package by ID
    # -h = silent installation (no user prompts)
    # --accept-package-agreements = auto-accept package licenses
    # --accept-source-agreements = auto-accept source agreements
    # capture_output=True captures what winget prints so we can check it
    # text=True makes the output a string instead of bytes
    result = subprocess.run(
        ["winget", "install", "-e", "--id", program_id, "-h", "--accept-package-agreements", "--accept-source-agreements"],
        capture_output=True,
        text=True
    )
    
    # Check if the program was already installed by looking at winget's output
    if "already installed" in result.stdout.lower():
        print(f"{program_id} is already installed.")
    # Check if the installation succeeded (returncode 0 means success)
    elif result.returncode == 0:
        print(f"Installed {program_id} successfully.")
    # If we get here, something went wrong
    else:
        print(f"Failed to install {program_id}.")
    
    # Increment the counter for the next program (shorthand for counter = counter + 1)
    counter += 1
