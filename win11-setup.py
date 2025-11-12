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
# Create counters to track installation results
installed_count = 0
already_installed_count = 0
failed_count = 0

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
    # --force = force installation even if already installed
    # --disable-interactivity = disable all interactive prompts
    # capture_output=True captures what winget prints so we can check it
    # text=True makes the output a string instead of bytes
    result = subprocess.run(
        ["winget", "install", "-e", "--id", program_id, "-h", "--accept-package-agreements", "--accept-source-agreements", "--disable-interactivity"],
        capture_output=True,
        text=True
    )
    
    # Check if the program was already installed by looking at winget's output
    if "already installed" in result.stdout.lower():
        print(f"{program_id} is already installed.")
        already_installed_count += 1
    # Check if the installation succeeded (returncode 0 means success)
    elif result.returncode == 0:
        print(f"Installed {program_id} successfully.")
        installed_count += 1
    # If we get here, something went wrong
    else:
        print(f"Failed to install {program_id}.")
        failed_count += 1
    
    # Increment the counter for the next program (shorthand for counter = counter + 1)
    counter += 1

# Print summary of installation results
print("\n" + "="*50)
print("INSTALLATION SUMMARY")
print("="*50)
print(f"Total programs processed: {len(programs)}")
print(f"Successfully installed: {installed_count}")
print(f"Already installed: {already_installed_count}")
print(f"Failed to install: {failed_count}")
print("="*50)

# Now update only the programs in our list to ensure they are on the latest version
print("\nNow updating programs from the installation list to latest versions...")

# Create counters to track update results
updated_count = 0
already_latest_count = 0

for program_id in programs:
    print(f"Updating {program_id}...")
    update_result = subprocess.run(
        ["winget", "upgrade", "-e", "--id", program_id, "-h", "--accept-package-agreements", "--accept-source-agreements", "--disable-interactivity"],
        capture_output=True,
        text=True
    )
    
    # Check if the program was already at the latest version
    if "No applicable update found" in update_result.stdout or "No installed package found" in update_result.stdout:
        already_latest_count += 1
    # Check if the update succeeded (returncode 0 means success)
    elif update_result.returncode == 0:
        updated_count += 1

print("\nUpdate process completed for all programs in the list.")

# Print summary of update results
print("\n" + "="*50)
print("UPDATE SUMMARY")
print("="*50)
print(f"Programs updated: {updated_count}")
print(f"Already on latest version: {already_latest_count}")
print("="*50)

